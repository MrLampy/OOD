user = [i for i in input('Enter list  of numbers: ').split(' ')]
data = {}
for i in user:
    if i not in data:
        data.update({i:1})
    else:
        data[i] += 1
data = list(data.items())
# print(data)
for i in range(len(data)-1):
    for ii in range(len(data)-1):
        if data[ii][1] < data[ii+1][1]:
            data[ii], data[ii+1] = data[ii+1], data[ii]
for i, j in data:
    print(f'number {i}, total: {j}')
# print(data)