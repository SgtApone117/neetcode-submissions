directions = [[1,0],[-1,0],[0,1], [0,-1]]
class Solution:
    def solve(self,board, idx, i, j, m, n, word):
        if idx == len(word):
            return True
        if i >= m or j >= n or i < 0 or j < 0 or board[i][j] == "$":
            return False
        if board[i][j] != word[idx]:
            return False
        temp = board[i][j]
        board[i][j] = "$"

        for dir in directions:
            i_new = i + dir[0]
            j_new = j + dir[1]
            if self.solve(board, idx + 1, i_new, j_new, m, n, word):
                return True
        board[i][j] = temp
        return False
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0] and self.solve(board, 0, i, j, m, n, word):
                    return True
        return False