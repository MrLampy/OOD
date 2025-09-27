def recur(num : int):
    if num < 2:
        return num
    return recur(num-1)+recur(num-2)

user_input = int(input('Enter Number : '))
print(f'fibo({user_input}) = {recur(user_input)}')