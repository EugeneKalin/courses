# 1. Дан список. Выведите те его элементы, которые встречаются в списке только
# один раз. Элементы нужно выводить в том порядке, в котором они встречаются в
# списке.
import random

rand_list = [random.randint(0, 9) for _ in range(20)]
print(rand_list)

# 1й способ
for number in rand_list:
    if rand_list.count(number) == 1:
        print(number, end=' ')


# 2. Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу.
# Считается, что любые два элемента, равные друг другу образуют одну пару,
# которую необходимо посчитать.
import random

rand_list = [random.randint(0, 9) for _ in range(10)]
print(rand_list)

# 1й способ
numbers_set = set(rand_list)

for number in numbers_set:
    print('{} имеет {} пар.'.format(number, rand_list.count(number) // 2))

print()
# 2й способ
already_checked_numbers = []
for number in rand_list:
    if rand_list.count(number) > 1 and number not in already_checked_numbers:
        print('{} имеет {} пар.'.format(number, rand_list.count(number) // 2))
        already_checked_numbers.append(number)


# 3. Даны два кортежа:
# C_1 = (35, 78,21,37, 2,98, 6, 100, 231)
# C_2 = (45, 21,124,76,5,23,91,234)
# Необходимо определить:
# 1) Сумма элементов какого из кортежей больше и вывести соответствующее
# сообщение на экран (Сумма больше в кортеже - ..)
# 2) Вывести на экран порядковые номера минимальных и максимальных элементов
# этих кортежей

C_1 = (35, 78, 21, 37, 2, 98, 6, 100, 231)
C_2 = (45, 21, 124, 76, 5, 23, 91, 234)

if sum(C_1) > sum(C_2):
    print('Сумма больше в кортеже - C_1')
else:
    print('Сумма больше в кортеже - C_2')


print('Для С_1 макс. число - {} и имеет индекс {}.'.format(
    max(C_1), C_1.index(max(C_1)))
)
print('Для С_1 мин. число - {} и имеет индекс {}.'.format(
    min(C_1), C_1.index(min(C_1)))
)
print('Для С_2 макс. число - {} и имеет индекс {}.'.format(
    max(C_2), C_2.index(max(C_2)))
)
print('Для С_2 мин. число - {} и имеет индекс {}.'.format(
    min(C_2), C_2.index(min(C_2)))
)


# 4. Создайте словарь из строки 'An apple a day keeps the doctor away' следующим
# образом: в качестве ключей возьмите буквы строки, а значениями пусть будут
# числа, соответствующие количеству вхождений данной буквы в строку.

st = 'An apple a day keeps the doctor away'

# 1й способ
keys_set = set(st)
keys_set.discard(' ')

st_dict = {}
for letter in keys_set:
    st_dict[letter] = st.count(letter)

print(st_dict)
# 2й способ
only_letters = [symbol for symbol in st if symbol.isalpha()]

st_dict = {}
for letter in only_letters:
    if letter not in st_dict:
        st_dict[letter] = st.count(letter)

print(st_dict)

# 3й способ
from collections import Counter

only_letters = [symbol for symbol in st if symbol.isalpha()]
st_dict = dict(Counter(''.join(only_letters)))
print(st_dict)

# 5. Клиент приходит в кондитерскую. Он хочет приобрести один или несколько видов
# продукции, а также узнать её состав.
# Реализуйте кондитерскую.
# У вас есть словарь, где ключ – название продукции (торт, пирожное, маффин и
# т.д.). Значение – список, который содержит состав, цену (за 100гр) и кол-во (в
# граммах).
# Предложите выбор:
# 1. Если человек хочет посмотреть описание: название – описание
# 2. Если человек хочет посмотреть цену: название – цена.
# 3. Если человек хочет посмотреть количество: название – количество.
# 4. Всю информацию.
# 5. Приступить к покупке:
# С клавиатуры вводите название торта и его кол-во. n – выход из программы.
# Посчитать цену выбранных товаров и сколько товаров осталось в изначальном
# списке
# 6. До свидания
import pprint

products = {
    'торт':
        [['тесто', 'шоколад', 'взбитые сливки', 'крем'], 3.0, 3000],
    'печенье':
        [['тесто', 'шоколад'], 2.0, 2000],
    'кекс':
        [['тесто', 'шоколад', 'изюм'], 1.0, 1500],
    'круассан':
        [['тесто', 'шоколад'], 1.5, 1000]
}

goods = {}

print('Добрый день, что Вы хотите?\n'
      'Введите 1. Если хотите посмотреть описание: название – описание\n'
      'Введите 2. Если хотите посмотреть цену: название – цена.\n'
      'Введите 3. Если хотите посмотреть количество: название – количество.\n'
      'Введите 4. Если хотите посмотреть всю информацию.\n'
      'Введите 5. Eсли хотите приступить к покупке:\n'
      'Введите 6 для выхода.')
while True:
    choice = input()
    if choice == '1':
        for product in products:
            print('{}. Состав: {}.'.format(
                product, ', '.join(products[product][0])
            ))
    elif choice == '2':
        for product in products:
            print('{}. Цена за 100 гр: {}.'.format(
                product, products[product][1]
            ))
    elif choice == '3':
        for product in products:
            print('{}. Количество в гр: {}.'.format(
                product, products[product][2]
            ))
    elif choice == '4':
        for product in products:
            print('{}. \n\tСостав: {}.'
                  '\n\tЦена за 100 гр: {}.'
                  '\n\tКоличество в гр: {}.\n'.format(
                product, ', '.join(products[product][0]),
                products[product][1], products[product][2]
            ))
    elif choice == '5':
        while True:
            print('Выберите товар:')
            for product in products.keys():
                print(product)

            print('n - выход.')

            prod_choice = input()
            prod_choice = prod_choice.lower()
            if prod_choice == 'n':
                break
            if prod_choice not in products:
                continue

            print('Сколько грамм?')
            while True:
                gramms = int(input())
                if gramms <= products[prod_choice][2]:
                    if prod_choice not in goods:
                        goods[prod_choice] = \
                            [products[prod_choice][1] * gramms / 100, gramms]
                        products[prod_choice][2] -= gramms
                        break
                    else:
                        goods[prod_choice][0] += \
                            products[prod_choice][1] * gramms / 100
                        goods[prod_choice][1] += gramms
                        products[prod_choice][2] -= gramms
                        break
                else:
                    print('У нас есть только {}г. Введите еще раз.'.format(
                        products[prod_choice][2])
                    )
                    continue

    elif choice == '6':
        break
    else:
        print('Вы ввели неверно, попробуйте еще раз.')

pprint.pprint(products)
pprint.pprint(goods)


# 6. Даны два списка чисел. Посчитайте, сколько чисел содержится одновременно как в
# первом списке, так и во втором.
import random


nums_1 = [random.randint(0, 9) for _ in range(10)]
nums_2 = [random.randint(0, 9) for _ in range(10)]
print(nums_1)
print(nums_2)

# 1й способ
print(len(set(nums_1) & set(nums_2)))

# 2й способ

numbers = []
for i in nums_1:
    if i in nums_2 and i not in numbers:
        numbers.append(i)
print(len(numbers))


# 7. Напишите программу, демонстрирующую работу try\except\finally

try:
    a = float(input('Enter a:'))
    b = float(input('Enter b:'))
    c = a / b
except ValueError:
    print('Only numbers allowed!!!')
except ZeroDivisionError as e:
    print(e)
except ArithmeticError as e:
    print(e)
else:
    print(c)
finally:
    print('Congratulations!')


# 8. В текстовый файл построчно записаны фамилия и имя учащихся класса и его
# оценка за контрольную. Вывести на экран всех учащихся, чья оценка меньше 3
# баллов и посчитать средний балл по классу

with open('file_kr2_teacher.txt', 'r') as stud_marks:
    stud_list = stud_marks.readlines()

students = []

for line in stud_list:
    students.append(line.replace('\n', '').split(' '))
print(students)

sum_marks = 0
for student in students:
    mark = int(student[2])
    if mark < 3:
        print(' '.join(student[:2]))
    sum_marks += mark

print('AVG =', sum_marks / len(students))


