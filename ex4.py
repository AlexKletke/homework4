# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
PolynomialInDegree_k = open('file_with_polynomial.txt', 'w')
k = int(input('введи степень многочлена: '))
PolynomialInDegree_k.writelines(f"degree of the polynomial = {k}\n")
import random
a = int()
a = random.randint(0, 10)
if a == 0:
    Polynomial = ''
else:
    if a == 1:
        Polynomial =  f'x^{k}'
    else:
        Polynomial =  f'{a}*x^{k}'
for i in range(k-1, 1, -1):
    a = random.randint(0, 10)
    if a == 0:
        Polynomial = Polynomial + ''
    else:
        if Polynomial =='':
            if a == 1:
                Polynomial = Polynomial + f'x^{i}'
            else:
                Polynomial = Polynomial + f'{a}*x^{i}'
        else:
            if a == 1:
                Polynomial = Polynomial + f' + x^{i}'
            else:
                Polynomial = Polynomial + f' + {a}*x^{i}'
a = random.randint(0, 10)
if a == 0:
    Polynomial = ''
else:
    if a == 1:
        Polynomial = Polynomial + f' + x'
    else:
        Polynomial = Polynomial + f' + {a}*x'
a = random.randint(0, 10)
if a == 0:
    Polynomial = Polynomial + ' = 0'
else:
    if Polynomial =='':
        Polynomial = 'все коэффициенты равны 0'
    else:
        Polynomial = Polynomial + f' + {a} = 0'

print(Polynomial)
PolynomialInDegree_k.writelines(f"Polynomial in degree {k}: \n")
PolynomialInDegree_k.writelines(f'{Polynomial}\n')
