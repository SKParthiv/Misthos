import openai
import sqlite3
from datetime import datetime
from classes.user import User

class Quest:
    def __init__(self, title, description, completion_evidence, reward, punishment=None, user_email=None, due_date=None, due_time=None, priority=1):
        self.title = title
        self.description = description
        self.completion_evidence = completion_evidence
        self.reward = reward
        self.punishment = punishment
        self.user_email = user_email
        self.due_date = ?
        self.due_time = due_time
        self.priority = priority

    @staticmethod
    def generate_reward(priority):
        reward_exp = priority * 100  # Example fixed reward calculation
        return {"exp": reward_exp}

    @staticmethod
    def generate_punishment(priority):
        punishment_exp_loss = priority * 50  # Example fixed punishment calculation
        return {"exp_loss": punishment_exp_loss}

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
                priority INTEGER,
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
        c.execute('''INSERT INTO quests (title, description, completion_evidence, reward, punishment, user_email, due_date, due_time, priority, status)
                     VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                  (self.title, self.description, self.completion_evidence, str(self.reward), str(self.punishment), self.user_email, self.due_date, self.due_time, self.priority, 'pending'))
        conn.commit()
        conn.close()

    @staticmethod
    def get_pending_quests(user_email):
        conn = sqlite3.connect('misthos.db')
        c = conn.cursor()
        c.execute('SELECT * FROM quests WHERE user_email = ? AND status = ? ORDER BY priority DESC', (user_email, 'pending'))
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
