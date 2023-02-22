#Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок, 
# если известно, что Петя и Сережа сделали одинаковое количество журавликов, а Катя сделала в два раза больше журавликов, 
# чем Петя и Сережа вместе?

#*Пример:*

#6 -> 1  4  1
#24 -> 4  16  4
#    60 -> 10  40  10"""

s = int (input("Введите количество всех сделанных журавликов: "))
if s%2 !=0:
    print ("Согласно условиям задачи, кол-во журавликов должно быть четное. Пожалуйста, перезапустите программу.")
else:
    print (f"Петя сделал {s // 4} журавликов")
    print (f"Cережа сделал {s // 4} журавликов")
    print (f"Катя сделала {s // 2} журавликов")

