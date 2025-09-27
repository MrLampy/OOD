class Stack:
    def __init__(self, stack = []):
        self.stack = stack

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        if self.isEmpty():
            return "Stack is empty"
        return self.stack.pop()

    def peek(self):
        if self.isEmpty():
            return "Stack is empty"
        return self.stack[-1]

    def isEmpty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)

class Queue:
  def __init__(self, queue = []):
    self.queue = queue
    
  def enqueue(self, element):
    self.queue.append(element)

  def dequeue(self):
    if self.isEmpty():
      return "Queue is empty"
    return self.queue.pop(0)

  def peek(self):
    if self.isEmpty():
      return "Queue is empty"
    return self.queue[0]

  def isEmpty(self):
    return len(self.queue) == 0

  def size(self):
    return len(self.queue)

class BST:
    class Node:
        def __init__(self, data):
            self.left = None
            self.right = None
            self.data = data
            
        def __repr__(self):
            return f"Node({self.data})"
    def __init__(self):
        self.root = None
        self.bfs = []
        self.pbfs = []
    def insert(self, data):
            new_Node = self.Node(data)
            if not self.root:
                self.root = new_Node
                return self.root
            target = self.root
            while(1):
                if data >= target.data:
                    if target.right:
                        target = target.right
                    else:
                        target.right = new_Node
                        return self.root
                else:
                    if target.left:
                        target = target.left
                    else:
                        target.left = new_Node
                        return self.root
    def _insert(self, node, data):
        pass

    def __str__(self):
        return self._print_tree(self.root, 0)
    def _print_tree(self, node, level):
        if node is None:
            return ""
        result = self._print_tree(node.right, level + 1)
        result += " " * 4 * level + f"{node.data}\n"
        result += self._print_tree(node.left, level + 1)
        return result
    
    def BFS(self, root):
        q = Queue()
        q.enqueue(root)
        while not q.isEmpty():
            n = q.dequeue()
            if n:
                self.bfs.append(n.data)
                if n.left:
                    q.enqueue(n.left)
                if n.right:
                    q.enqueue(n.right)
                    
    def pBFS(self, root):
        q = Stack()
        q.push(root)
        while not q.isEmpty():
            n = q.pop()
            if n:
                self.pbfs.append(n.data)
                if n.left:
                    q.push(n.left)
                if n.right:
                    q.push(n.right)

print('******BFS Pis-sa-dan******')
user = [int(i) for i in input('Enter numbers: ').split(' ')]
main = BST()
for i in user:
    root = main.insert(i)
print(main)
main.BFS(root)
main.pBFS(root)
print(f'BFS: {main.bfs}')
print(f'BFS Pid-Sa-Dan: {main.pbfs}')