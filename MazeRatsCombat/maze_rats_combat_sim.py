from random import randint

class Combatant():
    """A class representing either a PC or enemy NPC"""
    
    def __init__(self, attack_bonus=0,
                 strength = 1,
                 dexterity = 1,
                 willpower = 1,
                 armor = 6,
                 health = 4,
                 team = 'Player'):
        """Initialize the starting attributes for a combatant"""
        
        self.attack_bonus = attack_bonus
        self.strength = strength
        self.dexterity = dexterity
        self.willpower = willpower
        self.armor = armor
        self.health = health
        self.team = team
        
    def print_info(self):
        """Print info on the combatant"""
        
        print(f"This combatant has:\n\nAttack Bonus: {self.attack_bonus}\n\
Health: {self.health}\n\
Armor: {self.armor}\n\
Strength: {self.strength}\n\
Dexterity: {self.dexterity}\n\
Willpower: {self.willpower}\n\
Team: {self.team}")

player1 = Combatant()
player2 = Combatant()
player3 = Combatant()
player4 = Combatant()

player_roster = [player1, player2, player3, player4]

monster1 = Combatant(team = 'Monster')
monster2 = Combatant(team = 'Monster')
monster3 = Combatant(team = 'Monster')
monster4 = Combatant(team = 'Monster')

monster_roster = [monster1, monster2, monster3, monster4]



die_total = randint(1,6) + randint(1,6)










        