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
    
    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, str(node.data))
            self.printTree(node.left, level + 1)
    
    def most_vul(self, root):
        global ans
        if root == None:
            return
        ans.append(root.data)
        if self.most_vul(root.right):
            self.most_vul(root.right)
        else: self.most_vul(root.left)
    
user = [int(i) for i in input('Enter tree nodes: ').split(' ')]
main = AVLTree()
for i in user:
    main.root = main.insert(main.root, i)
ans = []
main.most_vul(main.root)
main.printTree(main.root)
# print(ans)
# print(main.get_height(main.root))
ans = ans[:main.get_height(main.root)]
count = 0
print()
print('Path with maximum sum: ',end='')
for i in ans[:-1]:
    print(i,end=' + ')
    count += i
print(ans[-1],end=f' = {count+ans[-1]}')