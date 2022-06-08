import random
import re

# It creates a new board, assigns values to the board, and creates a set of dug tiles
class Board:
    def __init__(self, dim_size, num_bombs):
        """
        It creates a new board, assigns values to the board, and creates a set of dug tiles
        
        :param dim_size: the size of the board (e.g. if dim_size = 3, the board will be 3x3)
        :param num_bombs: the number of bombs on the board
        """
        self.dim_size = dim_size
        self.num_bombs = num_bombs
        self.board = self.make_new_board()
        self.assign_values_to_board()
        self.dug = set()

    def make_new_board(self):
        """
        It creates a new board with the specified number of bombs
        :return: A list of lists.
        """
        board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]

        bombs_planted = 0
        while bombs_planted < self.num_bombs:
            loc = random.randint(0, self.dim_size**2 - 1)
            row = loc // self.dim_size
            col = loc % self.dim_size

            if board[row][col] == '*':
                continue
            
            board[row][col] = '*'
            bombs_planted += 1
        
        return board
    
    def assign_values_to_board(self):
        """
        It loops through the board and assigns the number of neighboring bombs to each cell.
        """
        for r in range(self.dim_size):
            for c in range(self.dim_size):
                if self.board[r][c] == '*':
                    continue
                self.board[r][c] = self.get_num_neighboring_bombs(r, c)

    def get_num_neighboring_bombs(self, row, col):
        """
        For each cell in the board, if the cell is not a bomb, then we check the neighboring cells to see
        if they are bombs. If they are, we increment the number of neighboring bombs by 1
        
        :param row: the row of the cell we're looking at
        :param col: the column of the cell
        :return: The number of neighboring bombs.
        """
        num_neighboring_bombs = 0
        for r in range(max(0, row -1), min(self.dim_size-1, row+1)+1):
            for c in range(max(0, col-1), min(self.dim_size-1, col+1)+1):
                if r == row and c == col:
                    continue
                if self.board[r][c] == '*':
                    num_neighboring_bombs += 1

        return num_neighboring_bombs 
    
    def dig(self, row, col):
        """
        If the cell is a mine, return False. If the cell is a number, return True. If the cell is a
        blank, recursively dig all adjacent cells
        
        :param row: the row of the cell to dig
        :param col: The column of the cell to dig
        :return: True or False
        """
        self.dug.add((row, col))

        if self.board[row][col] == '*':
            return False
        elif self.board[row][col] > 0:
            return True
        
        for r in range(max(0, row-1), min(self.dim_size-1, row+1)+1):
            for c in range(max(0, col-1), min(self.dim_size-1, col+1)+1):
                if (r,c) in self.dug:
                    continue
                self.dig(r,c)
        
        return True
    
    def __str__(self):
        """
        It creates a new board that is the same size as the original board, and then fills it with the
        values of the original board, but only if the cell has been dug. 
        
        If the cell has not been dug, it fills it with a space. 
        
        Then, it creates a string representation of the board, and returns it. 
        
        The string representation is a bit complicated, but it's just a way to make the board look nice.
        
        
        The first thing it does is find the longest string in each column. 
        
        Then, it creates a row of indices at the top of the board. 
        
        Then, it creates a row of dashes that is the same length as the board. 
        
        Then, it creates a row for each row in the board. 
        
        For each row, it creates a string representation of each cell, and then joins them together with
        a pipe. 
        
        Then
        :return: The board with the numbers that have been dug up.
        """
        visible_board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]
        for row in range(self.dim_size):
            for col in range(self.dim_size):
                if (row, col) in self.dug:
                    visible_board[row][col] = str(self.board[row][col])
                else:
                    visible_board[row][col] = ' '
                
                string_rep = ''
        
        widths = []
        for idx in range(self.dim_size):
            columns = map(lambda x: x[idx], visible_board)
            widths.append(
                len(
                    max(columns, key = len)
                )
            )
        
        indices = [i for i in range(self.dim_size)]
        indices_row = '   '
        cells = []
        for idx, col in enumerate(indices):
            format = '%-' + str(widths[idx]) + "s"
            cells.append(format % (col))
        indices_row += '  '.join(cells)
        indices_row += '  \n'

        for i in range(len(visible_board)):
            row = visible_board[i]
            string_rep += f'{i} |'
            cells = []
            for idx, col in enumerate(row):
                format = '%-' + str(widths[idx]) + "s"
                cells.append(format % (col))
            string_rep += ' |'.join(cells)
            string_rep += ' |\n'

        str_len = int(len(string_rep) / self.dim_size)
        string_rep = indices_row + '-'*str_len + '\n' + string_rep + '-'*str_len

        return string_rep

def play(dim_size=10, num_bombs=10):
    """
    It creates a board, then loops until the user has dug all the safe squares, printing the board after
    each dig, and asking the user for the next dig location
    
    :param dim_size: the size of the board. The board will be a square, so this is the number of rows
    and columns, defaults to 10 (optional)
    :param num_bombs: The number of bombs on the board, defaults to 10 (optional)
    """
    board = Board(dim_size, num_bombs)
    safe = True
    while len(board.dug) < board.dim_size ** 2 - num_bombs:
        print(board)
        user_input = re.split(',(\\s)*', input("Where would you like to dig? Input as row,col:"))
        row, col = int(user_input[0]), int(user_input[-1])
        if row < 0 or row >= board.dim_size or col < 0 or col >= dim_size:
            print("Invalid location. Try again.")
            continue
        
        safe = board.dig(row, col)
        if not safe:
            break

    # It's checking to see if the user has dug all the safe squares. If they have, it prints a
    # congratulations message. If they haven't, it prints a game over message, and then it digs up all
    # the
    # squares on the board, and prints the board.
    if safe:
        print("Congratulations!!! You are winner!")
    else:
        print("Sorry Game Over:(")
        board.dug = [(r,c) for r in range(board.dim_size) for c in range(board.dim_size)]
        print(board)

# It's a way to make sure that the code in the `play()` function only runs if the file is run
# directly.
if __name__ == "__main__":
    play()