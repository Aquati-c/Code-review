"""File52. Дана строка S0, целое число N (≤ 4) и N файлов целых чисел.
Объединить содержимое в файле-архиве S0:
N, размеры каждого файла, затем данные всех файлов.
"""

import os

MAX_FILES = 4


def read_numbers(filename: str) -> list[int]:
    """Читает целые числа из файла."""
    with open(filename, 'r', encoding='utf-8') as f:
        return [int(line.strip()) for line in f]


def create_archive(archive_name: str, file_names: list[str]) -> None:
    """Создаёт архив из указанных файлов."""
    n = len(file_names)
    if n > MAX_FILES:
        raise ValueError('Количество файлов не должно быть больше 4')

    file_sizes = []
    data = []
    for name in file_names:
        numbers = read_numbers(name)
        file_sizes.append(len(numbers))
        data.extend(numbers)

    with open(archive_name, 'w', encoding='utf-8') as f:
        f.write(f'{n}\n')
        for size in file_sizes:
            f.write(f'{size}\n')
        for number in data:
            f.write(f'{number}\n')

    print(f'Архив-файл {archive_name} успешно создан')


def all_files_exist(file_names: list[str]) -> bool:
    """Проверяет, существуют ли все файлы."""
    return all(os.path.exists(name) for name in file_names)


def get_file_names() -> list[str]:
    """Запрашивает у пользователя имена исходных файлов."""
    file_names = []
    i = 1
    while True:
        name = input(f'Введите название файла {i} (или "q" для завершения): ')
        if name.lower() == 'q':
            print(f'Вы успешно записали файлы в количестве {i - 1} штук')
            break
        if len(file_names) >= MAX_FILES:
            print('Количество файлов не должно быть больше 4')
            continue
        file_names.append(name)
        i += 1
    return file_names


def main() -> None:
    """Главная функция программы."""
    try:
        archive_name = input('Введите название файла-архива: ')
        file_names = get_file_names()

        if not file_names:
            print('Не указано ни одного файла')
            return

        if not all_files_exist(file_names):
            print('Не все файлы существуют. Создание архива отменено.')
            return

        create_archive(archive_name, file_names)
    except ValueError:
        # Некорректные данные в файле
        print('Неверный ввод')
    except OSError as e:
        # Ошибка чтения или записи файла
        print(f'Ошибка работы с файлом: {e}')


if __name__ == '__main__':
    main()