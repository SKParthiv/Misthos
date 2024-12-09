import openai
import sqlite3
from datetime import datetime
from classes.user import User

class Quest:
    def __init__(self, title, description, completion_evidence, reward, punishment=None, user_email=None, due_date=None, due_time=None):
        self.title = title
        self.description = description
        self.completion_evidence = completion_evidence
        self.reward = reward
        self.punishment = punishment
        self.user_email = user_email
        self.due_date = due_date
        self.due_time = due_time

    @staticmethod
    def generate_reward(user_email, quest_title, quest_description):
        user = User.get_user_by_email(user_email)
        if user:
            user_info = {
                "real_name": user.real_name,
                "age": user.age,
                "education_lvl": user.education_lvl,
                "email": user.email,
                "field_of_education": user.field_of_education,
                "hobbies": user.hobbies,
                "likes": user.likes,
                "dislikes": user.dislikes,
                "player": user.player,
                "task_title": quest_title,
                "task_description": quest_description
            }

            openai.api_key = 'your_openai_api_key'
            response = openai.Completion.create(
                engine="davinci",
                prompt=(
                    f"Based on the following data: {user_info}, generate the amount of exp awarded. "
                    f"For example, the amount of exp awarded to a 15 year old with avg grades and good intellect "
                    f"to solve a simple quadratic equation word problem (he knows how to solve and has practiced it) is 100 exp. "
                    f"Reply with a single number only."
                ),
                max_tokens=10
            )
            reward_exp = int(response.choices[0].text.strip())
            return {"exp": reward_exp}
        return None

    @staticmethod
    def generate_punishment(user_email, quest_title, quest_description):
        user = User.get_user_by_email(user_email)
        if user:
            user_info = {
                "real_name": user.real_name,
                "age": user.age,
                "education_lvl": user.education_lvl,
                "email": user.email,
                "field_of_education": user.field_of_education,
                "hobbies": user.hobbies,
                "likes": user.likes,
                "dislikes": user.dislikes,
                "player": user.player,
                "task_title": quest_title,
                "task_description": quest_description
            }

            openai.api_key = 'your_openai_api_key'
            response = openai.Completion.create(
                engine="davinci",
                prompt=(
                    f"Based on the following data: {user_info}, generate the amount of exp loss as punishment. "
                    f"For example, the amount of exp loss for a 15 year old with avg grades and good intellect "
                    f"for failing to solve a simple quadratic equation word problem (he knows how to solve and has practiced it) is 50 exp. "
                    f"Reply with a single number only."
                ),
                max_tokens=10
            )
            punishment_exp_loss = int(response.choices[0].text.strip())
            return {"exp_loss": punishment_exp_loss}
        return None

    @staticmethod
    def create_table():
        conn = sqlite3.connect('misthos.db')
        c = conn.cursor()
        c.execute('''
            CREATE TABLE IF NOT EXISTS quests (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                description TEXT NOT NULL,
                completion_evidence TEXT,
                reward TEXT,
                punishment TEXT,
                user_email TEXT,
                due_date TEXT,
                due_time TEXT,
                status TEXT DEFAULT 'pending',
                FOREIGN KEY(user_email) REFERENCES users(email)
            )
        ''')
        conn.commit()
        conn.close()

    def save_to_db(self):
        self.create_table()
        conn = sqlite3.connect('misthos.db')
        c = conn.cursor()
        c.execute('''INSERT INTO quests (title, description, completion_evidence, reward, punishment, user_email, due_date, due_time, status)
                     VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                  (self.title, self.description, self.completion_evidence, str(self.reward), str(self.punishment), self.user_email, self.due_date, self.due_time, 'pending'))
        conn.commit()
        conn.close()

    @staticmethod
    def get_pending_quests(user_email):
        conn = sqlite3.connect('misthos.db')
        c = conn.cursor()
        c.execute('SELECT * FROM quests WHERE user_email = ? AND status = ?', (user_email, 'pending'))
        quests_data = c.fetchall()
        conn.close()
        return [Quest(*data[1:]) for data in quests_data]

    def complete(self):
        user = User.get_user_by_email(self.user_email)
        if user:
            # Apply reward to the user
            user.player.gain_experience(self.reward.get('exp', 0))
            user.save()
        self.update_status('completed')

    def fail(self):
        user = User.get_user_by_email(self.user_email)
        if user and self.punishment:
            # Apply punishment to the user
            user.player.exp -= self.punishment.get('exp_loss', 0)
            if user.player.exp < 0:
                user.player.exp = 0
            user.save()
        self.update_status('failed')

    def update_status(self, status):
        conn = sqlite3.connect('misthos.db')
        c = conn.cursor()
        c.execute('UPDATE quests SET status = ? WHERE title = ? AND description = ?', (status, self.title, self.description))
        conn.commit()
        conn.close()

    def delete(self):
        conn = sqlite3.connect('misthos.db')
        c = conn.cursor()
        c.execute('DELETE FROM quests WHERE title = ? AND description = ?', (self.title, self.description))
        conn.commit()
        conn.close()

    def save(self):
        user = User.get_user_by_email(self.user_email)
        if user:
            user.quests.append(self.__dict__)
            user.save()
