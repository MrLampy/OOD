def combination(num: list, answer: list):
    if not num: return [answer]
    temp = num[0]
    choose = combination(num[1:], answer + [temp])
    skip = combination(num[1:], answer)

    return choose + skip

user_input = input('Enter Input: ').split(' ')
user_input = [int(i) for i in user_input]
ans = combination(user_input, [])
print(f"Output: {ans[:-1]}")