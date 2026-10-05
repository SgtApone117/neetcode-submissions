# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def BuildTree(self, preorder,preStart,preEnd, inorder, inStart,inEnd, inMap):
        if preStart > preEnd or inStart > inEnd:
            return None
        root = TreeNode(preorder[preStart])
        in_root = inMap[root.val]
        left_subtree_size = in_root-inStart

        root.left = self.BuildTree(preorder,preStart + 1, preStart+left_subtree_size,inorder, inStart,in_root-1,inMap)
        root.right = self.BuildTree(preorder, preStart+1+left_subtree_size, preEnd, inorder, in_root+1, inEnd,inMap)
        return root

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inMap = {}
        m = len(preorder)
        n = len(inorder)
        for i in range(n):
            inMap[inorder[i]] = i
        root = self.BuildTree(preorder,0,m-1,inorder,0,n-1,inMap)
        return root
        