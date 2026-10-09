class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        row = len(matrix)
        col = len(matrix[0])

        left,top,right,bottom = 0, 0, col-1, row-1
        res = [0] * (row * col)
        idx = 0

        while left <= right and top <= bottom:
            for i in range(left,right+1):
                res[idx] = matrix[top][i]
                idx += 1
            top += 1

            for i in range(top,bottom+1):
                res[idx] = matrix[i][right]
                idx += 1
            right -= 1

            if left > right or top > bottom:
                break

            for i in range(right,left-1,-1):
                res[idx] = matrix[bottom][i]
                idx += 1
            bottom -= 1

            for i in range(bottom,top-1,-1):
                res[idx] = matrix[i][left]
                idx += 1
            left += 1
        return res

            