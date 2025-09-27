class Node:
    def __init__(self, data):
        self.value = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        
        tail = self.head
        while tail.next:
            tail = tail.next
        tail.next = new_node
        self.tail = new_node
        
    def size(self):
        s = 0
        cur = self.head
        while cur:
            cur = cur.next
            s += 1
        return s

user_input = input('Git History: ').replace(' -> ',' ').split(' | ')
user_input = [i.split(' ') for i in user_input]
main = LinkedList()
end = user_input[0][-1]
user_input[0].pop()
good = 0
for i in range(1,len(user_input)):
    if end != user_input[i][-1]:
        good = 1
    user_input[i].pop()
for i in user_input:
    if good == 1: break
    for ii in i:
            main.append(int(ii))
    main.append(' | ')

if not good:
    cur = main.head
    count = 0
    while cur.next:
        if cur.value == ' | ': 
            cur = cur.next
            continue
        index = cur.next
        while index:
            if index.value == cur.value and index.next != None:
                if cur.next.value != index.next.value and (cur.next.value != ' | ' or index.next.value != ' | '):
                    count += 1
                if cur.next.value == index.next.value:
                    pre.next = index.next
            pre = index
            index = index.next
        cur = cur.next

# cur = main.head
# while cur:
#     print(cur .value)
#     cur = cur.next
    
if good == 1:
    print('Are these branches in the same repository? False')
else:
    print('Are these branches in the same repository? True')
    print(f'{count} Merge(s)')