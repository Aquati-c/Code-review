import random

word = input("Введите слово: ")

count = 0

while True:
    letters = list(word)
    random.shuffle(letters)

    new_word = "".join(letters)

    print(new_word)

    if new_word == word:
        break

    count += 1

print(count, "попыток")
"""
ChatGPT
"""
