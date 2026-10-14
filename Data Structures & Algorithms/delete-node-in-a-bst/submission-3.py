# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def GetRightNode(self,node):
        if not node.right:
            return node
        return self.GetRightNode(node.right)
    def HelperFunc(self,node):
        if not node.left:
            return node.right
        if not node.right:
            return node.left
        right_subtree = node.right
        left_subtree_right_most_node = self.GetRightNode(node.left)
        left_subtree_right_most_node.right = right_subtree
        return node.left
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return root
        if root.val == key:
            return self.HelperFunc(root)
        dummy_node = root
        while root:
            if root.val > key:
                if root.left and root.left.val == key:
                    root.left = self.HelperFunc(root.left)
                    break
                else:
                    root = root.left
            else:
                if root.right and root.right.val == key:
                    root.right = self.HelperFunc(root.right)
                    break
                else:
                    root = root.right
        return dummy_node

        