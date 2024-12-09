import json
import sqlite3
from .job_class import JobClass
from .item import Avatar

class Player:
    def __init__(self, player_name, strength=5, agility=5, stamina=5, vitality=5, intelligence=5, lvl=1, exp=0, free_stat_point=0):
        self.player_name = player_name
        self.strength = strength
        self.agility = agility
        self.stamina = stamina
        self.vitality = vitality
        self.intelligence = intelligence
        self.lvl = lvl
        self.exp = exp
        self.free_stat_points = 0

    def gain_experience(self, exp):
        self.exp += exp
        while self.exp >= self.lvl * 100:  # Example level-up logic
            self.exp -= self.lvl * 100
            self.lvl += 1
            self.free_stat_points += 5  # Example stat points gained per level

    def update_stat(self, stat, value):
        if self.free_stat_points >= value:
            setattr(self, stat, getattr(self, stat) + value)
            self.free_stat_points -= value

    def __dict__(self):
        return {
            "player_name": self.player_name,
            "strength": self.strength,
            "agility": self.agility,
            "stamina": self.stamina,
            "vitality": self.vitality,
            "intelligence": self.intelligence,
            "lvl": self.lvl,
            "exp": self.exp,
            "free_stat_points": self.free_stat_points
        }
    
    def calculate_hp(self):
        return self.vitality * 10

    def calculate_mp(self):
        return self.intelligence * 10

    def calculate_sp(self):
        return self.stamina * 10

    def level_up(self):
        self.lvl += 1
        self.exp = 0
        self.strength += 1
        self.agility += 1
        self.stamina += 1
        self.vitality += 1
        self.intelligence += 1
        self.free_stat_points += 3
        self.hp = self.calculate_hp()
        self.mp = self.calculate_mp()
        self.sp = self.calculate_sp()

    def take_damage(self, damage):
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0

    def use_mana(self, amount):
        self.mp -= amount
        if self.mp < 0:
            self.mp = 0

    def use_stamina(self, amount):
        self.sp -= amount
        if self.sp < 0:
            self.sp = 0

    def gain_experience(self, exp):
        self.exp += exp
        if self.exp >= self.lvl * 10:  # Example level-up condition
            self.level_up()

    def allocate_stat_points(self, strength=0, agility=0, stamina=0, vitality=0, intelligence=0):
        total_points = strength + agility + stamina + vitality + intelligence
        if total_points <= self.free_stat_points:
            self.strength += strength
            self.agility += agility
            self.stamina += stamina
            self.vitality += vitality
            self.intelligence += intelligence
            self.free_stat_points -= total_points
            self.hp = self.calculate_hp()
            self.mp = self.calculate_mp()
            self.sp = self.calculate_sp()
        else:
            raise ValueError("Not enough free stat points")

class User:
    def __init__(self, real_name, age, education_lvl, email, password, field_of_education, hobbies, school_attending, likes, dislikes, player, quests=[]):
        self.real_name = real_name
        self.age = age
        self.education_lvl = education_lvl
        self.email = email
        self.password = password
        self.field_of_education = field_of_education
        self.hobbies = hobbies
        self.school_attending = school_attending
        self.likes = likes
        self.dislikes = dislikes
        self.player = player
        self.quests = quests

    @staticmethod
    def create_table():
        conn = sqlite3.connect('misthos.db')
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY,
                        real_name TEXT,
                        age INTEGER,
                        education_lvl TEXT,
                        email TEXT,
                        password TEXT,
                        field_of_education TEXT,
                        hobbies TEXT,
                        school_attending TEXT,
                        likes TEXT,
                        dislikes TEXT,
                        player_name TEXT,
                        strength INTEGER,
                        agility INTEGER,
                        stamina INTEGER,
                        vitality INTEGER,
                        intelligence INTEGER,
                        lvl INTEGER,
                        exp INTEGER,
                        free_stat_points INTEGER
                    )''')
        conn.commit()
        conn.close()

    def save(self):
        conn = sqlite3.connect('misthos.db')
        c = conn.cursor()
        c.execute('''INSERT INTO users (real_name, age, education_lvl, email, password, field_of_education, hobbies, school_attending, likes, dislikes, player_name, strength, agility, stamina, vitality, intelligence, lvl, exp, free_stat_points)
                     VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                  (self.real_name, self.age, self.education_lvl, self.email, self.password, self.field_of_education, self.hobbies, self.school_attending, self.likes, self.dislikes, self.player.player_name, self.player.strength, self.player.agility, self.player.stamina, self.player.vitality, self.player.intelligence, self.player.lvl, self.player.exp, self.player.free_stat_points))
        conn.commit()
        conn.close()

    def update(self, **kwargs):
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)
        self.save()

    @staticmethod
    def get_user_by_email(email):
        conn = sqlite3.connect('misthos.db')
        c = conn.cursor()
        c.execute('SELECT * FROM users WHERE email = ?', (email,))
        user_data = c.fetchone()
        conn.close()
        if user_data:
            player = Player(user_data[12], user_data[13], user_data[14], user_data[15], user_data[16], user_data[17], user_data[18], user_data[19], user_data[20])
            return User(user_data[1], user_data[2], user_data[3], user_data[4], user_data[5], user_data[6], user_data[7], user_data[8], user_data[9], user_data[10], user_data[11], player)
        return None

    @staticmethod
    def delete_user(email):
        conn = sqlite3.connect('misthos.db')
        c = conn.cursor()
        c.execute('DELETE FROM users WHERE email = ?', (email,))
        conn.commit()
        conn.close()

    def update_from_db(self):
        conn = sqlite3.connect('misthos.db')
        c = conn.cursor()
        c.execute('SELECT * FROM users WHERE email = ?', (self.email,))
        user_data = c.fetchone()
        conn.close()
        if user_data:
            self.real_name = user_data[1]
            self.age = user_data[2]
            self.education_lvl = user_data[3]
            self.email = user_data[4]
            self.password = user_data[5]
            self.field_of_education = user_data[6]
            self.hobbies = user_data[7]
            self.school_attending = user_data[8]
            self.likes = user_data[9]
            self.dislikes = user_data[10]
            self.player = Player(user_data[11], user_data[12], user_data[13], user_data[14], user_data[15], user_data[16], user_data[17], user_data[18], user_data[19])
