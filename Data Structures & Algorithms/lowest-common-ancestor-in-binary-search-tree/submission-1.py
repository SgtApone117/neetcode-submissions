# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root or root.val == p.val or root.val == q.val:
            return root
        left_root = self.lowestCommonAncestor(root.left, p,q)
        right_root = self.lowestCommonAncestor(root.right,p,q)

        if not left_root:
            return right_root
        if not right_root:
            return left_root
        return root