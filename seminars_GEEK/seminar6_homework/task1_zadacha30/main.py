# Задача 30:  Заполните массив элементами арифметической прогрессии. Её первый элемент, 
# разность и количество элементов нужно ввести с клавиатуры. Формула для получения n-го члена 
# прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

first = int(input("Введиет первый член: "))
size = int(input("ВВедите количество элементов: "))
d = int(input("Введите разность(d): "))

arim_progr = []
for i in range (1, size+1):
    arim_progr.append(first + (i-1)*d)

print(arim_progr)