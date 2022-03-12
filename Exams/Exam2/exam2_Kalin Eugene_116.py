# 1. Дан список. Выведите те его элементы, которые встречаются в списке только один
# раз. Элементы нужно выводить в том порядке, в котором они встречаются в списке.

import random
a = [random.randint(0, 100) for i in range(10)]
print(a)
# или, например, a = [1, 2, 2, 4, 8, 6, 3, 9, 8, 7, 10, 7]
for i in range(len(a)):
    for j in range(len(a)):
        if i != j and a[i] == a[j]:
            break
    else:
        print(a[i], end=' ')

# 2. Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу.
# Считается, что любые два элемента, равные друг другу образуют одну пару,
# которую необходимо посчитать.

import random
a = [random.randint(0, 100) for i in range(10)]
print(a)
# или, например, a = [1, 2, 2, 4, 8, 6, 3, 9, 8, 7, 10, 7]
print(a)
par = 0
for i in range(len(a)):
    for j in range(i + 1, len(a)):
        if a[i] == a[j]:
            par += 1
print(par)

# 3. Даны два кортежа:
# C_1 = (35, 78, 21, 37, 2, 98, 6, 100, 231)
# C_2 = (45, 21, 124, 76, 5, 23, 91, 234)
# Необходимо определить:
# 1) Сумма элементов какого из кортежей больше и вывести соответствующее
# сообщение на экран (Сумма больше в кортеже - ..)
# 2) Вывести на экран порядковые номера минимальных и максимальных элементов
# этих кортежей

C_1 = (35, 78, 21, 37, 2, 98, 6, 100, 231)
C_2 = (45, 21, 124, 76, 5, 23, 91, 234)

sum_C_1 = sum(C_1)
sum_C_2 = sum(C_2)
print('Сумма C_1 - ', sum_C_1)
print('Сумма C_2 - ', sum_C_2)
if sum_C_1 > sum_C_2:
    print("Сумма больше в кортеже - C_1")
elif sum_C_1 < sum_C_2:
    print("Сумма больше в кортеже - C_2")
else:
    print("Суммы кортежей равны")
print('min C_1', min(C_1), 'Номер - ', C_1.index(min(C_1)))
print('min C_2', min(C_2), 'Номер - ', C_2.index(min(C_2)))
print('max C_1', max(C_1), 'Номер - ', C_1.index(max(C_1)))
print('max C_2', max(C_2), 'Номер - ', C_2.index(max(C_2)))

# 4. Создайте словарь из строки ' An apple a day keeps the doctor away' следующим
# образом: в качестве ключей возьмите символы строки, а значениями пусть будут
# числа, соответствующие количеству вхождений данной буквы в строку.

str0 = 'An apple a day keeps the doctor away'
str1 = str0.replace(" ", "")
print(str1)
my_dict = {i: str1.count(i) for i in str1}
print(my_dict)

# 6. Даны два списка чисел. Посчитайте, сколько чисел содержится одновременно как в
# первом списке, так и во втором.
import random
a = [random.randint(0, 100) for i in range(10)]
b = [random.randint(0, 100) for i in range(10)]
print(a)
print(b)
a1 = set(a)
b1 = set(b)
union = a1 & b1
print(union)
print(len(union))
# или )))
print(len(set(a) & set(b)))

# 7. Напишите программу, демонстрирующую работу try\except\finally
while True:
    a = input('Введите два число a ',)
    b = input('Введите два число b ',)

    try:
        result = int(a) / int(b)
    except ValueError:
        print("Вы ввели не числа")
    except ZeroDivisionError:
        print("Делить на ноль запрещено")
    else:
        print("Результат деления:", result)
        print("Конец.")
        break

# 8. В текстовый файл построчно записаны фамилия и имя учащихся класса и его
# оценка за контрольную. Вывести на экран всех учащихся, чья оценка меньше 3
# баллов и посчитать средний балл по классу

with open("123.txt", "r") as f:
    l = f.readlines()
sum_m = 0
for i in l:
    s = i.replace('\n', '').split('')
    if int(s[2]) < 3:
        print(s[0], s[1])
    sum_m += int(s[2])
print(sum_m / len(l))