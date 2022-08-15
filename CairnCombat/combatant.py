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
    
    def subtract_hp(self, damage_taken=0):
        """Subtract hp if combatant is damaged"""
        if damage_taken < self.hp:
            self.hp -= damage_taken
            print(f"{self.name} has taken {damage_taken} damage.")
            print(f"{self.name} has {self.hp} HP left.")
            print(f"{self.name} has {self.strength} STR left.")
        elif damage_taken == self.hp:
            # Get a scar!
            print(f"{self.name} gets a scar!")
            print(f"{self.name} has {self.hp} HP left.")
            print(f"{self.name} has {self.strength} STR left.")
            pass
        else:
            str_damage = damage_taken - self.hp
            self.hp = 0
            if str_damage >= self.strength:
                self.strength = 0
                print(f"{self.name} is dead.")
                print(f"{self.name} has {self.hp} HP left.")
                print(f"{self.name} has {self.strength} STR left.")
            else:
                self.strength -= str_damage
                # Roll for critical damage
                print(f"{self.name} needs to roll for critical damage.")
                print(f"{self.name} has {self.hp} HP left.")
                print(f"{self.name} has {self.strength} STR left.")