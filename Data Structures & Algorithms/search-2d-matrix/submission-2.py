class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        row_low = 0
        row_high = rows - 1
        col_low = 0
        col_high = cols - 1

        while row_low <= row_high:
            row_mid = (row_low + row_high) // 2
            col_mid = (col_low + col_high) // 2
            if matrix[row_mid][col_mid] == target:
                return True
            elif matrix[row_mid][col_mid] < target:
                if matrix[row_mid][col_low] <= target <= matrix[row_mid][col_high]:
                    col_low = col_mid + 1
                else:
                    row_low = row_mid + 1
            else:
                if matrix[row_mid][col_low] <= target <= matrix[row_mid][col_high]:
                    col_high = col_mid - 1
                else:
                    row_high = row_mid - 1
        return False


        