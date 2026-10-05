# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def solve(self,left_root,right_root):
        if not left_root and not right_root:
            return True
        if not left_root or not right_root:
            return False
        if left_root.val != right_root.val:
            return False
        return self.solve(left_root.left,right_root.left) and self.solve(left_root.right, right_root.right)
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return self.solve(p,q)