age = int(input('Enter your age: '))
balance = int(input('Enter your bank balance: '))


def bouncer(age, balance):
    if age < 18 or balance < 100:
        return print('Go home')
    else:
        return print("Welcome")


result = bouncer(age, balance)
print(result)
