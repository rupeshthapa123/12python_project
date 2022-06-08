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

class GeniusComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
    
    def get_move(self, game):
        if len(game.available_moves()) == 9:
            square = random.choice(game.available_moves())
        else:
            square = self.minimax(game, self.letter)['position']
        return square
    
    def minimax(self, state, player):
        max_player = self.letter
        other_player = 'O' if player == 'X' else 'X'

        if state.current_winner == other_player:
            return {'position':None,
                    'score': 1 *(state.num_empty_squares() + 1) if other_player == max_player else - 1 *(
                        state.num_empty_squares() + 1)
                    }
        elif not state.empty_squares():
            return {'position':None, 'score': 0}
        
        if player == max_player:
            best = {'position': None, 'score': -math.inf}
        else:
            best = {'position': None, 'score': math.inf}
        
        for possible_move in state.available_moves():
            state.make_move(possible_move, player)
            sim_score = self.minimax(state, other_player)
            state.board[possible_move] = ' '
            state.current_winner = None
            sim_score['position'] = possible_move

            if player == max_player:
                if sim_score['score'] > best['score']:
                    best = sim_score
            else:
                if sim_score['score'] < best['score']:
                    best = sim_score
        
        return best
