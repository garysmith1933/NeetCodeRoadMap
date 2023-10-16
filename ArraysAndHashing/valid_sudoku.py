class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #create hash sets for the rows, columns, and 3*3 squares
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        squares = collections.defaultdict(set)

      # we iterate up to 9 because it is a 9 x 9 board, we iterate over the rows, and columns to get the specific positions
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
              #if the number is a duplcate in rows, cols, or in the specifc 3 x 3 grid, its false
                if ( board[r][c] in rows[r] or 
                board[r][c] in cols[c] or 
                board[r][c] in squares[(r//3, c//3)]): return False
              # otherwise add to the sets
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                squares[(r//3, c//3)].add(board[r][c])
        return True
    
    #Time O(9^2)
    # Space O(9^2)