class LinkedList:
    class Node:
        def __init__(self, value):
            self.value = value
            self.next = None
        
    def __init__(self):
        self.head = None
        self.tail = self.head
        self.size = 0
    
    def isEmpty(self):
        return self.head == None
    
    def append(self,data):
        new_tail = self.Node(data)
        if self.isEmpty(): 
            self.tail = self.head = new_tail
        else:
            self.tail.next = new_tail
            self.tail = new_tail
        self.size += 1
        
    def __str__(self):
        ans = []
        node = self.head
        while node:
            ans.append(str(node.value))
            node = node.next
        return '->'.join(ans)
    
print('*****Bubble Sort Linked List*****')
user_input = input('Enter Input: ').split(',')
print('Input List: ', end='')
main = LinkedList()
for i in user_input:
    main.append(i)
print(str(main).replace(" ",""))
print('_______________________________________')
# print(main.size)
for i in range(main.size):
    if main.isEmpty() or main.size == 1: break
    cur = main.head
    pre = None
    post = cur.next
    while(post):
        if int(cur.value) > int(post.value):
            if pre == None:
                main.head = post
            else:
                pre.next = post
            if post.next == None:
                main.tail = cur
            print()
            print(f'Swapping {str(cur.value).replace(" ","")} and {post.value}')
            cur.next = post.next
            post.next = cur
            pre = post
            print(f'List: {str(main).replace(" ","")}')
        else:
            pre = cur
            cur = cur.next
        post = cur.next
print('_______________________________________')
print(f'Sorted List: {str(main).replace(" ","")}')