class Stack:
    def __init__(self, stack):
        self.stack = stack[:]
    def isEmpty(self):
        return len(self.stack) == 0
    def size(self):
        return len(self.stack)
    def push(self, element):
        self.stack.append(element)
    def pop(self):
        if self.isEmpty(): return "Stack is empty"
        return self.stack.pop()
    def peek(self):
        if self.isEmpty(): return "Stack is empty"
        return self.stack[-1]

user_input = [float(i) for i in input('Enter needed weight(s): ').split()]
user_input = [int(n) if n == int(n) else n for n in user_input]
weights = list(reversed([1.25, 2.5, 5, 10, 15, 20, 25]))
bar_weight = 20
max = 5 
count = 0
main = Stack([])

for weight in user_input:
    forbidden = 0
    total = bar_weight
    pairs_used = 0
    for plate in weights:
        while (total + plate * 2) <= weight and pairs_used < max:
            total += plate * 2
            pairs_used += 1
    if total != weight: forbidden = 1
    if weight>270 or forbidden:
        print(f"It's impossible to achieve the weight you want({weight}).")
        break
    has = 0
    has_deci = None
    temp = Stack([])
    current_weight = bar_weight
    for i in weights:
        while (i*2 + current_weight) <= weight and temp.size() < max:
            temp.push(i)
            current_weight += i*2
    index = 0
    while index < min(len(main.stack), len(temp.stack)) and main.stack[index] == temp.stack[index]:
        index += 1
    for i in range(main.size() - 1, index - 1, -1):
        removed = main.pop()
        count -=1
        has = 1
        print(f"PO:{removed} ",end='')
    for i in range(index, len(temp.stack)):
        plate = temp.stack[i]
        main.push(plate)
        count +=1
        has = 1
        print(f"PU:{plate} ",end='')
    main = Stack(temp.stack)
    temp2 = Stack([])
    if current_weight == weight:
        if has == 1: print('=> ',end='')
        print(f"{'-'*(max-count)}",end='')
        while not temp.isEmpty():
            print(f'[{temp.peek()}]',end='')
            temp2.push(temp.pop())
        print('|======|',end='')
        while not temp2.isEmpty():
            print(f'[{temp2.peek()}]',end='')
            if type(temp2.peek()) == float:
                has_deci = 1
            temp2.pop()
        if has_deci: print(f"{'-'*(max-count)} => {float(weight)} KG.")
        else: print(f"{'-'*(max-count)} => {weight} KG.")
    