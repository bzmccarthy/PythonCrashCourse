"""A game of life. Modeled after the game
Real Lives."""

def main():

    """Main function to initiate and run game"""

    print("Welcome to ToBe. Enjoy your stay.")
    print("\n")

    player = Player()
    game = GameState()

    while not game.game_over:

        print("You are " + player.return_age() + " years old.")

        game.play_turn(player)

        if player.age == 5:

            game.game_over = True
        
        input("Press ENTER to continue: ")
        print()

    print("You have died! You were " +
          player.return_age() + " years old.")

class GameState:
    
    """Class to store game variables, run life,
    and end game"""

    def __init__(self):

        self.game_over = False

    def play_turn(self, player):

        player.add_year()

class Player:

    """Player class to store all the information on the
    player character in the game"""

    def __init__(self):

        self.age = 0
        self.country = "USA"
        self.sex = "Male"
        self.race = "White"

    def add_year(self):

        self.age += 1

    def return_age(self):

        return(str(self.age))

if __name__ == "__main__":   
    main()