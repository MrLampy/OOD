user = [int(i) for i in input('Enter Input : ').split(' ')]
original = user[:]
for i in range(len(user)-1):
    for ii in range(len(user)-1):
        if user[ii] > user[ii+1]:
            user[ii],user[ii+1] = user[ii+1],user[ii]
print('Yes' if original == user else "No")