# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def solve(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + max(self.solve(root.left),self.solve(root.right))

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        left_height = self.solve(root.left)
        right_height = self.solve(root.right)
        print(left_height, right_height)
        if abs(left_height - right_height) > 1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)
        