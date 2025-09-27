def fibo(num : int):
    if num < 2:
        return num
    return fibo(num-1)+fibo(num-2)

def find_total(level, weight):
    if level == 1: return weight
    ck = fibo(level - 1)
    total = weight*2 + 1 - ck
    if total < 2: return -1
    if total % 2 == 0:
        a = b = total/2
    else:
        a = total//2
        b = total - a
        
    return find_total(level - 1, a) + find_total(level - 1, b)

user_input = [int(i) for i in input('Purity and Weight needed: ').split(' ')]
result = find_total(user_input[0], user_input[1])
print(f"Total weight of used minerals with Purity 1 : {int(result)}")