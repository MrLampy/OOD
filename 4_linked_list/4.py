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
        
    def pop(self, index):
        cur = self.head
        pre = None
        inx = 0
        if self.isEmpty(): return
        while cur:
            if inx == int(index):
                if pre == None:
                    self.head = cur.next
                else:
                    pre.next = cur.next
                self.size -= 1
                break
            pre = cur
            cur = cur.next
            inx += 1
            
    def __str__(self):
        ans = []
        node = self.head
        while node:
            ans.append(str(node.value))
            node = node.next
        return str(ans)
    
    def insert(self, index ,data):
        # insert ใช้ได้แค่ตัวก่อน กลาง แต่ใช้ต่อหลังไม่ได้อันนั้นไปใช้ append
        cur = self.head
        pre = None
        inx = 0
        new_node = self.Node(data)
        if self.isEmpty(): return
        while cur:
            if inx == int(index):
                if pre == None:
                    self.head = new_node
                else:
                    pre.next = new_node
                new_node.next = cur
                self.size += 1
                break
            pre = cur
            cur = cur.next
            inx += 1
        
            
                

main = LinkedList()
print('***This colony is our home***')
user_input = input('Enter input : ').split('/')
initial = user_input[0].split(' ')
command = user_input[1].split(',')
w_ant = int(initial[0])
a_ant = int(initial[1])
angy = 0
print('Current Ant List: ',end='')
for i in range(1, w_ant+1):
    print(f'W{i}', end=' ')
    main.append(f'W{i}')
for i in range(1, a_ant+1):
    print(f'A{i}',end=' ')
    main.append(f'A{i}')
if main.isEmpty(): print('Empty',end='')
print()
print()

for i in command:
    if i[0] == 'C':
        # print(main)
        print(f'Food carrying mission : ',end='')
        if main.isEmpty(): print('Empty', end='')
        cost = int(i[2:])
        while not main.isEmpty() and cost > 0:
            if main.head.value[0] == 'W':
                cost -= 2
                w_ant -= 1
            else: 
                cost -= 5
                a_ant -= 1
            print(f'{main.head.value} ',end='')
            main.pop(0)
        print()
        if main.isEmpty() and cost > 0:
            print('The food load is incomplete!')
            print('Queen is angry! ! !')
            angy += 1
            
        
    if i[0] == 'F':
        # print(main)
        print(f'Attack mission : ',end='')
        if main.isEmpty(): print('Empty', end='')
        cost = int(i[2:])
        while not main.isEmpty() and cost > 0:
            if main.head.value[0] == 'W':
                cost -= 5
                w_ant -= 1
            else: 
                cost -= 10
                a_ant -= 1
            print(f'{main.head.value} ',end='')
            main.pop(0)
        print()
        if main.isEmpty() and cost>0:
            print('Ant nest has fallen!')
            break
        
    if i[0] == 'S':
        if w_ant > 0:
            print(f'-> Remaining worker ants: ',end='')
            cur = main.head
            while cur:
                if cur.value[0] == 'W':
                    print(cur.value, end=' ')
                cur = cur.next
            print()
        else: print('-> Remaining worker ants: Empty')
        if a_ant > 0:
            print(f'-> Remaining soldier ants: ',end='')
            cur = main.head
            while cur:
                if cur.value[0] == 'A':
                    print(cur.value, end=' ')
                cur = cur.next
            print()
        else: print('-> Remaining soldier ants: Empty')
        
    if i[0] == 'W' or i[0] == 'A':
        mode = None
        num = int(i[2:])
        count = 1
        another_count = 0
        if i[0] == 'A': 
            mode = 1
        if main.isEmpty():
            if mode:
                for ii in range(num):
                    main.append(f'A{ii+1}')
            else:
                for ii in range(num):
                    main.append(f'W{ii+1}')
        else:
            while another_count < num:
                count = 1
                while True:
                    if mode: test = f'A{count}'
                    else: test = f'W{count}'
                    found = False
                    cur = main.head
                    while cur:
                        if cur.value == test:
                            found = True
                            break
                        cur = cur.next
                    if not found:
                        break
                    count += 1
                main.append(test)
                another_count += 1
        if mode: a_ant += num
        else: w_ant += num
        main.size += num
        # print(main)
        
    if angy == 3:
        print('**The queen is furious! The ant colony has been destroyed**')
        break
# print(main)