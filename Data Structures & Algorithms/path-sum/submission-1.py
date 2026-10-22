# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        total_sum = [0]
        def solve(node):
            if not node:
                return False
            total_sum[0] += node.val
            if not node.left and not node.right:
                res = (total_sum[0] == targetSum)
                total_sum[0] -= node.val
                return res
            if solve(node.left):
                return True
            if solve(node.right):
                return True
            total_sum[0] -= node.val
            return False
        return solve(root)