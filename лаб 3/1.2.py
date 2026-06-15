import random

# Ввод слова с клавиатуры
original_word = input("Введите слово: ")

# Преобразуем слово в список букв для удобства перестановки
word_list = list(original_word)
current_word = original_word
attempts = 0

print()  # Пустая строка для красоты

# Переставляем буквы, пока не получим исходное слово
while True:
    # Перемешиваем буквы случайным образом
    random.shuffle(word_list)
    current_word = ''.join(word_list)

    # Увеличиваем счётчик попыток
    attempts += 1

    # Выводим полученное слово
    print(current_word)

    # Если получили исходное слово - завершаем цикл
    if current_word == original_word:
        break

# Выводим результат
print(f"{attempts} попыток")
"""
DeepSeek
"""