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

print('***Make a group***')
user_input = input('Enter input : ').split(', ')
user_input[0] = int(user_input[0])
user_input[1] = user_input[1].split(' ')
temp = Queue([])
real_temp = Queue([])
reject = Queue([])
has_blue = has_green = has_pink = has_red = has_yellow = False
count = 1
current_count = 0
index = -1
for round in user_input[1]:
  index += 1
  if round == 'Green': has_green = True
  if round == 'Blue': has_blue = True
  if round == 'Red': has_red = True
  if round == 'Pink': has_pink = True
  if round == 'Yellow': has_yellow = True
  if (has_pink and has_green and has_blue) or (has_yellow and has_blue and has_red):
    temp.enqueue(round)
    current_count += 1
  elif (has_pink and has_green) or (has_yellow and has_blue):
    reject.enqueue(round)
    has_blue = has_green = has_red = has_yellow = has_pink = False
    while not temp.isEmpty():
      if temp.peek() == 'Blue': has_blue = True
      if temp.peek() == 'Red': has_red = True
      if temp.peek() == 'Yellow': has_yellow = True
      if temp.peek() == 'Pink': has_pink = True
      if temp.peek() == 'Green': has_green = True
      real_temp.enqueue(temp.dequeue())
    while not real_temp.isEmpty():
      temp.enqueue(real_temp.dequeue())
    continue
  else:
    temp.enqueue(round)
    current_count += 1

  if current_count == user_input[0]:
    print(f"Group {count} : {', '.join(map(str, temp.queue))}")
    while not temp.isEmpty():
      temp.dequeue()
    count +=1
    current_count = 0
    has_blue = has_green = has_red = has_yellow = has_pink = False
      
while not temp.isEmpty():
    reject.enqueue(temp.dequeue())

if not reject.isEmpty():
  print(f"Rejected : {', '.join(map(str, reject.queue))}")
else:
    print('Rejected : None')
# print(user_input)