"""File29. Дан файл целых чисел, содержащий более 50 элементов.
Уменьшить его размер до 50 элементов, удалив из файла
необходимое количество конечных элементов.
"""

import struct

FILENAME = 'numbers.bin'
MAX_ELEMENTS = 50


def read_numbers(filename: str) -> list[int]:
    """Читает целые числа из бинарного файла."""
    numbers = []
    with open(filename, 'rb') as f:
        while chunk := f.read(4):
            numbers.append(struct.unpack('i', chunk)[0])
    return numbers


def write_numbers(filename: str, numbers: list[int], limit: int) -> None:
    """Записывает целые числа в бинарный файл."""
    with open(filename, 'wb') as f:
        for num in numbers[:limit]:
            f.write(struct.pack('i', num))


def print_numbers(label: str, numbers: list[int]) -> None:
    """Выводит список чисел."""
    print(f'{label}:\n{", ".join(map(str, numbers))}\n')


def main() -> None:
    """Читает, уменьшает и сохраняет файл."""
    try:
        numbers = read_numbers(FILENAME)
        print_numbers('Файл до уменьшения', numbers)
        write_numbers(FILENAME, numbers, MAX_ELEMENTS)
        print_numbers('Файл после уменьшения', read_numbers(FILENAME))
    except FileNotFoundError:
        # Файл не найден
        print('Файл не найден')
    except (OSError, struct.error):
        # Ошибка чтения, записи или некорректный формат данных
        print('Неверный ввод')


if __name__ == '__main__':
    main()