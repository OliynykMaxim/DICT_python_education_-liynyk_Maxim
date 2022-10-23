import random
y_or_n = {'yes': True, 'no': False}

num = int(input("Enter the number of friends joining (including you):\n>"))
if num < 1:
    print('No one is joining for the party')
    exit()
payments = {}
print('Enter the name of every friend (including you), each on a new line:')
for _ in range(num):
    name = input(">")
    payments[name] = 0
price = int(input("Enter the total amount:\n>"))
print('Do you want to use "Who is lucky?" feature\n Type Yes/No')
lucky = y_or_n[input(">").lower()]
lucky_name = ''
if lucky:
    lucky_name = random.choice(list(payments.keys()))
    print(lucky_name, "is lucky today!")
else:
    print("No one is going to be lucky")
all_price = round(price / (num - int(lucky)), 2)
for p in payments.keys():
    payments[p] = all_price
if lucky:
    payments[lucky_name] = 0
print(payments)
