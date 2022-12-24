# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
n = int(input('enter the natural number: '))
print('список простых множителей числа N: ')
list =list()
i = 2
while n > 1:
    if n % i == 0:
        list.append(i)
        n = n/i
    else:
        i = i + 1

print(*list)

