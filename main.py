"""
Allows the viewing and creation of Dungeon and Dragons NPCs and their relevant statblocks (Strength, Constitution, Intelligence, Wisdom, Charisma).

User can organize NPCs by race, class, etc. They can also modify existing statblocks and update them.

Users can also make notes or mark NPCs with certain conditions or statuses.

Can read from json files.
"""
import PyQt5
import dnd_npcs

if __name__ == "__main__":
    npc_one = dnd_npcs.npc('John', 'Smith', 'Human')
    npc_one_first_name = npc_one.return_first_name()
    npc_one_last_name = npc_one.return_last_name()
    npc_one_race = npc_one.return_race()
    print(f"First npc is: {npc_one_first_name + ' ' + npc_one_last_name} who is a {npc_one_race}")