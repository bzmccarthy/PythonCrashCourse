from die import Die

class Combatant:
    """A class representing a single friendly or enemy combatant"""
    
    def __init__(self, hp=6, ac=0, hit_die=6,
                strength=10, dexterity=10, willpower=10,
                name='DefaultName'):
        """Set initial values for combatant"""
        self.name = name
        self.attack_die = Die(num_sides=hit_die)
        self.hp = hp
        self.ac = ac
        self.strength = strength
        self.dexterity = dexterity
        self.willpower = willpower
        
    def roll_attack(self):
        """Roll attack die and return the numbers"""
        attack_roll = self.attack_die.roll()
        print(f"{self.name} rolled a {attack_roll}.")
        return attack_roll
    
    def take_damage(self, enemy_attack_roll=0):
        """See if and how much damage is taken"""
        
        actual_damage = enemy_attack_roll - self.ac
        
        if actual_damage <= 0:
            print(f"Enemy only rolled {enemy_attack_roll}.")
            print(f"Lower than {self.name}'s AC of {self.ac}.")
            print("No damage taken.")
        
        else:
            self.subtract_hp(actual_damage)
    
    def subtract_hp(self, damage_taken=0):
        """Subtract hp if combatant is damaged"""
        if damage_taken < self.hp:
            self.hp -= damage_taken
            print(f"{self.name} has taken {damage_taken} damage.")
            self.print_stats()

        elif damage_taken == self.hp:
            # Get a scar!
            print(f"{self.name} gets a scar!")
            self.hp -= damage_taken
            self.print_stats()
            
        else:            
            str_damage = damage_taken - self.hp
            print(f"{self.name} takes {self.hp} HP damage.")
            print(f"{self.name} takes {str_damage} STR damage.")
            self.hp = 0
            
            if str_damage >= self.strength:
                self.strength = 0
                print(f"{self.name} is dead.")
                self.print_stats()
                
            else:
                self.strength -= str_damage
                self.print_stats()
                # Roll for critical damage
                print(f"{self.name} needs to roll for critical damage.")
                self.roll_critical()
                
    def print_stats(self):
        """Print the combatants stats"""
        print(f"{self.name} has {self.hp} HP left.")
        print(f"{self.name} has {self.strength} STR left.")
        
    def attack(self, enemy):
        """Attack an enemy"""
        attack_roll = self.attack_die.roll()
        print(f"{self.name} attacks {enemy.name}, rolls a {attack_roll}.")
        enemy.take_damage(attack_roll)
        
    def roll_critical(self):
        """Roll for critical damage"""
        d20_roll = Die(num_sides=20).roll()
        
        if d20_roll <= self.strength:
            print(f"{self.name} has rolled a {d20_roll} and saved!")
        else:
            print(f"{self.name} has rolled a {d20_roll}, and is taken out.")
        