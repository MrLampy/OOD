class Node:
    instances = []
    def __init__(self, data):
       self.data = data
       self.left = None
       self.right = None
       self.check = 0
       Node.instances.append(self)
    
def rerun():
    for instance in Node.instances:
        if instance.check != 2:
            instance.check = 0
            
class BST:
    def __init__(self):
        self.root = None
        
    def insert(self, data):
        new_Node = Node(data)
        if not self.root:
            self.root = new_Node
            return
        target = self.root
        while(1):
            if data >= target.data:
                if target.right:
                    target = target.right
                else:
                    target.right = new_Node
                    return
            if data < target.data:
                if target.left:
                    target = target.left
                else:
                    target.left = new_Node
                    return
                
    def print_tree(self, root, level = 0):
        if root:
            self.print_tree(root.right, level+1)
            if root.check != 2:
                print('     '*level,root.data,end='')
                print()
                # print(f'({root.check})')
            self.print_tree(root.left, level+1)
    
def print_arrow_sum(Alist: list):
    ans = 0
    for i in Alist[:-1]:
        print(i, end='->')
        ans += i
    ans += Alist[-1]
    print(f'{Alist[-1]} = {ans}')

def print_dot():
    print('--------------------------------------------------')
        
if __name__ == '__main__':
    main = BST()
    user, cmd = input('Enter <Create City A (BST)>/<Create conditions and deploy the army>: ').split('/')
    user = [int(i) for i in user.split(' ')]
    cmd = cmd.split(',')
    for i in user:
        main.insert(i)
    print('(City A) Before the war:')
    main.print_tree(main.root)
    # print(cmd)
    for ii in cmd:
        num = ii.split(' ')
        num = int(num[1])
        # print(ii[0])
        
        if ii[0] == 'L':
            print_dot()
            print(f'Removing paths where the sum is less than {num}:')
            run = 1
            Alist = []
            count = 0
            cur = main.root
            while(not main.root.check):
                if cur:
                    count += cur.data
                    Alist.append(cur.data)
                    if cur.left and cur.left.check == 0: cur = cur.left
                    elif cur.right and cur.right.check == 0: cur = cur.right
                    elif cur.left and cur.right and cur.left.check + cur.right.check > 3:
                        if count < num:
                            print(f'{run}) ',end='')
                            print_arrow_sum(Alist)
                            run += 1
                            cur.check = 2
                        else: 
                            cur.check = 1
                        Alist = []
                        cur = main.root
                        count = 0
                    elif cur.left and not cur.right and cur.left.check == 2:
                        if count < num:
                            print(f'{run}) ',end='')
                            print_arrow_sum(Alist)
                            run += 1
                            cur.check = 2
                        else: 
                            cur.check = 1
                        Alist = []
                        cur = main.root
                        count = 0
                    elif cur.right and not cur.left and cur.right.check == 2:
                        if count < num:
                            print(f'{run}) ',end='')
                            print_arrow_sum(Alist)
                            run += 1
                            cur.check = 2
                        else: 
                            cur.check = 1
                        Alist = []
                        cur = main.root
                        count = 0
                    elif cur.left and cur.left.check:
                        if cur.left.check:
                            cur.check = 1
                            cur = main.root
                            count = 0
                            Alist = []
                    elif cur.right and cur.right.check:
                        if cur.right.check: 
                            cur.check = 1
                            cur = main.root
                            count = 0
                            Alist = []
                    else:
                        if count < num:
                            print(f'{run}) ',end='')
                            print_arrow_sum(Alist)
                            run += 1
                            cur.check = 2
                        else: 
                            cur.check = 1
                        Alist = []
                        cur = main.root
                        count = 0
            if run == 1: print('No paths were removed.')
            
        if ii[0] == 'E':
            print_dot()
            print(f'Removing paths where the sum is equal to {num}:')
            run = 1
            Alist = []
            count = 0
            cur = main.root
            while(not main.root.check):
                if cur:
                    count += cur.data
                    Alist.append(cur.data)
                    if cur.left and cur.left.check == 0: cur = cur.left
                    elif cur.right and cur.right.check == 0: cur = cur.right
                    elif cur.left and cur.right and cur.left.check + cur.right.check > 3:
                        if count == num:
                            print(f'{run}) ',end='')
                            print_arrow_sum(Alist)
                            run += 1
                            cur.check = 2
                        else: 
                            cur.check = 1
                        Alist = []
                        cur = main.root
                        count = 0
                    elif cur.left and not cur.right and cur.left.check == 2:
                        if count == num:
                            print(f'{run}) ',end='')
                            print_arrow_sum(Alist)
                            run += 1
                            cur.check = 2
                        else: 
                            cur.check = 1
                        Alist = []
                        cur = main.root
                        count = 0
                    elif cur.right and not cur.left and cur.right.check == 2:
                        if count == num:
                            print(f'{run}) ',end='')
                            print_arrow_sum(Alist)
                            run += 1
                            cur.check = 2
                        else: 
                            cur.check = 1
                        Alist = []
                        cur = main.root
                        count = 0
                    elif cur.left and cur.left.check:
                        if cur.left.check:
                            cur.check = 1
                            cur = main.root
                            count = 0
                            Alist = []
                    elif cur.right and cur.right.check:
                        if cur.right.check: 
                            cur.check = 1
                            cur = main.root
                            count = 0
                            Alist = []
                    else:
                        if count == num:
                            print(f'{run}) ',end='')
                            print_arrow_sum(Alist)
                            run += 1
                            cur.check = 2
                        else: 
                            cur.check = 1
                        Alist = []
                        cur = main.root
                        count = 0
            if run == 1: print('No paths were removed.')

        if ii[0] == 'M':
            print_dot()
            print(f'Removing paths where the sum is greater than {num}:')
            run = 1
            Alist = []
            count = 0
            cur = main.root
            while(not main.root.check):
                if cur:
                    count += cur.data
                    Alist.append(cur.data)
                    if cur.left and cur.left.check == 0: cur = cur.left
                    elif cur.right and cur.right.check == 0: cur = cur.right
                    elif cur.left and cur.right and cur.left.check + cur.right.check > 3:
                        if count > num:
                            print(f'{run}) ',end='')
                            print_arrow_sum(Alist)
                            run += 1
                            cur.check = 2
                        else: 
                            cur.check = 1
                        Alist = []
                        cur = main.root
                        count = 0
                    elif cur.left and not cur.right and cur.left.check == 2:
                        if count > num:
                            print(f'{run}) ',end='')
                            print_arrow_sum(Alist)
                            run += 1
                            cur.check = 2
                        else: 
                            cur.check = 1
                        Alist = []
                        cur = main.root
                        count = 0
                    elif cur.right and not cur.left and cur.right.check == 2:
                        if count > num:
                            print(f'{run}) ',end='')
                            print_arrow_sum(Alist)
                            run += 1
                            cur.check = 2
                        else: 
                            cur.check = 1
                        Alist = []
                        cur = main.root
                        count = 0
                    elif cur.left and cur.left.check:
                        if cur.left.check:
                            cur.check = 1
                            cur = main.root
                            count = 0
                            Alist = []
                    elif cur.right and cur.right.check:
                        if cur.right.check: 
                            cur.check = 1
                            cur = main.root
                            count = 0
                            Alist = []
                    else:
                        if count > num:
                            print(f'{run}) ',end='')
                            print_arrow_sum(Alist)
                            run += 1
                            cur.check = 2
                        else: 
                            cur.check = 1
                        Alist = []
                        cur = main.root
                        count = 0
            if run == 1: print('No paths were removed.')
       
        print_dot()
        print('(City A) After the war:')
        rerun()
        main.print_tree(main.root)
        if main.root.check == 2:
            print('City A has fallen!')
            exit()