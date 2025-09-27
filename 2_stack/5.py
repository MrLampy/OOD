class Stack:
    def __init__(self, stack : list):
        self.stack = stack[:]
    def size(self):
        return len(self.stack)
    def pop(self):
        if (self.size() == 0): return 'The Stack is Empty'
        return self.stack.pop()
    def peek(self):
        if (self.size() == 0): return 'The Stack is Empty'
        return self.stack[-1]
    def push(self, obj):
        self.stack.append(obj)
    def isEmpty(self):
        return len(self.stack) == 0
    
user_input = input("Enter Input : ").split(",")
user_input = [i.split(" ") for i in user_input]
# print(user_input)
main = Stack([])
temp = Stack([])
for tree in user_input:
    if tree[0] == 'A':
        if tree[1] != '0':
            main.push(int(tree[1]))
    if tree[0] == 'B':
        main2 = Stack(main.stack)
        while not main.isEmpty():
            if temp.isEmpty() or temp.peek() < main.peek():
                temp.push(main.peek())
            main.pop()
        print(temp.size())
        main = Stack(main2.stack)
        while not temp.isEmpty():
            temp.pop()
        while not main2.isEmpty():
            main2.pop()
    if tree[0] == 'S':
        main2 = Stack([])
        while not main.isEmpty():
            # print(main.peek())
            if main.peek()%2 == 0:
                main2.push(main.pop()-1)
            else:
                main2.push(main.pop()+2)
        while not main2.isEmpty():
            main.push(main2.pop())