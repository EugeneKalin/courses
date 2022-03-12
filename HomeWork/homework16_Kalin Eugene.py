def func(a):
    d = 0
    c = 0
    k = 0
    f = 0
    if type(a) is tuple:
        for i in a:
            e = len(i)
            k += e
        return f"Длина всех слов {k}"
    elif type(a) is list:
        for i in a:
            if type(i) is int:
                c += 1
            elif type(i) is str:
                d += 1
        return f"Количество чисел {c},Количество букв {d}"
    elif type(a) is int:
        for i in str(a):
            i = int(i)
            if i % 2 != 0:
                f += 1
        return f"Количество нечётных цифр {f}"
    elif type(a) is str:
        m = len(a)
        return f"Количество букв {m}"
print(func(("bye", "hello")))
print(func([123, "asd", 345]))
print(func(143))
print(func("bye"))