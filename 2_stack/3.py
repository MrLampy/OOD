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
user_input = input('Enter input: ').split(' ')
main = Stack([])
temp = Stack([])
user_input = [int(i) for i in user_input]
ans = [-1 for i in user_input]
for index, value in enumerate(user_input, start=0):
    print(f'Stack push {index} index of {user_input[index]}')
    if value != user_input[-1]:
        if value < user_input[index+1]:
            print(f'input[{index+1}]({user_input[index+1]}) is greater than input[top of stack]({user_input[index]})')
            print('Stack pop')
            main.push(user_input[index+1])
            while main.size() < len(user_input):
                main.push(-1)
            print(f'Output: {main.stack}')
            ans = main.stack[:]
            for i in range(main.size()):
                if main.peek() == -1:
                    main.pop()
            temp.push(main.pop())
            if main.peek() != -1:
                main.push(temp.pop())
            num = index-1
            count = 2
            for i in range(len(user_input)):
                if main.peek() == -1:
                    main.pop()
                    # print(f'here we go ------------------------- {count}')
                    for ii in range(count):
                        main.push(temp.peek())
                    print(f'input[{index+1}]({user_input[index+1]}) is greater than input[top of stack]({user_input[num]})')
                    print('Stack pop')
                    num -=1
                    while main.size() < len(user_input):
                        main.push(-1)
                    print(f'Output: {main.stack}')
                    ans = main.stack[:]
                    for ii in range(main.size()):
                        if main.peek() == -1:
                            main.pop()
                    for ii in range(count):
                        main.pop()
                count += 1
            while(not temp.isEmpty()):
                temp.pop()
        else:
            main.push(-1)
print(f'Output: {ans}')