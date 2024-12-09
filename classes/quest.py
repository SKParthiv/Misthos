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
        conn = sqlite3.connect('misthos.db')
        c = conn.cursor()
        c.execute('SELECT * FROM users WHERE email = ?', (user_email,))
        user_data = c.fetchone()
        conn.close()

        if user_data:
            user_info = {
                "real_name": user_data[1],
                "age": user_data[2],
                "education_lvl": user_data[3],
                "email": user_data[4],
                "field_of_education": user_data[6],
                "hobbies": user_data[7],
                "likes": user_data[9],
                "dislikes": user_data[10],
                "player": user_data[11],
                "task_title": quest_title,
                "task_description": quest_description
            }

            openai.api_key = 'your_openai_api_key'
            response = openai.Completion.create(
                engine="davinci",
                prompt=f"Generate a reward for the user based on the following data: {user_info}",
                max_tokens=50
            )
            reward = response.choices[0].text.strip()
            return reward
        return None

    @staticmethod
    def generate_punishment(user_email, quest_title, quest_description):
        conn = sqlite3.connect('misthos.db')
        c = conn.cursor()
        c.execute('SELECT * FROM users WHERE email = ?', (user_email,))
        user_data = c.fetchone()
        conn.close()

        if user_data:
            user_info = {
                "real_name": user_data[1],
                "age": user_data[2],
                "education_lvl": user_data[3],
                "email": user_data[4],
                "field_of_education": user_data[6],
                "hobbies": user_data[7],
                "likes": user_data[9],
                "dislikes": user_data[10],
                "player": user_data[11],
                "task_title": quest_title,
                "task_description": quest_description
            }

            openai.api_key = 'your_openai_api_key'
            response = openai.Completion.create(
                engine="davinci",
                prompt=f"Generate a punishment for the user based on the following data: {user_info}",
                max_tokens=50
            )
            punishment = response.choices[0].text.strip()
            return punishment
        return None

    def complete(self):
        user = User.get_user_by_email(self.user_email)
        if user:
            # Apply reward to the user
            user.player.gain_experience(self.reward.get('exp', 0))
            user.player.free_stat_points += self.reward.get('free_stat_points', 0)
            # Add logic for items if needed
            user.save()

    def fail(self):
        user = User.get_user_by_email(self.user_email)
        if user and self.punishment:
            # Apply punishment to the user
            # Example: reduce experience points
            user.player.exp -= self.punishment.get('exp_loss', 0)
            if user.player.exp < 0:
                user.player.exp = 0
            user.save()

    def delete(self):
        conn = sqlite3.connect('misthos.db')
        c = conn.cursor()
        c.execute('DELETE FROM quests WHERE title = ? AND description = ?', (self.title, self.description))
        conn.commit()
        conn.close()

    def save(self):
        conn = sqlite3.connect('misthos.db')
        c = conn.cursor()
        c.execute('''INSERT INTO quests (title, description, completion_evidence, reward, punishment, user_email, due_date, due_time)
                     VALUES (?, ?, ?, ?, ?, ?, ?, ?)''',
                  (self.title, self.description, self.completion_evidence, self.reward, self.punishment, self.user_email, self.due_date, self.due_time))
        conn.commit()
        conn.close()
