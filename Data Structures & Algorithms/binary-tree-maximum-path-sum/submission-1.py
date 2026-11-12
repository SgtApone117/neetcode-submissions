# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def solve(self, root, maxi):
        if not root:
            return 0
        left_max = max(0, self.solve(root.left,maxi))
        right_max = max(0, self.solve(root.right, maxi))
        maxi[0] = max(maxi[0], root.val + left_max+right_max)
        return root.val + max(left_max, right_max)
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        maxi = [float('-inf')]
        self.solve(root,maxi)
        return maxi[0]