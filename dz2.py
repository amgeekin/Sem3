"""
Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
"""

n = int(input('Введите количество элементов в массиве: '))
A = []
X = int(input('Введите X (число, близкий к которому элемент массива мы вычисляем): '))
for i in range(n):
    A.append(i+1)
print(f' Вот наш массив: {A}')
if (A.count(X)) >= 1:
    print(f' Элемент массива, ближайший по значению к числу X: {X}')
elif X > A[-1]:
    print(f' Элемент массива, ближайший по значению к числу X: {(A[-1])}')
else:
    print('Элемент массива, ближайший по значению к числу X: 0')
