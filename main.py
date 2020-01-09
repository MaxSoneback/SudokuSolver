from board_requester import request_board
from math import sqrt


def solve(board):
    unfilled_square = find_empty(board)

    if not unfilled_square:
        return True

    else:
        col, row = unfilled_square

        for val in range(1, len(board)+1):
            if assignment_is_valid(board, val, col, row):
                board[row][col] = val

                if solve(board):
                    return True

                else:
                    board[row][col] = 0


def print_board(board):
    """
    :param board: Spelbräde i form av 2D-list
    :return: None
    """
    for row_index, row in enumerate(board):
        if row_index % int(sqrt(len(board))) == 0 and row_index != 0:
            print(' - ' * round(len(board)*1.1) + ' - ')

        for col_index, elem in enumerate(row):
            if col_index % int(sqrt(len(board))) == 0:
                print(" | ", end="")

            print(f'{elem} ', end="")

            if col_index == len(board) - 1:
                print("| ")


def find_empty(board):
    """
    :param board: Spelbräde i form av 2D-list
    :return: Position av första tomma rutan i formen (col, row)
    """
    for row_index, row in enumerate(board):
        for col_index, elem in enumerate(row):
            if elem == 0:
                return col_index, row_index
    return None


def assignment_is_valid(board, target, col, row):
    """
    :param board: Spelbräde i form av 2D-list
    :param target: Värdet vi försöker tilldela en ruta
    :param col: Kolumnindex
    :param row: Radindex
    :return: boolean
    """

    for i in range(len(board)):
        # Kolla alla element i raden
        if board[row][i] == target and i != col:
            return False

        # Kolla alla element i kolumnen
        if board[i][col] == target and i != row:
            return False

    # Kolla element i boxen
    box_x_coords, box_y_coords = calc_box_limits(board, col, row)

    for x in box_x_coords:
        for y in box_y_coords:
            if x != col and y != row and board[y][x] == target:
                return False
    return True


def calc_box_limits(board, col, row):
    """
        :param col: Kolumnindex
        :param row: Radindex
        :return: Tuple med x respektive y-koordinater (startkolumn,slutkolumn+1),(startrad, slutrad+1)
        """
    box_x = col // int(sqrt(len(board))) # 0 = vänstra boxen, 1 = mellersta, 2 = högra
    box_y = row // int(sqrt(len(board)))  # 0 = översta boxen, 1 = mellersta, 2 = nedersta

    box_x_start = box_x * int(sqrt(len(board)))  # Vänstra boxen startar på index = 0, mitten på index = 3, högra på index = 6
    box_x_end = box_x_start + int(sqrt(len(board)))

    box_y_start = box_y * int(sqrt(len(board)))  # Översta boxen startar på index = 0, mitten på index = 3, nedersta på index = 6
    box_y_end = box_y_start + int(sqrt(len(board)))

    return range(box_x_start, box_x_end), range(box_y_start, box_y_end)


url = 'http://www.cs.utep.edu/cheon/ws/sudoku/new/'
size = 9  # Stöd för 4 & 9
level = 3  # 1 = enkel, 2 = medel, 3 = svår

start_board = request_board(url, size, level)

if not start_board:
    if size == 9:
        start_board = [[0, 0, 9, 7, 0, 0, 0, 0, 6],
                       [0, 0, 7, 0, 9, 0, 0, 4, 2],
                       [0, 2, 4, 6, 0, 3, 0, 0, 0],
                       [0, 0, 0, 4, 0, 0, 9, 0, 0],
                       [6, 0, 0, 0, 0, 0, 0, 0, 1],
                       [0, 0, 5, 0, 0, 8, 0, 0, 0],
                       [0, 0, 0, 9, 0, 4, 2, 7, 0],
                       [4, 5, 0, 0, 3, 0, 8, 0, 0],
                       [7, 0, 0, 0, 0, 6, 3, 0, 0]]
    else:
        start_board = [[4, 0, 0, 0],
                       [0, 0, 4, 0],
                       [0, 1, 0, 0],
                       [2, 0, 0, 1]]

print_board(start_board)
solve(start_board)
print('')
print_board(start_board)
