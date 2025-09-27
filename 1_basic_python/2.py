print(' *** Wind classification ***')
user_input = input('Enter wind speed (km/h) : ')
km = float(user_input)
if km < 51.99 and km >= 0: state = 'Breeze'
elif km < 55.99: state = "Depression"
elif km < 101.99: state = "Tropical Storm"
elif km < 208.99: state = "Typhoon"
elif km > 208.99: state = "Super Typhoon"
print(f'Wind classification is {state}.')