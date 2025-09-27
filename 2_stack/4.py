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
 
print('*****Big leg on the right side*****')
user = input('Enter input: ')
user = [int(i) for i in user.split(' ')]
temp = Stack([])
count = 0
# print(f'Stack push 0 index of {user[0]}')
for i in range(len(user)-1):
    print(f'Stack push {count} index of {user[i]}')
    for ii in range(1, len(user)):
        if(user[ii] > user[i]):
            temp.push(user[ii])
            print(f'input[{ii}]({user[ii]}) is greater than input[top of stack]({i+1})')
            print('Stack pop')
            while temp.size() < len(user):
                temp.push(-1)
            print(f'Output: {temp.stack}')
            for iii in range(len(user)):
                if temp.peek() == -1:
                    temp.pop()
            break
    count += 1
while temp.size() < len(user):
                temp.push(-1)
print(f'Stack push {count} index of {user[-1]}')
print(f'Output: {temp.stack}')