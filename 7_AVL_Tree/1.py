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

        if balance < -1 and data > root.right.data:
            return self.rotate_left(root)

        if balance > 1 and data > root.left.data:
            root.left = self.rotate_left(root.left)
            return self.rotate_right(root)

        if balance < -1 and data < root.right.data:
            root.right = self.rotate_right(root.right)
            return self.rotate_left(root)

        return root
    
    def find_k_smallest(self, root, k: int):
        global count
        if root:
            self.find_k_smallest(root.left, k)
            if count == k: print(root.data)
            count += 1
            self.find_k_smallest(root.right, k)
            
            
print('*** Simple but more ***')
nodes, data, smallest = input('input  N node, Data, K small : ').split(',')
data = [int(i) for i in data.split(' ')]
nodes,smallest = int(nodes),int(smallest)
main = AVLTree()
count = 1
for i in data:
    main.root = main.insert(main.root, i)
main.find_k_smallest(main.root, smallest)