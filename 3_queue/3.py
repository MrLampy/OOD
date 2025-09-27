class Queue:
    def __init__(self, init_list = []):
        self.queue = init_list
    
    def enqueue(self,data):
        self.queue.append(data)

    def isEmpty(self):
        return (len(self.queue) == 0)
    
    def size(self):
        return len(self.queue)
    
    def dequeue(self):
        if self.isEmpty(): return "Queue is empty"
        return self.queue.pop(0)
        
    def peek(self): #ใช้ดูตัวแรกของ Queue
        if self.isEmpty(): return "Queue is empty"
        return self.queue[0]
    
    # def __str__(self):
    #     return str(self.list)
    
print('*****Hot Potato Game*****')
user_input = input('Enter Input: ').split('/')
name = user_input[0].split(',')
num = int(user_input[1])
name = Queue(name)
temp = Queue([])
# print(name)
# print(num)
while name.size() > 1:
    temp.enqueue(name.dequeue())
    # if num == 0:
    #     print(f'{temp.peek()} is the first player holding the potato')
    #     break
    print(f'{temp.peek()} is the first player holding the potato')
    for i in range(num):
        name.enqueue(temp.dequeue())
        temp.enqueue(name.dequeue())
        print(f'  Potato passed to: {temp.peek()}')
    print(f'Eliminated: {temp.dequeue()}. Remaining players: {name.queue}')
print()
print(f'The winner is: {name.peek()}!')