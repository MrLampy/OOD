class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.head, str(self.head.value) + " "
        while cur.next != None:
            s += str(cur.next.value) + " "
            cur = cur.next
        return s

    def isEmpty(self):
        return self.head == None

    def append(self, item):
        if self.isEmpty():
           self.head = Node(item)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(item)

    def addHead(self, item):
        if self.isEmpty():
           self.head = Node(item)
        else:
            temp = self.head
            self.head = Node(item)
            self.head.next = temp

    def search(self, item):
        if self.isEmpty(): return 'Not Found'
        cur = self.head
        while cur:
            if cur.value == item:
                return 'Found'
            cur = cur.next
        return 'Not Found'

    def index(self, item):
        cur = self.head
        index = 0
        if self.isEmpty(): return -1
        while cur:
            if cur.value == item:
                return index
            index += 1
            cur = cur.next
        return -1

    def size(self):
        cur = self.head
        if self.isEmpty(): return 0
        else: size = 1
        while cur.next:
            size+=1
            cur = cur.next
        return size

    def pop(self, pos):
        if pos < 0 or pos > self.size(): return 'Out of Range'
        if self.isEmpty(): return 'Out of Range'
        if pos == 0:
            self.head = self.head.next
            return 'Success'
        cur = self.head
        index = 0
        while cur.next:
            if index == pos:
                pre.next = cur.next
            index += 1
            pre = cur
            cur = cur.next
        return 'Success'

L = LinkedList()
inp = input('Enter Input : ').split(',')
for i in inp:
    if i[:2] == "AP":
        L.append(i[3:])
    elif i[:2] == "AH":
        L.addHead(i[3:])
    elif i[:2] == "SE":
        result = L.search(i[3:])
        print("{0} {1} in {2}".format(result, i[3:], L))
    elif i[:2] == "SI":
        print("Linked List size = {0} : {1}".format(L.size(), L))
    elif i[:2] == "ID":
        print("Index ({0}) = {1} : {2}".format(i[3:], L.index(i[3:]), L))
    elif i[:2] == "PO":
        before = "{}".format(L)
        k = L.pop(int(i[3:]))
        print(("{0} | {1}-> {2}".format(k, before, L)) if k == "Success" else ("{0} | {1}".format(k, L)))
print("Linked List :", L)