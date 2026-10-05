# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def solve(self, root):
        if not root:
            return 0
        left_height = self.solve(root.left)
        right_height = self.solve(root.right)

        return 1 + max(left_height, right_height)
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.solve(root)