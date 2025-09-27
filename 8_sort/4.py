user = [i for i in input('Enter Input : ').split(' ')]
temp = []
ans = []
for i in range(len(user)):
    temp2 = list(user[i])
    while 1:
        if temp2[0].isdigit():
            temp2 = temp2[1:]
        else: break
    temp.append(temp2)
for i in range(len(temp)-1):
    for ii in range(len(temp)-1):
        if temp[ii][0] > temp[ii+1][0]:
            temp[ii],temp[ii+1] = temp[ii+1],temp[ii]
for i in temp:
    for ii in user:
        if i[0] in ii:
            ans.append(ii)
for i in ans: print(i,end=' ')