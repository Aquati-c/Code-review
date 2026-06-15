"""
Лучшая читаемость кода, не происходит лишних выделений памяти, а так же список букв
создается один раз
Счетчик не учитывает последнее слово
"""
import random

# Ввод исходного слова
original_word = input("Введите слово: ").strip()

# Превращаем слово в список букв, так как строки в Python неизменяемы
letters = list(original_word)
attempts = 0

print("--- Начинаем перемешивание ---")

while True:
    # Перемешиваем буквы случайным образом
    random.shuffle(letters)

    # Собираем буквы обратно в строку
    current_word = "".join(letters)

    # Выводим текущий результат
    print(current_word)
    attempts += 1

    # Если слово совпало с исходным, выходим из цикла
    if current_word == original_word:
        break

print(f"Попыток: {attempts}")
"""
Gemini
"""