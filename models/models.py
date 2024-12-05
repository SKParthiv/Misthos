import sqlite3
import os
import json
from datetime import datetime

# Database folder and file
DB_FOLDER = "database"
DB_NAME = os.path.join(DB_FOLDER, "productivity_app.db")


def ensure_db_folder_exists():
    """Ensure that the database folder exists."""
    if not os.path.exists(DB_FOLDER):
        os.makedirs(DB_FOLDER)


class BaseModel:
    """Base model to handle shared database connection logic."""

    @staticmethod
    def connect():
        return sqlite3.connect(DB_NAME)

    @staticmethod
    def save_preferences(preferences_dict):
        """Serialize preferences or related tasks as JSON."""
        return json.dumps(preferences_dict)

    @staticmethod
    def load_preferences(preferences_json):
        """Deserialize JSON to a Python dictionary."""
        return json.loads(preferences_json)


class User(BaseModel):
    """Represents a user in the system."""

    def __init__(self, name, age, preferences, job_designation):
        self.name = name
        self.age = age
        self.preferences = preferences  # Stored as a dictionary
        self.job_designation = job_designation

    def save(self):
        """Insert a new user into the database."""
        conn = self.connect()
        cursor = conn.cursor()
        preferences_json = self.save_preferences(self.preferences)
        cursor.execute('''
        INSERT INTO users (name, age, preferences, job_designation)
        VALUES (?, ?, ?, ?);
        ''', (self.name, self.age, preferences_json, self.job_designation))
        conn.commit()
        conn.close()


class Task(BaseModel):
    """Represents a task in the system."""

    def __init__(self, user_id, title, description, due_date_time, priority, topic_area, event_relation=None):
        self.user_id = user_id
        self.title = title
        self.description = description
        self.due_date_time = due_date_time  # ISO format
        self.priority = priority
        self.topic_area = topic_area
        self.event_relation = event_relation

    def save(self):
        """Insert a new task into the database."""
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute('''
        INSERT INTO tasks (user_id, title, description, due_date_time, priority, topic_area, event_relation)
        VALUES (?, ?, ?, ?, ?, ?, ?);
        ''', (self.user_id, self.title, self.description, self.due_date_time,
              self.priority, self.topic_area, self.event_relation))
        conn.commit()
        conn.close()


class Event(BaseModel):
    """Represents an event in the system."""

    def __init__(self, user_id, title, description, duration, related_tasks, related_to_goal=None):
        self.user_id = user_id
        self.title = title
        self.description = description
        self.duration = duration  # Duration in minutes
        self.related_tasks = related_tasks  # List of task IDs
        self.related_to_goal = related_to_goal

    def save(self):
        """Insert a new event into the database."""
        conn = self.connect()
        cursor = conn.cursor()
        related_tasks_json = self.save_preferences(self.related_tasks)
        cursor.execute('''
        INSERT INTO events (user_id, title, description, duration, related_tasks, related_to_goal)
        VALUES (?, ?, ?, ?, ?, ?);
        ''', (self.user_id, self.title, self.description, self.duration,
              related_tasks_json, self.related_to_goal))
        conn.commit()
        conn.close()


class Goal(BaseModel):
    """Represents a goal in the system."""

    def __init__(self, user_id, title, description, priority, related_goals):
        self.user_id = user_id
        self.title = title
        self.description = description
        self.priority = priority
        self.related_goals = related_goals  # List of sub-goal IDs

    def save(self):
        """Insert a new goal into the database."""
        conn = self.connect()
        cursor = conn.cursor()
        related_goals_json = self.save_preferences(self.related_goals)
        cursor.execute('''
        INSERT INTO goals (user_id, title, description, priority, related_goals)
        VALUES (?, ?, ?, ?, ?);
        ''', (self.user_id, self.title, self.description, self.priority, related_goals_json))
        conn.commit()
        conn.close()


# Database Initialization Function
def initialize_db():
    ensure_db_folder_exists()  # Ensure the folder exists

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    # User Table Schema
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER,
        preferences TEXT,  -- Stored as JSON
        job_designation TEXT
    );
    ''')

    # Task Table Schema
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        title TEXT NOT NULL,
        description TEXT,
        due_date_time TEXT,
        priority TEXT,
        topic_area TEXT,
        event_relation INTEGER,
        FOREIGN KEY (user_id) REFERENCES users(id),
        FOREIGN KEY (event_relation) REFERENCES events(id)
    );
    ''')

    # Event Table Schema
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS events (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        title TEXT NOT NULL,
        description TEXT,
        duration INTEGER,
        related_tasks TEXT,  -- JSON array of task IDs
        related_to_goal INTEGER,
        FOREIGN KEY (user_id) REFERENCES users(id),
        FOREIGN KEY (related_to_goal) REFERENCES goals(id)
    );
    ''')

    # Goal Table Schema
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS goals (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        title TEXT NOT NULL,
        description TEXT,
        priority TEXT,
        related_goals TEXT,
        FOREIGN KEY (user_id) REFERENCES users(id)
    );
    ''')

    conn.commit()
    conn.close()


# Example Usage
if __name__ == "__main__":
    initialize_db()

    # Create a new user
    user = User("Alice Smith", 25, {"topics": {"art": 5, "coding": 4}}, "Graphic Designer")
    user.save()

    # Add a task for the user
    task = Task(1, "Design Mockups", "Create design mockups for the project", datetime.now().isoformat(), "High", "Design")
    task.save()

    # Add an event related to the task
    event = Event(1, "Client Meeting", "Discuss mockups with the client", 60, [1])
    event.save()

    # Add a goal related to the user
    goal = Goal(1, "Career Growth", "Improve design skills", "High", [])
    goal.save()
