class Queue:
    def __init__(self):
        self.queue = []
    def size(self):
        return len(self.queue)
    def isEmpty(self):
        return self.size() == 0
    def enqueue(self, data):
        self.queue.append(data)
    def dequeue(self):
        if self.isEmpty(): return 'Queue is Empty'
        return self.queue.pop(0)
    def peek(self):
        if self.isEmpty(): return 'Queue is Empty'
        return self.queue[0]
    
print(' ***Queue of Queue of Queue of ...***')
user_input = input('Enter Input : ').split(",")
user_input = [i.strip().split(" ") for i in user_input]
compute = Queue()
for command in user_input:
    if command[0] == 'en':
        number = command[1]
        print(f'Enqueued: {number}')
        note = False
        for i in compute.queue:
            if not i.isEmpty() and i.peek()[0] == number[0]:
                i.enqueue(number)
                note = True
                break
        if not note:
            temp = Queue()
            temp.enqueue((number))
            compute.enqueue(temp)
    if command[0] == 'de':
        if compute.isEmpty(): 
            print('Queue is empty')
            continue
        print(f'Dequeued: {compute.queue[0].peek()}')
        compute.queue[0].dequeue()
    # อย่าลบเอาไว้ลบ list เปล่า
    if compute.queue[0].isEmpty():
        compute.dequeue()
    print("Queue state: [", end="")
    print(", ".join(["[" + ", ".join(q.queue) + "]" for q in compute.queue]), end="")
    print("]")
