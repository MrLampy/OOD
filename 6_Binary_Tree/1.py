class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        new_Node = Node(data)
        if not self.root:
            self.root = new_Node
            return self.root
        target = self.root
        while(1):
            if data > target.data:
                if target.right:
                    target = target.right
                else:
                    target.right = new_Node
                    return self.root
            if data < target.data:
                if target.left:
                    target = target.left
                else:
                    target.left = new_Node
                    return self.root
    
    def printTree(self, node, level = 0):
        if node:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
for i in inp:
    root = T.insert(i)
T.printTree(root)