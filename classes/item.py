import sqlite3

class Avatar:
    def __init__(self, image_path):
        self.image_path = image_path

class Item:
    def __init__(self, name, job_class_compatibility, atk_buff_percentage=0, def_buff_percentage=0, poison_factor=0, min_lvl=1, base_strength=0, base_agility=0, base_vitality=0, base_intelligence=0, base_stamina=0):
        self.name = name
        self.job_class_compatibility = job_class_compatibility
        self.atk_buff_percentage = atk_buff_percentage
        self.def_buff_percentage = def_buff_percentage
        self.poison_factor = poison_factor
        self.min_lvl = min_lvl
        self.base_strength = base_strength
        self.base_agility = base_agility
        self.base_vitality = base_vitality
        self.base_intelligence = base_intelligence
        self.base_stamina = base_stamina

    def save(self):
        conn = sqlite3.connect('misthos.db')
        c = conn.cursor()
        c.execute('''INSERT INTO items (name, job_class_compatibility, atk_buff_percentage, def_buff_percentage, poison_factor, min_lvl, base_strength, base_agility, base_vitality, base_intelligence, base_stamina)
                     VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                  (self.name, self.job_class_compatibility, self.atk_buff_percentage, self.def_buff_percentage, self.poison_factor, self.min_lvl, self.base_strength, self.base_agility, self.base_vitality, self.base_intelligence, self.base_stamina))
        conn.commit()
        conn.close()
