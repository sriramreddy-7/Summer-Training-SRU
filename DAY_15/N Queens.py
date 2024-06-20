def is_safe(board, row, col):
    for i in range(row):
        if board[i] == col:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i] == j:
            return False

    for i, j in zip(range(row, -1, -1), range(col, len(board))):
        if board[i] == j:
            return False

    return True


def solve_nqueens_util(board, row):
    if row >= len(board):
        return True

    for col in range(len(board)):
        if is_safe(board, row, col):
            board[row] = col
            if solve_nqueens_util(board, row + 1):
                return True
            board[row] = -1

    return False


def solve_nqueens(n):
    board = [-1] * n
    if solve_nqueens_util(board, 0):
        return board
    else:
        return None


def print_solution(board):
    n = len(board)
    for i in range(n):
        row = ['.'] * n
        row[board[i]] = 'Q'
        print(' '.join(row))


# Example Usage
n = 8
solution = solve_nqueens(n)
if solution:
    print_solution(solution)
else:
    print("No solution exists for the given N.")


def is_safe(board, row, col):
    # Check if there's a queen in the same column
    for i in range(row):
        if board[i] == col:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i] == j:
            return False

    for i, j in zip(range(row, -1, -1), range(col, len(board))):
        if board[i] == j:
            return False

    return True


def solve_nqueens_util(board, row):
    if row >= len(board):
        return True

    for col in range(len(board)):
        if is_safe(board, row, col):
            board[row] = col
            if solve_nqueens_util(board, row + 1):
                return True

            board[row] = -1

    return False


def solve_nqueens(n):
    board = [-1] * n
    if solve_nqueens_util(board, 0):
        return board
    else:
        return None


def print_solution(board):
    n = len(board)
    for i in range(n):
        row = ['.'] * n
        row[board[i]] = 'Q'
        print(' '.join(row))


n = 8
solution = solve_nqueens(n)
if solution:
    print_solution(solution)
else:
    print("No solution exists for the given N.")


def queen(r):
    if r == n:
        return
    for c in range(n):
        if check(r, c):
            m[r][c] = 1
            queen(r + 1)
            return
    return


def check(i, j):
    if i == u or j == v:
        return False

    for k in range(i):
        if m[k][j] == 1:
            return False

    r, c = i, j
    while r >= 0 and c >= 0:
        if m[r][c] == 1:
            return False
        r -= 1
        c -= 1

    r, c = i, j
    while r >= 0 and c < n:
        if m[r][c] == 1:
            return False
        r -= 1
        c += 1

    return True


n = 5
u = 1
v = 3
m = [[0] * n for _ in range(n)]

queen(0)
print(m)