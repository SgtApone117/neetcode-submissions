# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def GetRightNode(self,root):
        if not root.right:
            return root
        return self.GetRightNode(root.right)

    def HelperFunc(self,root):
        # if deleting nodes left subtree does not exist make parent of deleting nodes left as right
        if not root.left:
            return root.right
        # if deleting nodes right subtree does not exist make parent of deleting nodes left as left
        if not root.right:
            return root.left
        # if deleting node has both left and right get right subtree
        right_subtree = root.right
        # get the right most node of the deleting nodes left subtree
        last_node = self.GetRightNode(root.left)
        # the right most ndoe of left subtree (deleting nodes) assign it the right subtree of deleting node
        last_node.right = right_subtree
        # return the deleting nodes left subtree (right has been added to this and right becomes null)
        return root.left

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return root
        
        # if root is key
        if root.val == key:
            return self.HelperFunc(root)

        original_root = root
        while root:
            # if root's value is greater than key then check left subtree
            if root.val > key:
                # if left subtree exists and root's immediate next(left) nodes data is key
                if root.left and root.left.val == key:
                    # assign root's left with the new subtree post deletion
                    root.left = self.HelperFunc(root.left)
                else:
                    # did not find key ? move left
                    root = root.left
            else:
                # key is in right subtree
                # if right subtree exists and root's immediate next(right) nodes data is key
                if root.right and root.right.val == key:
                    # assign root's right with the new subtree post deletion
                    root.right = self.HelperFunc(root.right)
                else:
                    # did not find key ? move right
                    root = root.right
        return original_root