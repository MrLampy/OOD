class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
class Queue:
    def __init__(self, queue = []):
        self.queue = queue
    
    def enqueue(self, data):
        self.queue.append(data)
        
    def dequeue(self):
        return self.queue.pop(0)

    def isEmpty(self):
        return len(self.queue) == 0
        
class BST:
    def __init__(self):
        self.root = []
        
    def insert(self, data: int):
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

    def print_tree(self, node, level = 0):
        if node != None:
            self.print_tree(node.right, level+1)
            print('     ' * level, node.data)
            self.print_tree(node.left, level+1)
            
    def BFS(self, root):
        count = 0
        q = Queue([root])
        while not q.isEmpty():
            n = q.dequeue()
            if n:
                if k < n.data: n.data = k*n.data
                count += n.data
                if n.left: q.enqueue(n.left)
                if n.right: q.enqueue(n.right)
        return count
print('**Sum of tree**')
user, k = input('Enter input : ').split('/')
user = [int(i) for i in user.split(' ')]

checked = []
for i in user:
    if i in checked:
        continue
    else:
        checked.append(i)
user = checked
k = int(k)
print()
print('Tree before:')
main = BST()
count = 0
for i in user:
    root = main.insert(i)
    count += i
main.print_tree(root)
print(f'Sum of all nodes = {count}')
print()
count = main.BFS(root)
print('Tree after:')
main.print_tree(root)
print(f'Sum of all nodes = {count}')