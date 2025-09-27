class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
class BST:
    def __init__(self):
        self.root = None
        self.in_order1 = []
        self.post_order1 = []
        self.pre_order1 = []
        self.bfs1 = []
        
    def insert(self, data):
        new_Node = Node(data)
        if not self.root:
            self.root = new_Node
            return
        target = self.root
        while(1):
            if data > target.data:
                if target.right:
                    target = target.right
                else:
                    target.right = new_Node
                    return
            if data < target.data:
                if target.left:
                    target = target.left
                else:
                    target.left = new_Node
                    return
                
    def print_tree(self, root, level = 0):
        self.print_tree(root.right, level+1)
        print('     '*level, root)
        self.print_tree(root.left, level+1)
        
    def in_order(self, root):
        if root:
            self.in_order(root.left)
            self.in_order1.append(root.data)
            self.in_order(root.right)
            
    def post_order(self, root):
        if root:
            self.post_order(root.left)
            self.post_order(root.right)
            self.post_order1.append(root.data)
            
    def pre_order(self, root):
        if root:
            self.pre_order1.append(root.data)
            self.pre_order(root.left)
            self.pre_order(root.right)
            
    def bfs(self, root):
        q = [root]
        while len(q):
            n = q.pop(0)
            self.bfs1.append(n.data)
            if n.left:
                q.append(n.left)
            if n.right:
                q.append(n.right)
    
if __name__ == "__main__":
    main = BST()
    user = [int(i) for i in input('Enter Input : ').split(' ')]
    for i in user:
        main.insert(i)
    main.in_order(main.root)
    main.post_order(main.root)
    main.pre_order(main.root)
    main.bfs(main.root)
    print(f'Preorder :', " ".join(map(str, main.pre_order1)))
    print("Inorder :", " ".join(map(str, main.in_order1)))
    print(f'Postorder :', " ".join(map(str, main.post_order1)))
    print(f'Breadth :', " ".join(map(str, main.bfs1)))