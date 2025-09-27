user_input = int(input('Enter year : '))

def hbd(n):
    for i in range(2):
        if(i == 1):
            base = (n - 1) // 2
            if base >= 2 and 2*base + 1 == n:
                return f"saimai is just 21, in base {base}!"
        else:
            base = n // 2
            if base >= 2 and 2* base == n:
                return f"saimai is just 20, in base {base}!"
            
print(hbd(user_input))