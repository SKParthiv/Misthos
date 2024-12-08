# Misthos
## Features Organized:

### User Features:

 - Task management (edit, create, etc.)
 - Goal setting and task editing of generated tasks and sub-goals by the GPT
 - Calendar management (same as above)
 - Notifications
 - User details editing (name, age, etc. for GPT customization)

    GPT Features:

        Automated task prioritizing

        Automated task assignment to dates

        Data collection for future automation

        Automated scheduling of a day

    Minimum UI Features and Interface:

        Main Dashboard (sidebar for navigation, widgets like time, date, today's tasks, immediate tasks, etc.)

        Task View

        Calendar View

        Goal Setting View

        Settings

        User Profile

    Game-like Features:

        Rewards for task completion and evidence upload

        GPT-generated rewards based on task difficulty and user skill level

        GPT learning the likes and dislikes of the user for appropriate rewards

        Feedback mechanism through a small chat feature for edits

    Story Mode Features:

        Defeat orcs with progressively increasing difficulty

        Use assets from the assets folder for sprites and images

Final Tech Stack:

    Front-end:

        Tkinter: For building the GUI.

    Back-end and Logic:

        Python: Main programming language.

        APScheduler: For scheduling tasks and reminders.

        T3nsor: For using GPT models.

        Google Calendar API: For calendar management and Google login.

        Pillow: For handling images.

    Database and ORM:

        SQLite: For local data storage.

        SQLAlchemy: For database management and ORM.

    APIs:

        Chat GPT's Free API (using T3nsor): For task prioritization, assignment, and rewards generation.

        Gemini API: Integration for enhanced features (if applicable).

    Package Management:

        pip: For managing Python packages.

    Versioning Software:

        Git: For version control.

        GitHub: For code repository and collaboration.

    IDE:

        Visual Studio Code (VSCode): For development.

    Platform:

        Windows 11: Development and deployment environment.

Implementation Overview:

    Task Management:

        Use Tkinter to create forms for task and goal management.

        Store tasks in SQLite, managed by SQLAlchemy.

        Use APScheduler to schedule task notifications and reminders.

    Calendar Integration:

        Integrate Google Calendar API for calendar management and Google login.

        Display calendar events in the app using Tkinter.

    GPT Features:

        Use T3nsor to leverage Chat GPT's API for task prioritizing, assigning tasks to dates, and generating rewards.

        Collect user details to customize GPT's subtask generation and rewards.

    Story Mode Features:

        Implement a story mode where the player defeats orcs with progressively increasing difficulty.

        Use assets from the assets folder for sprites and images.

    UI Design:

        Design a main dashboard with widgets using Tkinter.

        Create views for tasks, calendar, goal setting, settings, and user profile.

    Packaging:

        Use PyInstaller to package the app into standalone executables.

