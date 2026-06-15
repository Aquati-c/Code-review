"""
Условие задачи:
Программа принимает от пользователя слово, после чего случайным образом
перемешивает его буквы в цикле и выводит каждую итерацию на экран.
Цикл завершается, когда полученное слово вновь совпадет с исходным.
В конце выводится общее количество сделанных попыток.
"""

import random


def shuffle_until_original(original_word: str) -> int:
    """Перемешивает буквы слова до тех пор, пока оно не совпадет с исходным.

    Args:
        original_word (str): Исходное слово для перемешивания.

    Returns:
        int: Общее количество итераций (попыток) до совпадения.
    """
    letters: list[str] = list(original_word)
    attempts: int = 0

    while True:
        random.shuffle(letters)
        current_word: str = "".join(letters)

        # Вывод промежуточного состояния (допускается внутри алгоритма по условию)
        print(current_word)
        attempts += 1

        if current_word == original_word:
            return attempts


def main() -> None:
    """Управляет дружественным интерфейсом и вводом пользователя."""
    print("=== Программа регенерации слова ===")
    original_word: str = input("Введите слово: ").strip()

    # Защита от некорректного ввода (Локальное требование №2)
    if not original_word:
        print("[Ошибка ввода]: Слово не может быть пустым!")
        return

    if len(original_word) < 2:
        print("[Ошибка ввода]: Слово должно состоять минимум из 2-х букв!")
        return

    print("--- Начинаем перемешивание ---")
    total_attempts: int = shuffle_until_original(original_word)
    print(f"Попыток: {total_attempts}")


if __name__ == "__main__":
    main()