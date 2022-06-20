from random import randint, choice

class Combatant():
    """A class representing either a PC or enemy NPC"""
    
    def __init__(self, 
                 name = 'A',
                 attack_bonus=0,
                 dmg_bonus=0,
                 strength = 1,
                 dexterity = 1,
                 willpower = 1,
                 armor = 6,
                 health = 4,
                 team = 'Player'):
        """Initialize the starting attributes for a combatant"""
        
        self.name = name
        self.attack_bonus = attack_bonus
        self.dmg_bonus = dmg_bonus
        self.strength = strength
        self.dexterity = dexterity
        self.willpower = willpower
        self.armor = armor
        self.health = health
        self.team = team
        
    def print_info(self):
        """Print info on the combatant"""
        
        print(f"This combatant has:\n\nName: {self.name}\n\
Attack Bonus: {self.attack_bonus}\n\
Damage Bonus: {self.dmg_bonus}\n\
Health: {self.health}\n\
Armor: {self.armor}\n\
Strength: {self.strength}\n\
Dexterity: {self.dexterity}\n\
Willpower: {self.willpower}\n\
Team: {self.team}\n")
        
def attack_target(attacker, target):
    
    print(f'Attacker: {attacker.name}')
    print(f'Target: {target.name}')
           
    attack_roll = randint(1,6) + randint(1,6)
    
    attack_total = attack_roll + attacker.attack_bonus
    print(f'Attack total: {attack_total}')
        
    if attack_total > target.armor:
        if attack_roll == 12:
            damage = (attack_total - target.armor + attacker.dmg_bonus) * 2
        else:
            damage = attack_total - target.armor + attacker.dmg_bonus
        print(f'Target armor: {target.armor}')
        print(f'Hit! {attacker.name} hit\
 {target.name} for {damage} points of damage!')
        target.health -= damage
        print(f'{target.name} now has {target.health} HP left.')
        
def check_dead(keep_going):
    
    for player in player_roster:
        if player.health < 1:
            print(f'{player.name} has died!')
            player_roster.remove(player)
            keep_going = False
    
    for monster in monster_roster:
        if monster.health < 1:
            print(f'{monster.name} has died!')
            monster_roster.remove(monster)
            
            if len(monster_roster) == 0:
                keep_going = False
    
    return(keep_going)
        
        
def play_round():
                  
    keep_going = True
    
    init_winner = roll_initiative()
    
    if init_winner == 'PCs':
            for player in player_roster:
                if keep_going == False:
                    break
                else:
                    monster = choice(monster_roster)
                    attack_target(player, monster)
                    keep_going = check_dead(keep_going)
            for monster in monster_roster:
                if keep_going == False:
                    break
                else:
                    player = choice(player_roster)
                    attack_target(monster, player)
                    keep_going = check_dead(keep_going)
    else:
            for monster in monster_roster:
                if keep_going == False:
                    break
                else:
                    player = choice(player_roster)
                    attack_target(monster, player)
                    keep_going = check_dead(keep_going)
            for player in player_roster:
                if keep_going == False:
                    break
                else:
                    monster = choice(monster_roster)
                    attack_target(player, monster)
                    keep_going = check_dead(keep_going)
                    
    # print("Game over!")
    
    for player in player_roster:
        print(f'{player.name} HP: {player.health}')
            
    for monster in monster_roster:
        print(f'{monster.name} HP: {monster.health}')
        
    return(keep_going)
               
def roll_initiative():
        
    init_roll = randint(1,6)
        
    if init_roll > 3:
        init_winner = 'PCs'
    else:
        init_winner = 'Monsters'
        
    return(init_winner)









keep_going = True
        
player_roster = [Combatant(name = 'PC_A', 
                           attack_bonus=3,
                           dmg_bonus=0,
                           armor=8,
                           health=6), 
                 Combatant(name = 'PC_B', 
                           attack_bonus=3,
                           dmg_bonus=0,
                           armor=8,
                           health=6), 
                 Combatant(name = 'PC_C', 
                           attack_bonus=3,
                           dmg_bonus=1,
                           armor=7,
                           health=6), 
                 Combatant(name = 'PC_D', 
                           attack_bonus=3,
                           dmg_bonus=0,
                           armor=8,
                           health=6)]

monster_roster = [Combatant(team = 'Monster', 
                            name = 'Mon_1',
                            attack_bonus=0,
                            dmg_bonus=0,
                            armor=7,
                            health=3), 
                  Combatant(team = 'Monster', 
                            name = 'Mon_2',
                            attack_bonus=0,
                            dmg_bonus=0,
                            armor=7,
                            health=3), 
                  Combatant(team = 'Monster', 
                            name = 'Mon_3',
                            attack_bonus=0,
                            dmg_bonus=0,
                            armor=7,
                            health=3), 
                  Combatant(team = 'Monster', 
                            name = 'Mon_4',
                            attack_bonus=0,
                            dmg_bonus=0,
                            armor=7,
                            health=3)]
              
"""monster_roster = [Combatant(team = 'Monster', 
                            name = 'Mon_1',
                            attack_bonus=0,
                            dmg_bonus=0,
                            armor=7,
                            health=4), 
                  Combatant(team = 'Monster', 
                            name = 'Mon_2',
                            attack_bonus=0,
                            dmg_bonus=0,
                            armor=7,
                            health=4)]"""
              
"""monster_roster = [Combatant(team = 'Monster', 
                            name = 'Mon_1',
                            attack_bonus=0,
                            dmg_bonus=0,
                            armor=8,
                            health=8)]"""


round_number = 0

while keep_going == True:
    
    round_number += 1
    print(f'\nThis is round number {round_number}.\n')
    keep_going = play_round()

    
if len(monster_roster) == 0:
    print('PLAYERS WIN THE GAME!!!!')
else:
    print('MONSTERS WIN.  Ohhhh nooooo')
        
print(f'TOTAL COMBAT ROUNDS: {round_number}')
    








        