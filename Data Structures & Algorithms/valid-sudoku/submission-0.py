class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_check = defaultdict(set)
        col_check = defaultdict(set)
        sub_check = defaultdict(set)
        for i in range(len(board)):
            for j in range(len(board)):
                print(board[i], i)
                if board[i][j] == ".":
                    continue
                elt = int(board[i][j])
                if elt in row_check[i]:
                    print(elt, row_check[i], "row_fail")
                    return False
                row_check[i].add(elt)
                if elt in col_check[j]:
                    print(elt, col_check[j], "col_fail")
                    return False
                col_check[j].add(elt)
                sub_idx = ((i//3) * 3) + (j//3)
                if elt in sub_check[sub_idx]:
                    print(elt, sub_check[sub_idx], "sub_fail")
                    return False
                sub_check[sub_idx].add(elt)
        return True