import os
os.chdir('C:/Users/bzmcc/Documents/PythonCrashCourse/CairnCombat')

from combatant import Combatant
from die import Die


#PCs
penelope = Combatant(hp=6, ac=2, hit_die=[8],
                strength=8, dexterity=11, willpower=10,
                name='Penelope')

bill = Combatant(hp=6, ac=1, hit_die=[6,6],
                strength=8, dexterity=10, willpower=10,
                name='Bill')

abobo = Combatant(hp=6, ac=2, hit_die=[8],
                strength=11, dexterity=14, willpower=13,
                name='Abobo')

mathia = Combatant(hp=6, ac=0, hit_die=[6],
                strength=11, dexterity=13, willpower=13,
                name='Mathia')

# NPCs
alfred = Combatant(hp=4, ac=2, hit_die=[8],
                strength=11, dexterity=8, willpower=18,
                name='Sir Alfred')


pc_list = [penelope, bill, abobo, mathia]
npc_list = [alfred]

def roll_initiative(pc_list):
    """Roll to see who goes first"""
    
    d20 = Die(num_sides=20)
    
    for pc in pc_list:
        d20_roll = d20.roll()
        if d20_roll <= pc.dexterity:
            print(f"{pc.name} rolls a {d20_roll} and goes first.")
        else:
            print(f"{pc.name} rolls a {d20_roll} and misses initiative.")
            
            
            
            
            
            