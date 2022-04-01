#Лифт 10 этажей
from time import sleep
floor = 1
while True:
    next_floor = input(f"Лифт на {floor} этаже, введите этаж: ")
    if next_floor == "exit":
        break
    next_floor = int(next_floor)
    while floor != next_floor:
        if next_floor > floor:
            if floor > 9:
                break
            print(floor)
            floor += 1
            sleep(1)
        elif next_floor < floor:
            if floor < 2:
                break
            print(floor)
            floor -=1
            sleep(1)
#________________________________________________________________