# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def solve(node):
            if not node:
                return 0
            left_node = solve(node.left)
            if left_node == -1:
                return -1
            right_node = solve(node.right)
            if right_node == -1:
                return -1
            if abs(left_node-right_node) > 1:
                return -1
            return 1 + max(left_node,right_node)
            
        return solve(root) != -1