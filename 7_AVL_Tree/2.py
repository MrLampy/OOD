class AVLNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def __init__(self):
        self.root = None

    def get_height(self, node):
        if not node:
            return 0
        return node.height

    def get_balance_factor(self, node):
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    def rotate_right(self, y):
        x = y.left
        T2 = x.right

        x.right = y
        y.left = T2


        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))

        return x

    def rotate_left(self, x):
        y = x.right
        T2 = y.left

        y.left = x
        x.right = T2

        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y

    def insert(self, root, data):
        if not root:
            return AVLNode(data)
        elif data < root.data:
            root.left = self.insert(root.left, data)
        else:
            root.right = self.insert(root.right, data)

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        balance = self.get_balance_factor(root)

        if balance > 1 and data < root.left.data:
            return self.rotate_right(root)

        if balance < -1 and data >= root.right.data:
            return self.rotate_left(root)

        if balance > 1 and data >= root.left.data:
            root.left = self.rotate_left(root.left)
            return self.rotate_right(root)

        if balance < -1 and data < root.right.data:
            root.right = self.rotate_right(root.right)
            return self.rotate_left(root)

        return root
    
    def pre_order_traversal(self, root):
        if not root:
            return []
        return [root.data] + self.pre_order_traversal(root.left) + self.pre_order_traversal(root.right)
    
    def in_order_traversal(self, root):
        if not root:
            return []
    
        return self.in_order_traversal(root.left) + [root.data] + self.in_order_traversal(root.right)
    
    def post_order_traversal(self, root):
        if not root:
            return []
    
        return self.in_order_traversal(root.left)  + self.in_order_traversal(root.right) + [root.data]

    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('    ' * level + str(node.data))
            self.printTree(node.left, level + 1)

def check_same_tree(Tree1: AVLTree, Tree2: AVLTree):
    C1In = Tree1.in_order_traversal(Tree1.root)
    C2In = Tree2.in_order_traversal(Tree2.root)
    C1Pre = Tree1.pre_order_traversal(Tree1.root)
    C2Pre = (Tree2.pre_order_traversal(Tree2.root))
    C1Post = (Tree1.post_order_traversal(Tree1.root))
    C2Post = (Tree2.post_order_traversal(Tree2.root))
    if C1In == C2In and C1Pre == C2Pre and C1Post == C2Post:
        print('Same Tree')
    else: print('Different Tree')

    
Tree1 = AVLTree()
Tree2 = AVLTree()


Tree1_inp, Tree2_inp = (input("Enter Tree1/Tree2 : ")).split("/")

Tree1_inp = Tree1_inp.split()

Tree2_inp = Tree2_inp.split()



for data in Tree1_inp:

    Tree1.root = Tree1.insert(Tree1.root, int(data))



for data in Tree2_inp:

    Tree2.root = Tree2.insert(Tree2.root, int(data))

   

print("Tree 1")    

Tree1.printTree(Tree1.root)



print()

print("Tree 2")

Tree2.printTree(Tree2.root)



print()
check_same_tree(Tree1, Tree2)