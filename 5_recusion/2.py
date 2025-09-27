def palin(text):
    if len(text) == 0: return True
    if text[0] == text[-1]:
        text = text[1:-1]
        return palin(text)
    return False

print('**Palindrome pretty version!**') 
user_input = (input('Enter message : '))
user_input = ''.join(ch.lower() for ch in user_input if ch.isalnum())
print(palin(user_input))