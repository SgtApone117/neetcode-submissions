# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self,root,res):
        if not root:
            return
        self.solve(root.left,res)
        self.solve(root.right,res)
        res.append(root.val)

    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if not root:
            return res
        self.solve(root,res)
        return res
        