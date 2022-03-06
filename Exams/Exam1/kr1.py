# Дан список. Выведите те его элементы, которые встречаются в списке только один раз.
# Элементы нужно выводить в том порядке, в котором они встречаются в списке.
import random

t = tuple([random.randint(1,10) for _ in range (10)])
print(t)

for i in t:
    if t.count(i) == 1:
        print(i, end = ' ')

# Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу.
# Считается, что любые два элемента, равные друг другу образуют одну пару,
# которую необходимо посчитать.

t = tuple([random.randint(1,10) for _ in range(10)])
print(t)

couple = 0
l = []
for i in t:
    if t.count(i) >=2 and i not in l:
        couple += t.count(i) // 2
        print(i, t.count(i) // 2)
        l.append(i)
print(couple)