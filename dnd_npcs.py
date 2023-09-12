"""
Simple NPCs have names, languages, race, and statuses

Detailed NPCs have names, base stats, race, languages, ac, speed, and statuses

Story NPCs have names, base stats, race, languages, ac, speed, HP, skills, attacks, spells, and statuses
"""
class npc:
    def __init__(self, firstname = '', lastname = '', race = '', status = ''):
        self.first_name = firstname
        self.last_name = lastname
        self.race = race
        self.status = status
    
    def get_first_name(self):
        return self.first_name
    
    def get_last_name(self):
        return self.last_name
    
    def get_race(self):
        return self.race
    


class detailed_npc(npc):
    def __init__(self, firstname = '', lastname = '', race = '', languages = 'Common', ac = 10, speed = 30, status = ''):
        super().__init__(firstname, lastname, race, status)
        self.languages = languages
        self.ac = ac
        self.speed = speed


"""
Update to have skills, attacks, and spells later
"""
class story_npc(detailed_npc):
    def __init__(self, firstname = '', lastname = '', race = '', languages = 'Common', ac = 10, speed = 30, hp = 20, current_hp = 20, status = ''):
        super().__init__(firstname, lastname, race, languages, ac, speed, status)
        self.hp = hp
        self.current_hp = current_hp

    def get_current_HP(self):
        return self.current_HP

    def change_HP(self, amount):
        self.HP = self.hp + amount


if __name__ == "__main__":
    bob = npc("Bob", "Smith", "Human")
    print(bob.get_race())
    # print(help(npc))

    alice = story_npc("Alice", "Smith", "Human", "Common", 13, 30, 25)
    print(alice.ac)