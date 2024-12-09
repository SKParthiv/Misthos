import sqlite3

def create_tables():
    conn = sqlite3.connect('misthos.db')
    c = conn.cursor()
    
    # Create users table
    c.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            real_name TEXT NOT NULL,
            age INTEGER,
            education_lvl TEXT,
            email TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
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
            avatar TEXT,
            free_stat_points INTEGER
        )
    ''')
    
    # Create quests table
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
            FOREIGN KEY(user_email) REFERENCES users(email)
        )
    ''')
    
    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_tables()