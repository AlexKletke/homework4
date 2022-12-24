# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
n = int(input('enter the quantity of numbers: '))
list = list()
import random
for i in range(0,n):
    list.append(random.randint(0,5))
list.sort()
print('случайная последовательность чисел по возрастанию: ')
print(list)

UniqElements = set()
for y in range(0, len(list)):
    UniqElements.add(list[y])
print('список неповторяющихся элементов исходной последовательности: ')
print(*UniqElements)
