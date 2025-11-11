def printBoard(board, n):
    for i in range(n):
        for j in range(n):
            print('Q' if board[i][j] else '.', end=' ')
        print()
    print()


def isSafe(board, row, col, n):
    # Check column for existing queens
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper left diagonal
    i, j = row - 1, col - 1
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check upper right diagonal
    i, j = row - 1, col + 1
    while i >= 0 and j < n:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True


def solveNQueens(board, row, n, all_solutions):
    if row == n:   # Base case — all rows processed
        # Deep copy of current board
        solution = [row[:] for row in board] # Store the current solution
        all_solutions.append(solution)
        return

    # Skip row that already has a fixed queen
    if 1 in board[row]:
        solveNQueens(board, row + 1, n, all_solutions)
        return

    # Try placing queen in every column
    for col in range(n):
        if isSafe(board, row, col, n):
            board[row][col] = 1
            solveNQueens(board, row + 1, n, all_solutions)
            board[row][col] = 0  # backtrack


def nQueensWithFirstPlaced(n, first_row, first_col): 
    board = [[0 for _ in range(n)] for _ in range(n)] # Initialize empty board
    board[first_row][first_col] = 1  # Place the first queen
    all_solutions = []

    solveNQueens(board, 0, n, all_solutions)

    if not all_solutions:
        print("No solution possible with this first queen position.")
    else:
        print(f"\nTotal Solutions Found: {len(all_solutions)}\n")
        for idx, sol in enumerate(all_solutions, 1):
            print(f"Solution {idx}:")
            printBoard(sol, n)


# --- Main Code ---
if __name__ == "__main__":
    n = int(input("Enter size of board (n x n): "))
    r = int(input("Enter row of first queen (0-based): "))
    c = int(input("Enter column of first queen (0-based): "))

    nQueensWithFirstPlaced(n, r, c)
#time complexity: O(N!)
#space complexity: O(N^2)