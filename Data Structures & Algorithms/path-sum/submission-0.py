# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        sum_count = [0]
        def dfs(node):
            if not node:
                return False
            sum_count[0] += node.val
            if not node.left and not node.right:
                if sum_count[0] == targetSum:
                    return True
                sum_count[0] -= node.val
                return False
            left = dfs(node.left)
            if left:
                return True
            right = dfs(node.right)
            if right:
                return True
            sum_count[0] -= node.val
            return False
        return dfs(root)