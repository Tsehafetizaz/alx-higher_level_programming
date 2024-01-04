#!/usr/bin/python3

import sys


def is_safe(board, row, col):
    for i in range(row):
        if board[i][col] == 1:
            return False
        i, j = row, col
        while i >= 0 and j >= 0:
            if board[i][j] == 1:
                return False
            i -= 1
            j -= 1
            i, j = row, col
            while i >= 0 and j < len(board):
                if board[i][j] == 1:
                    return False
                i -= 1
                j += 1
                return True

            def solve_n_queens(n, board, row):
                if row == n:
                    print(board)
                    return
                for col in range(n):
                    if is_safe(board, row, col):
                        board[row][col] = 1
                        solve_n_queens(n, board, row + 1)
                        board[row][col] = 0

                        def main():
                            if len(sys.argv) != 2:
                                print("Usage: nqueens N", file=sys.stderr)
                                sys.exit(1)
                                try:
                                    n = int(sys.argv[1])
                                except ValueError:
                                    print("N must be a number",
                                          file=sys.stderr)
                                    sys.exit(1)
                                    if n < 4:
                                        print("N must be at least 4",
                                              file=sys.stderr)
                                        sys.exit(1)
                                        board = [[0 for _ in range(n)]
                                                 for _ in range(n)]
                                        solve_n_queens(n, board, 0)

                                        if __name__ == "__main__":
                                            main()
