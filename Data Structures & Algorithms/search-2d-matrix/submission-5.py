class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m_dim = len(matrix) - 1
        b, t = 0, m_dim
        
        while b <= t:
            curr_row = b + ((t-b) // 2)
            if matrix[curr_row][0] == target:
                return True
            
            if matrix[curr_row][0] <= target <= matrix[curr_row][-1]:
                l, r = 0, len(matrix[curr_row]) - 1
                while l <= r:
                    curr_col = l + ((r-l) // 2)
                    if matrix[curr_row][curr_col] < target:
                        l = curr_col + 1
                    elif matrix[curr_row][curr_col] > target:
                        r = curr_col - 1
                    else:
                        return True
                return False

            elif matrix[curr_row][0] < target and matrix[curr_row][-1] < target:
                b = curr_row + 1
            else:
                t = curr_row - 1


        return False