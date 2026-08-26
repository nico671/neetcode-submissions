class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = {i: set() for i in range(9)}
        cols = {i: set() for i in range(9)}
        squares = {i: set() for i in range(9)}

        for row in range(len(board)):
            for col in range(len(board[0])):
                elt = board[row][col]
                if elt == '.':
                    continue
                
                if elt in rows[row]:
                    return False
                else:
                    rows[row].add(elt)
                
                if elt in cols[col]:
                    return False
                else:
                    cols[col].add(elt)
                
                sq_idx = math.floor(row/3) + (3*math.floor(col/3))

                if elt in squares[sq_idx]:
                    return False
                else:
                    squares[sq_idx].add(elt)
        return True