user = int(input('Введите первое число: '))
user1 = int(input('Введите второе число: '))
for i in range(user, user1):
    if i**2 < user1:
        print(i**2)