user_input = input('Enter All Bid : ')
user_input = [int(n) for n in user_input.split(" ")]
if(len(user_input) < 2): print('not enough bidder')
else: 
    user_input.sort()
    if user_input[-1] == user_input[-2]:
        print('error : have more than one highest bid')
    else:
        print(f"winner bid is {user_input[-1]} need to pay {user_input[-2]}")