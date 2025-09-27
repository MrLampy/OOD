class BST:
    class Node:
        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None
            self.h = 1

        def update_height(self):
            left_height = self.left.h if self.left else 0
            right_height = self.right.h if self.right else 0
            self.h = 1 + max(left_height, right_height)
    
        def balance_factor(self):
            left_height = self.left.h if self.left else 0
            right_height = self.right.h if self.right else 0
            return left_height - right_height
        
    def __init__(self):
        self.root = None
    
    def insert(self,key):
        if not self.root:
            self.root = BST.Node(key)
        else:
            BST._insert(self.root,key)

    def _insert(node,key):
        if key < node.data:
            if node.left:
                BST._insert(node.left,key)
            else:
                node.left = BST.Node(key)
        else:
            if node.right:
                BST._insert(node.right,key)
            else:
                node.right = BST.Node(key)
    
    def _get_format(root,ans = ""):
        if root:
            temp = ""
            if root.right:
                temp += BST._get_format(root.right,ans + "     ")
            temp += f"{ans}{root.data}\n"
            if root.left:
                temp += BST._get_format(root.left,ans + "     ")
            return temp
        return ""
    
    def __str__(self):
        return BST._get_format(self.root)

def isAVL(node : BST.Node):
    if node is None:
        return True, 0

    is_left_avl, left_h = isAVL(node.left)
    is_right_avl, right_h = isAVL(node.right)

    if not is_left_avl or not is_right_avl:
        return False, 0

    current_h = 1 + max(left_h, right_h)
    balance_factor = abs(left_h - right_h)
    
    if balance_factor <= 1:
        return True, current_h
    else:
        return False, current_h

tree = BST()

print("**********IsAVL**********")
for i in list(map(int, input("Enter numbers to insert in the tree: ").split())):
    tree.insert(i)
print("Tree:")
print(tree)
is_avl_tree, _ = isAVL(tree.root)
print("Is AVL???:", is_avl_tree)