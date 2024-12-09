import sqlite3

class Skill:
    def __init__(self, name, atk_damage=0, cooldown=0, atk_defense=0, defense_duration=0, buff=None, buff_stat=None, poison_effect=None, poison_stat=None, poison_amount=0, min_lvl=1, base_strength=0, base_agility=0, base_vitality=0, base_intelligence=0, base_stamina=0):
        self.name = name
        self.atk_damage = atk_damage
        self.cooldown = cooldown
        self.atk_defense = atk_defense
        self.defense_duration = defense_duration
        self.buff = buff
        self.buff_stat = buff_stat
        self.poison_effect = poison_effect
        self.poison_stat = poison_stat
        self.poison_amount = poison_amount
        self.min_lvl = min_lvl
        self.base_strength = base_strength
        self.base_agility = base_agility
        self.base_vitality = base_vitality
        self.base_intelligence = base_intelligence
        self.base_stamina = base_stamina

class JobClass:
    def __init__(self, name):
        self.name = name
        self.skills = self.get_skills()

    def get_skills(self):
        skills = {
            "Swordsman": {
                1: [Skill("Slash", atk_damage=10, cooldown=5, min_lvl=1, base_strength=5)],
                2: [Skill("Slash", atk_damage=10, cooldown=5, min_lvl=1, base_strength=5), Skill("Block", atk_defense=5, defense_duration=3, min_lvl=2, base_vitality=3)],
                # ... add skills for levels 3 to 10
            },
            "Magician": {
                1: [Skill("Fireball", atk_damage=15, cooldown=7, min_lvl=1, base_intelligence=5)],
                2: [Skill("Fireball", atk_damage=15, cooldown=7, min_lvl=1, base_intelligence=5), Skill("Magic Shield", atk_defense=3, defense_duration=5, min_lvl=2, base_intelligence=3)],
                # ... add skills for levels 3 to 10
            },
            "Spearman": {
                1: [Skill("Thrust", atk_damage=12, cooldown=6, min_lvl=1, base_strength=4)],
                2: [Skill("Thrust", atk_damage=12, cooldown=6, min_lvl=1, base_strength=4), Skill("Parry", atk_defense=4, defense_duration=4, min_lvl=2, base_agility=3)],
                # ... add skills for levels 3 to 10
            },
            "Poisonmaster": {
                1: [Skill("Poison Dart", atk_damage=8, cooldown=5, poison_effect=True, poison_stat="hp", poison_amount=2, min_lvl=1, base_intelligence=4)],
                2: [Skill("Poison Dart", atk_damage=8, cooldown=5, poison_effect=True, poison_stat="hp", poison_amount=2, min_lvl=1, base_intelligence=4), Skill("Venom Shield", atk_defense=2, defense_duration=4, poison_effect=True, poison_stat="atk", poison_amount=1, min_lvl=2, base_intelligence=3)],
                # ... add skills for levels 3 to 10
            },
            "Healer": {
                1: [Skill("Heal", buff=True, buff_stat="hp", cooldown=10, min_lvl=1, base_intelligence=5)],
                2: [Skill("Heal", buff=True, buff_stat="hp", cooldown=10, min_lvl=1, base_intelligence=5), Skill("Protect", atk_defense=5, defense_duration=5, min_lvl=2, base_vitality=3)],
                # ... add skills for levels 3 to 10
            }
        }
        return skills.get(self.name, {})

    def save(self):
        conn = sqlite3.connect('misthos.db')
        c = conn.cursor()
        c.execute('''INSERT INTO job_classes (name)
                     VALUES (?)''', (self.name,))
        conn.commit()
        conn.close()

