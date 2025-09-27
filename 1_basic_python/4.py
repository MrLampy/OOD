print('*** Fun with Drawing ***')
user_input = input('Enter input : ')
max = (int(user_input)*2-1)+int(user_input)*2-2
# print(max)
for i in range(1,max+1):
    for j in range(1,max+1):
        if i == 1 or j == 1 or i == max or j == max:print("#",end='')
        elif ((i%2 == 0 and (((i <= j and j<max-i+1) or i+j==max+1) or ((j+i>max+1) and i>=j)))): print('.',end='')
        elif (j%2 == 0 and max-j<i and i < (max//2)+2): print(".",end='')
        elif (j%2 == 0 and i<j and i > (max//2)+1): print(".",end='')
        elif (j%2 == 0 and i>j and i < (max//2)+2): print(".",end='')
        elif (j%2 == 0 and max+1-i>j and i > (max//2)+1): print(".",end='')
        else: print("#",end='')
    print()