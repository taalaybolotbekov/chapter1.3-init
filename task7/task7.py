user = [1, 2, 6, 3, 9, 2, 11, 20, 16, 7, 8]
a = []
b = []
for i in user:
    if i % 2 == 0:
        a.append(i)
    else:
        b.append(i)
print('Четные числа: ', a, 'Нечетные числа: ', b)