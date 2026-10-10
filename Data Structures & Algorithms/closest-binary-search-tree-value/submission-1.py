# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        if not root:
            return -1
        res = [root.val]
        min_diff = [abs(root.val - target)]
        def solve(node):
            if not node:
                return
            solve(node.left)
            diff = abs(node.val - target)
            if diff < min_diff[0]:
                res[0] = node.val
                min_diff[0] = diff
            solve(node.right)
        solve(root)
        return res[0]
