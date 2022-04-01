#Висилица
from random import choice
word_list = ["дом", "свет", "мир", "труд", "май", "радуга", "цветок", "земля", "любовь"]
comp_word = choice(word_list)
list_comp_word = []
for i in comp_word:
    list_comp_word.append(i)
hide_list_comp_word = []
for i in list_comp_word:
    hide_list_comp_word.append("*")
print("Копьютер загадал слово, попробуйте его угадать!")
live = 10
while live > 0:
    print(f"Загаданное слово: ")
    print(hide_list_comp_word)
    user_word = input("Введите букву! ")
    if user_word == "exit":
        break
    if user_word not in list_comp_word:
        live -= 1
    for i in list_comp_word:
        if i == user_word:
            print("Такая буква есть!!!")
            hide_list_comp_word[list_comp_word.index(i)] = i
    print(f"Оставшиеся жизни: {live}")
    if list_comp_word == hide_list_comp_word:
        print("Вы угадали! Игра окончена!")
        break
else:
    print(f"Вы проиграли, это было слово: {comp_word}")
