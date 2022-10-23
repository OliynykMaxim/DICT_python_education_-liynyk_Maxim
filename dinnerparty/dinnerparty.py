num = int(input("Enter the number of friends joining (including you):\n>"))
if num < 1:
    print('No one is joining for the party')
    exit()
payments = {}
print('Enter the name of every friend (including you), each on a new line:')
for _ in range(num):
    name = input(">")
    payments[name] = 0
print(payments)