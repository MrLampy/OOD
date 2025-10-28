class Data:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return "{0}".format(self.key)

class hash:
    def __init__(self, table_size, max, threshold):
        self.hash_table = self.assign_table_size(table_size)
        self.max_coll = max
        self.threshold = threshold
        self.data_count = 0
        self.is_restarting = False

    
    def assign_table_size(self, table_size : int, mode = 0):
        if mode == 1:
            listA = self.hash_table
            listA.extend([None for _ in range(table_size)])
            return listA
        listA = []
        for _ in range(table_size):
            listA.append(None)
        return listA
    
    def rehash(self):
        old_table = self.hash_table
        self.hash_table = self.assign_table_size(next_prime(len(old_table)*2))
        self.data_count = 0
        for data in old_table:
            if data is not None:
                key_value = int(data.value)
                index = key_value % len(self.hash_table)
                i = 0
                while self.hash_table[index] is not None:
                    i += 1
                    index = (key_value%len(self.hash_table)+ i**2)%len(self.hash_table)
                self.hash_table[index] = data
                self.data_count += 1
    
    def add_to_table(self, data : Data, i = 0):
        def quad(index, i):
                return (index+i**2) % len(self.hash_table)
            
        is_restarting_local = self.is_restarting
        self.is_restarting = False
        if i == 0 and not is_restarting_local: print(f'Add : {data.key}')
        percent = (self.data_count + 1)/len(self.hash_table)
        
        if percent > self.threshold/100:
            if i == 0: print('****** Data over threshold - Rehash !!! ******')
            self.data_count -= 1
            self.rehash()
            self.is_restarting = True
            self.add_to_table(data, 0)
            return
            
        key_value = int(data.value)

        if i >= self.max_coll:
            print('****** Max collision - Rehash !!! ******')
            self.data_count -= 1
            self.rehash()
            self.is_restarting = True
            self.add_to_table(data, 0)
            return

        index = key_value%len(self.hash_table) if i == 0 else (quad(key_value%len(self.hash_table), i))
        
        if self.hash_table[index] == None:
            self.hash_table[index] = data
            self.data_count += 1
            
            for ii in range(len(self.hash_table)):
                print(f'#{ii+1}\t{self.hash_table[ii]}')
            print('----------------------------------------')
        else:
            mode = 1
            for ii in self.hash_table:
                if ii == None:
                    mode = 0
                    break
            if mode == 0:
                print(f'collision number {i+1} at {index}')
                self.add_to_table(data, i + 1)
            else:
                print('This table is full !!!!!!')
                exit()
        

def next_prime(n):
    def is_prime(num):
        if num < 2:
            return False
        for ii in range(2, int(num ** 0.5) + 1):
            if num % ii == 0:
                return False
        return True

    candidate = n + 1
    while not is_prime(candidate):
        candidate += 1
    return candidate
    
    
if __name__ == '__main__':
    user = input(' ***** Rehashing *****\nEnter Input : ').split('/')
    cmd, text = user[0].split(' '),user[1].split(' ')
    main = hash(int(cmd[0]),int(cmd[1]),int(cmd[2]))
    print('Initial Table :')
    
    for i in range(len(main.hash_table)):
        print(f'#{i+1}\t{"None"}')
    print('----------------------------------------')
        
    for data in text:
        main.add_to_table(Data(data,data))