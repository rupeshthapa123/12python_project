import math
import random

# The Player class is a template for creating player objects
class Player:
    def __init__(self, letter):
        self.letter = letter
    
    def get_move(self, game):
        pass

# The RandomComputerPlayer class inherits from the Player class and overrides the get_move method to
# return a random move from the available moves
class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
    
    def get_move(self, game):
        square = random.choice(game.available_moves())
        return square

# The HumanPlayer class is a subclass of the Player class. It has a constructor that takes a letter as
# an argument and passes it to the superclass constructor. It also has a get_move method that takes a
# game as an argument and returns a valid move
class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
    
    def get_move(self, game):
        """
        It takes in a game object and returns a valid move
        :param game: the game object
        :return: The value of the square that the player has chosen.
        """
        valid_square  = False
        val = None
        while not valid_square:
            square = input(self.letter + '\'s turn. Input move (0-8):')
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print('Invalid square. Try again.')
        return val
