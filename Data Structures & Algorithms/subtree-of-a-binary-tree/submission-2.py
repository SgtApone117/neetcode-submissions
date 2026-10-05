# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def CheckIfSubTree(self,new_root,subRoot):
        if not new_root and not subRoot:
            return True
        if not new_root or not subRoot:
            return False
        if new_root.val != subRoot.val:
            return False
        return self.CheckIfSubTree(new_root.left, subRoot.left) and self.CheckIfSubTree(new_root.right, subRoot.right)

    def FindSubRoot(self, root, subRoot):
        if not root:
            return False
        if root.val == subRoot.val:
            if self.CheckIfSubTree(root,subRoot):
                return True 
        return self.FindSubRoot(root.left,subRoot) or self.FindSubRoot(root.right,subRoot)  
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return None
        return self.FindSubRoot(root, subRoot)