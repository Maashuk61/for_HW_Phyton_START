#Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
#Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества.
#  Затем пользователь вводит сами элементы множеств.
n = int(input("Введите значение n "))
m = int(input("Введите значение m "))
set1 = set()
set2 = set()
for i in range(1, n+1):
    i = int(input())
    set1.add(i)
print(set1)
for i in range(1, m+1):
    i = int(input())
    set2.add(i)
print(set2)
inner = set1.intersection(set2)
print(inner)