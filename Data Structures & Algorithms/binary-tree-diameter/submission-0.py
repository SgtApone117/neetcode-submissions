# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def solve(self,root,diameter):
        if not root:
            return 0
        left_depth = self.solve(root.left,diameter)
        right_depth = self.solve(root.right,diameter)
        diameter[0] = max(diameter[0], left_depth + right_depth)
        return 1 + max(left_depth, right_depth)
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = [0]
        self.solve(root, diameter)
        return diameter[0]