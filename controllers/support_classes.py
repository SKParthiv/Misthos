class Avatar:
    def __init__(self, head, body, legs, feet, head_color, body_color, legs_color, feet_color, head_dress, body_dress, legs_dress, feet_dress):
        self.head = head
        self.body = body
        self.legs = legs
        self.feet = feet
        self.head_color = head_color
        self.body_color = body_color
        self.legs_color = legs_color
        self.feet_color = feet_color
        self.head_dress = head_dress
        self.body_dress = body_dress
        self.legs_dress = legs_dress
        self.feet_dress = feet_dress

    def edit_head(self, new_head, new_color=None, new_dress=None):
        self.head = new_head
        if new_color:
            self.head_color = new_color
        if new_dress:
            self.head_dress = new_dress

    def edit_body(self, new_body, new_color=None, new_dress=None):
        self.body = new_body
        if new_color:
            self.body_color = new_color
        if new_dress:
            self.body_dress = new_dress

    def edit_legs(self, new_legs, new_color=None, new_dress=None):
        self.legs = new_legs
        if new_color:
            self.legs_color = new_color
        if new_dress:
            self.legs_dress = new_dress

    def edit_feet(self, new_feet, new_color=None, new_dress=None):
        self.feet = new_feet
        if new_color:
            self.feet_color = new_color
        if new_dress:
            self.feet_dress = new_dress

class Skill:
    def __init__(self, name, level, atk_dmg, defense, skill_type, effects, poison_level=0, buff_level=0):
        self.name = name
        self.level = level
        self.atk_dmg = atk_dmg
        self.defense = defense
        self.skill_type = skill_type
        self.effects = effects
        self.poison_level = poison_level
        self.buff_level = buff_level

    def upgrade(self):
        self.level += 1
        self.atk_dmg += 5  # Example increment
        self.defense += 2  # Example increment
        self.poison_level += 1  # Example increment
        self.buff_level += 1  # Example increment

    def add_effect(self, effect):
        self.effects.append(effect)

class Quest:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        # difficulty = GPT gen
        self.difficulty = difficulty

class Reward:
    def __init__(self, quest):
        self.quest = quest
        self.calculate_rewards()

    def calculate_rewards(self):
        # GPT code
        pass

class Swordsman:
    def __init__(self):
        self.skills = {
            1: "Slash",
            2: "Stab",
            3: "Heavy Slash",
            4: "Double Slash",
            5: "Power Stab",
            6: "Whirlwind",
            7: "Blade Dance",
            8: "Earthquake Slash",
            9: "Lightning Stab",
            10: "Ultimate Slash"
        }

class Spearman:
    def __init__(self):
        self.skills = {
            1: "Thrust",
            2: "Pierce",
            3: "Sweep",
            4: "Double Thrust",
            5: "Power Pierce",
            6: "Whirlwind Spear",
            7: "Spear Dance",
            8: "Earthquake Thrust",
            9: "Lightning Pierce",
            10: "Ultimate Thrust"
        }

class Magician:
    def __init__(self):
        self.skills = {
            1: "Fireball",
            2: "Ice Shard",
            3: "Lightning Bolt",
            4: "Flame Wave",
            5: "Frost Nova",
            6: "Thunderstorm",
            7: "Meteor Shower",
            8: "Blizzard",
            9: "Chain Lightning",
            10: "Ultimate Spell"
        }

class Necromancer:
    def __init__(self):
        self.skills = {
            1: "Raise Skeleton",
            2: "Dark Pact",
            3: "Soul Drain",
            4: "Raise Zombie",
            5: "Dark Ritual",
            6: "Life Drain",
            7: "Raise Wraith",
            8: "Dark Explosion",
            9: "Soul Harvest",
            10: "Ultimate Necromancy"
        }

class Assassin:
    def __init__(self):
        self.skills = {
            1: "Backstab",
            2: "Poison Dagger",
            3: "Shadow Step",
            4: "Double Backstab",
            5: "Venom Strike",
            6: "Shadow Dance",
            7: "Silent Kill",
            8: "Shadow Assault",
            9: "Poison Cloud",
            10: "Ultimate Assassination"
        }

class Healer:
    def __init__(self):
        self.skills = {
            1: "Heal",
            2: "Cure",
            3: "Revive",
            4: "Greater Heal",
            5: "Purify",
            6: "Mass Revive",
            7: "Divine Shield",
            8: "Holy Light",
            9: "Blessing",
            10: "Ultimate Healing"
        }
