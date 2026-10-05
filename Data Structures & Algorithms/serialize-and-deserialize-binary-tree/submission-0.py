# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""
        res = []
        q = deque([root])
        while q:
            node = q.popleft()
            if not node:
                res.append("#")
            else:
                res.append(str(node.val))
                q.append(node.left)
                q.append(node.right)
        return ",".join(res)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None
        data = deque(data.split(","))
        root = TreeNode(int(data.popleft()))
        q = deque([root])

        while q:
            node = q.popleft()

            left_val = data.popleft()
            if left_val != "#":
                left_node = TreeNode(int(left_val))
                node.left = left_node
                q.append(left_node)
            right_val = data.popleft()
            if right_val != "#":
                right_node = TreeNode(int(right_val))
                node.right = right_node
                q.append(right_node)
        return root
