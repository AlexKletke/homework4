# Пользователь вводит число, нужно вывести чило pi с заданной точностью(БЕЗ БИБЛИОТЕК/МОДУЛЕЙ)
n = int(input('enter the number of numbers after the decimal point: '))
# k = float(0) не нужно
# Pi1 = float((1/(16 **k)) * (4/(8*k + 1) - (2/(8*k + 4)) - (1/(8*k + 5)) - (1/(8*k + 6))))  не нужно
Pi = float(0)
for k in range (0, 1000):
    Pi = Pi + float((1/(16 **k)) * (4/(8*k + 1) - (2/(8*k + 4)) - (1/(8*k + 5)) - (1/(8*k + 6))))

print(float(round(Pi, n)))
# print(round(Pi1, n)) проверка

