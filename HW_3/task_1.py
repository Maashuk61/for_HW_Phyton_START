"""Задача 16: Требуется вычислить, сколько раз встречается некоторое
число X в массиве A[1..N]. Пользователь в первой строке вводит
натуральное число N – количество элементов в массиве. В последующих
строках записаны N целых чисел Ai
. Последняя строка содержит число X"""

import random
n = int(input("Введите какое количество элементов будет в массиве:"))
A = 1
B = 10
Array = [random.randint(A, B) for _ in range(n)]
print(Array)
x = int(input("Введите число, которое будет подсчитано сколько раз встречается в массиве:"))
count = 0
for i in Array:
    if i == x:
        count += 1 
print(count)
