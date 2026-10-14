class TreeNode:
    def __init__(self,key=0,val=0,left=None,right=None):
        self.key = key
        self.val = val
        self.left = left
        self.right = right

class TreeMap:
    def __init__(self):
        self.root = None
    def new_node(self, key,val):
        return TreeNode(key,val)
    def insert(self, key: int, val: int) -> None:
        new_node_temp = self.new_node(key,val)
        if not self.root:
            self.root = new_node_temp
            return
        curr = self.root
        while True:
            if key < curr.key:
                if not curr.left:
                    curr.left = new_node_temp
                    return
                else:
                    curr = curr.left
            elif key > curr.key:
                if not curr.right:
                    curr.right = new_node_temp
                    return
                else:
                    curr = curr.right
            else:
                curr.val = val
                return


    def get(self, key: int) -> int:
        if not self.root:
            return -1
        curr = self.root
        while curr:
            if key < curr.key:
                curr = curr.left
            elif key > curr.key:
                curr = curr.right
            else:
                return curr.val
        return -1

    def getMin(self) -> int:
        if not self.root:
            return -1
        curr = self.root
        while curr and curr.left:
            curr = curr.left
        return curr.val if curr else -1

    def getMax(self) -> int:
        if not self.root:
            return -1
        curr = self.root
        while curr and curr.right:
            curr = curr.right
        return curr.val if curr else -1

    def remove(self, key: int) -> None:
        def GetRightMax(node):
            if not node.right:
                return node
            return GetRightMax(node.right)
        def HelperFunc(node):
            if not node.left:
                return node.right
            if not node.right:
                return node.left
            right_subtree = node.right
            left_max = GetRightMax(node.left)
            left_max.right = right_subtree
            return node.left
        
        if not self.root:
            return self.root
        if self.root.key == key:
            self.root = HelperFunc(self.root)
            return
        
        dummy_node = self.root
        while self.root:
            if self.root.key > key:
                if self.root.left and self.root.left.key == key:
                    self.root.left = HelperFunc(self.root.left)
                    break
                else:
                    self.root = self.root.left
            else:
                if self.root.right and self.root.right.key == key:
                    self.root.right = HelperFunc(self.root.right)
                    break
                else:
                    self.root = self.root.right
        self.root = dummy_node

    def getInorderKeys(self) -> List[int]:
        curr = self.root
        result = []
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            result.append(node.key)
            inorder(node.right)
        inorder(curr)
        return result
