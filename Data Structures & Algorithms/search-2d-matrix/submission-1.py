class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row_l, row_r = 0, len(matrix) - 1
        while row_l <= row_r:
            row_c = (row_l + row_r) // 2
            if matrix[row_c][0] <= target and matrix[row_c][-1] >= target:
                l, r = 0, len(matrix[row_c]) - 1
                found = False
                while l <= r:
                    c = (l + r) // 2
                    if matrix[row_c][c] == target:
                        found = True
                        break
                    elif matrix[row_c][c] > target:
                        r = c - 1
                    elif matrix[row_c][c] < target:
                        l = c + 1
                return found
            elif matrix[row_c][0] > target:
                row_r = row_c - 1
            elif matrix[row_c][0] < target:
                row_l = row_c + 1
            else:
                return False
        return False