from tictactoe.player import GeniusComputerPlayer, HumanPlayer, RandomComputerPlayer
import time
# It's a class that represents a tic tac toe board
class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.current_winner = None
    
    def print_board(self):
        """
        It takes the board, and prints it out in a 3x3 grid
        """
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')
    
    @staticmethod
    def print_board_nums():
        """
        It creates a list of lists, where each list is a row of the board, and each element of the list
        is a number from 0 to 8
        """
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')
    
    def available_moves(self):
        """
        It returns a list of all the indices of the board that are empty.
        :return: A list of the available moves.
        """
        return [i for i, spot in enumerate(self.board) if spot == ' ']
    
    def empty_squares(self):
        """
        It returns True if there is an empty space on the board
        :return: The return statement is returning the value of the expression.
        """
        return ' ' in self.board
    
    def num_empty_squares(self):
        """
        It counts the number of empty squares on the board
        :return: The number of empty squares on the board.
        """
        return self.board.count(' ')
    
    def make_move(self, square, letter):
        """
        If the square is empty, make the move and check if it's a winning move
        :param square: The square number (0-8) where you want to make a move
        :param letter: The letter that the player wants to place on the board
        :return: True if the move is valid, and False if it is not.
        """
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False
    
    def winner(self, square, letter):
        """
        If all the spots in the row are the same as the letter, return True
        :param square: the square that was just played
        :param letter: the letter that is being checked for a win
        :return: True if all the spots in the row are the same as the letter.
        """
        row_ind = square // 3
        row = self.board[row_ind*3 : (row_ind + 1) * 3]
        if all([spot == letter for spot in row]):
            return True 
        # This is checking for a column win. The column index is the remainder of the square divided
        # by 3.
        # The column is a list of the 3 spots in the column. If all of the spots in the column
        # are the same,
        # then there is a column win.
        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True
        # This is checking for a diagonal win. If the square is in the middle, then it is on both
        # diagonals. If the square is on the top left or bottom right, then it is only on the top left
        # to bottom right diagonal. If the square is on the top right or bottom left, then it is only
        # on the top right to bottom left diagonal.
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            if all([spot == letter for spot in diagonal2]):
                return True
        return False       

def play(game, x_player, o_player, print_game=True):
    """
    It plays a game of tic-tac-toe between two players, and returns the winner
    :param game: the game object
    :param x_player: The player that will be playing as X
    :param o_player: The player that plays the 'O' pieces
    :param print_game: If True, the game will be printed to the console, defaults to True (optional)
    :return: The letter of the winner.
    """
    if print_game:
        game.print_board_nums()
    letter = 'X'
    # Checking if the game is empty. If it is, it will check if the letter is O. If it is, it will get
    # the move from the O player. If it is not, it will get the move from the X player. If the game is
    # not empty, it will make the move. If the move is made, it will print the letter and the square.
    # It will then print the board. If the game is not empty, it will print the letter and the winner.
    # If the game is empty, it will return the letter.
    while game.empty_squares():
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)
        if game.make_move(square, letter):
            if print_game:
                print(letter + f' makes a move to square {square}')
                game.print_board()
                print('')
            if game.current_winner:
                if print_game:
                    print(letter + ' wins!')
                return letter
            letter = 'O' if letter == 'X' else 'X'
        # Making the game wait 0.8 seconds before the next move is made.
        time.sleep(0.8)
        # Printing out the message "It's a tie!" if the game is a tie.
    if print_game: 
        print('It\'s a tie!')

# Creating a game with a human player and a random computer player.
if __name__ == '__main__':
    x_wins = 0
    o_wins = 0
    ties = 0
    for _ in range(50):
        x_player = RandomComputerPlayer('X')
        o_player = GeniusComputerPlayer('O')
        t = TicTacToe()
        result = play(t, x_player, o_player, print_game=False)
        if result == 'X':
            x_wins += 1
        elif result == 'O':
            o_wins += 1
        else:
            ties += 1
        
    print(f'After 50 iterations, we see {x_wins} X wins, {o_wins} O wins, {ties} ties')
