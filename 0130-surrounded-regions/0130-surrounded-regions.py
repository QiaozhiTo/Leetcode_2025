class Solution:
    def solve(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows, cols = len(board), len(board[0])
        def capture(r, c):
            if r < 0 or r == rows or c < 0 or c == cols or board[r][c] != 'O':
                return 
                # if X, won't keep going the following dfs
            board[r][c] = 'T'
            capture(r, c + 1)
            capture(r, c - 1)
            capture(r + 1, c)
            capture(r - 1, c)
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O' and (r in [0, rows - 1] or c in [0, cols - 1]):
                    capture(r, c)

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                if board[r][c] == 'T':
                    board[r][c] = 'O'        