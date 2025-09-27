class Node:
    def __init__(self, data):
        self.value = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        
        tail = self.head
        while tail.next:
            tail = tail.next
        tail.next = new_node
        
    def size(self):
        s = 0
        cur = self.head
        while cur:
            cur = cur.next
            s += 1
        return s

    def print_list(self):
        current = self.head
        while current:
            print(current.value, end=" → " if current.next else "\n")
            current = current.next
            
    def swap(self, index : int, k : int):
        round = k
        if round > self.size() : round = self.size()
        if k <= 1: return
        cur = self.head
        post = cur.next
        pre = None
        for i in range(self.size()-index-1):
            # if post == None: break
            cur = self.head
            post = cur.next
            pre = None
            for ii in range(index):
                if post:
                    pre = cur
                    cur = cur.next
                    post = post.next
            # print(cur.value)
            for ii in range(round-1):
                if post:
                    if not pre: self.head = post
                    else: pre.next = post
                    pre = post
                    cur.next = post.next
                    post.next = cur
                    post = cur.next
                
            round -= 1


test = LinkedList()

print(' *** Ant Army ***')
user_input,round = input('Input : ').split(',')
round = int(round)
user_input = user_input.split(' ')
for i in user_input:
    test.append(i)

print('Before : ', end='')
test.print_list()
count = 0
mode = 1

for i in range(test.size()):
    if round == 0 or round == 1: break
    if count%round == 0:
        if mode : 
            test.swap(count,round)
            mode = 0
        else: mode = 1
    count += 1

print('After : ', end='')
test.print_list()