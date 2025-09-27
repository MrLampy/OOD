class Queue:
  def __init__(self, queue):
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

user = input('Enter Input : ')
user = [i.split(' ') for i in user.split(',')]
# print(user)
index = 0
index_run = 0
user = Queue(user)
ans = Queue([])
size = 0
for i in range(len(user.queue)):
    if len(user.queue[i]) == 2:
        ans.enqueue(user.queue[i][1])
        print(f'Add {user.queue[i][1]} index is {index_run}')
        index_run += 1
        size = ans.size()
    else:
        if size > 0:
            # print(ans.queue)
            # print(index)
            print(f'Pop {ans.queue[0]} size in queue is {size-1}')
            ans.dequeue()
            size = ans.size()
            index_run -=1
        else:
            print(-1)
    
if ans.isEmpty(): print(f'Empty') 
else: print(f'Number in Queue is :  {ans.queue}')