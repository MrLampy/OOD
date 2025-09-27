def Rshift(num,shift):
   
    new = num >> shift
    return int(new)

n,s = input("Enter number and shiftcount : ").split()
print(Rshift(int(n),int(s)))
