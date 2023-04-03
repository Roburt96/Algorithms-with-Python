def board_print(board):
    [print(*row) for row in board]
    print()


def can_place_queen(row, col, rows, cols, l_diagonal, r_diagonals):
    if row in rows:
        return False
    if col in cols:
        return False
    if (row - col) in l_diagonal:
        return False
    if (row + col) in r_diagonals:
        return False
    return True


def set_queen(row, col, board, rows, cols, l_diagonal, r_diagonals):
    board[row][col] = '*'
    rows.add(row)
    cols.add(col)
    l_diagonal.add((row - col))
    r_diagonals.add((row + col))


def remove_queen(row, col, board, rows, cols, l_diagonal, r_diagonals):
    board[row][col] = '-'
    rows.remove(row)
    cols.remove(col)
    l_diagonal.remove((row - col))
    r_diagonals.remove((row + col))


def put_queens(row, board, rows, cols, l_diagonal, r_diagonals):
    if row == 8:
        board_print(board)
        return

    for col in range(8):
        if can_place_queen(row, col, rows, cols, l_diagonal, r_diagonals):
            set_queen(row, col, board, rows, cols, l_diagonal, r_diagonals)
            put_queens(row + 1, board, rows, cols, l_diagonal, r_diagonals)
            remove_queen(row, col, board, rows, cols, l_diagonal, r_diagonals)


n = 8
board = [['-' for _ in range(n)] for _ in range(n)]
put_queens(0, board, set(), set(), set(), set())