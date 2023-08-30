class npc:
    def __init__(self, firstname = '', lastname = '', race = ''):
        self.first_name = firstname
        self.last_name = lastname
        self.race = race
    
    def return_first_name(self):
        return self.first_name
    
    def return_last_name(self):
        return self.last_name
    
    def return_race(self):
        return self.race