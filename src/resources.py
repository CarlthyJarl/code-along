# imports
# global variabels
# classes
class Character:

    def __init__(self, name, health, damage, armor):
        self.name = name
        self.health = health
        self.damage = damage 
        self.armor = armor

    def __str__(self):
        return F"Name: {self.name}\nHealth: {self.health}\nDamage: {self.damage}\nArmor: {self.armor}"

    def take_damage(self, dmg):
        actual_damage = dmg - self.armor
        if actual_damage < 0: actual_damage = 0 
        if (self.health - actual_damage) < 0:
            self.health = 0
        else:
            self.health -= actual_damage

    def attack(self):
        return self.damage

    def get_health(self):
        return self.health

    def get_name(self):
        return self.name

    def get_all_attributes(self):
        return self.name, self.health, self.damage, self.armor

    

class Goblin:

    def __init__(self, id):
        self.id = id
        self.health = 10
        self.damage = 3
        self.armor = 2

    def __str__(self):
        return F"Name: {self.id}\nHealth: {self.health}\nDamage: {self.damage}\nArmor: {self.armor}"

    def take_damage(self, dmg):
        actual_damage = dmg - self.armor
        if actual_damage < 0: actual_damage = 0 
        if (self.health - actual_damage) < 0:
            self.health = 0
        else:
            self.health -= actual_damage
    
    
    def attack(self):
        return self.damage

    def get_health(self):
        return self.health

    def get_name(self):
        return f"Goblin #{self.id}"

# functions
def hi():
    print("hi")



def save_character(character: Character):
    """
    Tar in karaktär, bryter ner dess attribut och sparar ner på fil
    
    Args:
        character (Character): Det objekt som ska sparas ner påå fil
    """
    name, health, damage, armor = character.get_all_attributes()
    with open("character_file.txt", "w", encoding="utf8") as f:
        save_string = f"{name}/{health}/{damage}/{armor}\n"
        f.write(save_string)
        print(F"{name} has been successfully saved. ")


def load_characters():

    with open("character_file.txt", "r", encoding="utf8") as f:
        characters = []
        for line in f.readlines():
            attributes = line.split("/")
            this_char = Character(attributes[0],
                                  int(attributes[1]),
                                  int(attributes[2]),
                                  int(attributes[3]))
            characters.append(this_char)
        print("Characters has been loaded from file.")
        return characters


# main code




