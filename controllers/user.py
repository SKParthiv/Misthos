class Player:
    def __init__(self, user_name, avatar, intelligence, strength, agility, stamina, health, skills, level=1, exp=0):
        self.user_name = user_name
        self.avatar = avatar
        self.intelligence = intelligence
        self.strength = strength
        self.agility = agility
        self.stamina = stamina
        self.health = health
        self.skills = skills  # Dictionary of Skill objects
        self.level = level
        self.exp = exp

    def update_stat(self, stat, value):
        if hasattr(self, stat):
            setattr(self, stat, value)

    def add_skill(self, skill_name, skill):
        self.skills[skill_name] = skill

    def remove_skill(self, skill_name):
        if skill_name in self.skills:
            del self.skills[skill_name]

    def gain_exp(self, amount):
        self.exp += amount
        if self.exp >= self.level * 100:  # Example level-up condition
            self.level_up()

    def level_up(self):
        self.level += 1
        self.exp = 0
        # Add logic to increase stats or unlock new skills

class User:
    def __init__(self, name, edu_lvl, age, family, player):
        self.name = name
        self.edu_lvl = edu_lvl
        self.age = age
        self.family = family
        self.player = player

    def update_info(self, name=None, edu_lvl=None, age=None, family=None):
        if name:
            self.name = name
        if edu_lvl:
            self.edu_lvl = edu_lvl
        if age:
            self.age = age
        if family:
            self.family = family

    def update_preferences(self, new_preferences):
        """Update user preferences."""
        self.player.update_preferences(new_preferences)

    def update_job_designation(self, new_job_designation):
        """Update user job designation."""
        self.player.update_job_designation(new_job_designation)

    def link_google_account(self, google_user_info):
        """Link Google account to the user."""
        self.google_user_info = google_user_info
        self.name = google_user_info['name']
        self.email = google_user_info['email']
        self.avatar_url = google_user_info['picture']
