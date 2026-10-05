# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def GetPathToNode(self,root, data, path):
        if not root:
            return False
        path.append(root)
        if root.val == data:
            return True
        if self.GetPathToNode(root.left, data,path) or self.GetPathToNode(root.right, data, path):
            return True
        path.pop()
        return False

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root:
            return root
        path_p,path_q = [],[]
        self.GetPathToNode(root,p.val,path_p)
        self.GetPathToNode(root,q.val,path_q)
        i,last_common_seen = 0,None
        while i < len(path_p) and i < len(path_q):
            if path_p[i].val == path_q[i].val:
                last_common_seen = path_p[i]
            i += 1
        return last_common_seen


        