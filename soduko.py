from pprint import pprint

def find_next_empty(puzzle):
    """
    > Find the next empty cell in the puzzle
    
    :param puzzle: The puzzle to solve
    :return: The row and column of the next empty cell.
    """
    for r in range(9):
        for c in range(9):
            if puzzle[r][c] == -1:
                return r, c    
    return None, None

def is_valid(puzzle, guess, row, col):
    """
    If the guess is not in the row or column or 3x3 box, then it is valid.
    
    :param puzzle: the puzzle to solve
    :param guess: the number we're trying to place in the puzzle
    :param row: the row of the cell we're trying to fill
    :param col: the column of the cell we're trying to fill
    :return: A list of lists.
    """
    row_vals = puzzle[row]
    if guess in row_vals:
        return False
    # col_vals = []
    # for i in range(9):
    #     col_vals.append(puzzle[i][col])
    col_vals = [puzzle[i][col] for i in range(9)]
    if guess in col_vals:
        return False
    row_start = (row // 3) * 3
    col_start = (col // 3) * 3
    for r in range(row_start, row_start + 3):
        for c in range(col_start, col_start + 3):
            if puzzle[r][c] == guess:
                return False
    return True

def solve_sudoku(puzzle):
    """
    If there are no empty cells, return True. Otherwise, try each possible guess in the current cell,
    and if it's valid, recursively solve the puzzle with that guess. If the recursive call returns True,
    return True. Otherwise, reset the current cell to empty and try the next guess. If all guesses fail,
    return False
    
    :param puzzle: The sudoku puzzle to solve
    :return: a boolean value.
    """
    row, col = find_next_empty(puzzle)
    if row is None:
        return True
    for guess in range(1, 10):
        if is_valid(puzzle, guess, row, col):
            puzzle[row][col] = guess
            if solve_sudoku(puzzle):
                return True
        puzzle[row][col] = -1
    return False

# This is a special variable in Python that is set when the module is run as the main program.
if __name__ == '__main__':
    example_board = [
        [3, 9, -1, -1, 5, -1, -1, -1, -1],
        [-1, -1, -1,  2, -1, -1, -1, -1, 5],
        [-1, -1, -1, 7, 1, 9, -1, 8, -1],

        [-1, 5, -1, -1, 6, 8, -1, -1, -1],
        [2, -1, 6,  -1, -1, 3, -1, -1, -1],
        [-1, -1, -1, -1, -1,-1, -1, -1, 4],

        [5, -1, -1, -1, -1, -1, -1, -1, -1],
        [6, 7, -1, 1, -1, -1, -1, 4, -1],
        [1, -1, 9, -1, -1, -1, 2, -1, -1]
    ]
    print(solve_sudoku(example_board))
    pprint(example_board)


