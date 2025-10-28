class Data:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return "({0}, {1})".format(self.key, self.value)

class hash:
    def __init__(self, table_size, max):
        self.hash_table = self.assign_table_size(table_size)
        self.max_coll = max
        
    def assign_table_size(self, table_size : int):
        listA = []
        for _ in range(table_size):
            listA.append(None)
        return listA
        
    def ASCII_calculation(self, data : Data) -> int:
        key = data.key
        temp = [ord(i) for i in key]
        key = 0
        for i in temp:
            key += i
        return key
    
    def add_to_table(self, data : Data, i = 0):
        def quad(index, i):
                return (index+i**2) % len(self.hash_table)
        if i >= self.max_coll:
            print('Max of collisionChain')
            for i in range(len(self.hash_table)):
                print(f'#{i+1}	{self.hash_table[i]}')
            print('---------------------------')
            return
        key_value = self.ASCII_calculation(data)
        # print(f'Key :{data.key}')
        # print(f'ASCII :{key_value}')
        index = key_value % len(self.hash_table) if i == 0 else quad(key_value % len(self.hash_table), i)
        # print(f'index = {index}')
        if self.hash_table[index] == None:
            self.hash_table[index] = data
            for i in range(len(self.hash_table)):
                print(f'#{i+1}	{self.hash_table[i]}')
            print('---------------------------')
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
    
            
if __name__ == '__main__':
    user = input(' ***** Fun with hashing *****\nEnter Input : ').split('/')
    cmd, text = user[0].split(' '),user[1].split(',')
    text = [i.split(' ') for i in text]
    main = hash(int(cmd[0]),int(cmd[1]))
    for data in text:
        main.add_to_table(Data(data[0],data[1]))
            
            
        
        