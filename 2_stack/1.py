class Stack:
    def __init__(self, stack: list):
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

print('***Always 5 or 10***')
user_input = [int(i) for i in input('Enter Input : ').split(' ')]
my_list = Stack(user_input)
temp1 = Stack([])

if not my_list.isEmpty():
    temp1.push(my_list.pop())

while not my_list.isEmpty():
    top1 = my_list.peek()
    top2 = temp1.peek()

    if abs(top1 + top2) == 5 or abs(top1 + top2) == 10 or abs(top1 - top2) == 5 or abs(top1 - top2) == 10:
        temp1.push(my_list.pop())
    else:
        my_list.pop()

print('Output :', end=' ')
for i in reversed(temp1.stack):
    print(i, end=' ')
