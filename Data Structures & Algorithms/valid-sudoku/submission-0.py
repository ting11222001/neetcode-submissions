class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Input: board = 
        # [["1","2",".",".","3",".",".",".","."],
        #  ["4",".",".","5",".",".",".",".","."],
        #  [".","9","8",".",".",".",".",".","3"],
        #  ["5",".",".",".","6",".",".",".","4"],
        #  [".",".",".","8",".","3",".",".","5"],
        #  ["7",".",".",".","2",".",".",".","6"],
        #  [".",".",".",".",".",".","2",".","."],
        #  [".",".",".","4","1","9",".",".","8"],
        #  [".",".",".",".","8",".",".","7","9"]]
        # Output: true

        # HashMap
        # rows: {0: {1, 2, ...}, 1: {4, 5, ...}, ...}
        # grids: {(0, 0): {1, 2, 4, 9, 8,}, (0, 1): {5, 3}, ...}
        # key: (r//3, c//3), val: set
        # if at the 0th row and 7th col, then it's in the grid no.: (0 // 3, 7 // 3) i.e. (0, 2)


        rows = defaultdict(set)
        cols = defaultdict(set)
        grids = defaultdict(set) 

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in grids[(r // 3, c // 3)]:
                    return False
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                grids[(r // 3, c // 3)].add(board[r][c])
        
        return True


