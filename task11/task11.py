a = b = 1
user = int(input('Введите число : '))
for i in range(2, user+1):
    a, b = b, a + b
    if i < 2:
        break
    print(b)