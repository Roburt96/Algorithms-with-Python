def find_paths(row, col, matrix, direction, path):
    if row < 0 or col < 0 or row >= len(matrix) or col >= len(matrix[0]):
        return
    if matrix[row][col] == '*':
        return
    if matrix[row][col] == 'v':
        return

    path.append(direction)
    if matrix[row][col] == 'e':
        print(''.join(path))
    else:
        matrix[row][col] = 'v'

        find_paths(row - 1, col, matrix, 'U', path)
        find_paths(row + 1, col, matrix, 'D', path)
        find_paths(row, col - 1, matrix, 'L', path)
        find_paths(row, col + 1, matrix, 'R', path)
        matrix[row][col] = '-'

    path.pop()

rows, cols = int(input()), int(input())
matrix = [list(input()) for _ in range(rows)]
find_paths(0, 0, matrix, '', [])

