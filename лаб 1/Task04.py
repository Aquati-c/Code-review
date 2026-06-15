"""Сведения о клиентах фитнес-центра.
Для клиента K по каждому году найти месяц с наибольшей
продолжительностью занятий (при равенстве — меньший номер месяца).
Вывод: год, месяц, продолжительность по убыванию года.
"""

import os
import struct

FILENAME = 'clients.bin'
RECORD_SIZE = 5


class FitnessClient:
    """Хранит и обрабатывает записи о занятиях клиента."""

    def __init__(self, client_code: int) -> None:
        self.client_code = client_code
        self.records: dict[int, dict[int, int]] = {}

    def add_record(self, duration: int, year: int, month: int) -> None:
        """Добавляет продолжительность занятий за месяц."""
        if year not in self.records:
            self.records[year] = {}
        self.records[year][month] = self.records[year].get(month, 0) + duration

    def get_max_duration_per_year(self) -> list[tuple[int, int, int]]:
        """Возвращает год, месяц и макс. продолжительность по годам."""
        result = []
        for year in sorted(self.records, reverse=True):
            max_duration = 0
            best_month = 0
            for month in sorted(self.records[year]):
                if self.records[year][month] > max_duration:
                    max_duration = self.records[year][month]
                    best_month = month
            result.append((year, best_month, max_duration))
        return result


def read_binary_file(filename: str) -> bytes:
    """Читает бинарный файл."""
    with open(filename, 'rb') as f:
        return f.read()


def parse_binary_data(data: bytes, client_code: int) -> FitnessClient:
    """Разбирает бинарные данные и фильтрует записи клиента."""
    client = FitnessClient(client_code)
    for i in range(0, len(data), RECORD_SIZE):
        record = data[i:i + RECORD_SIZE]
        if len(record) < RECORD_SIZE:
            continue
        duration, year, month, code = struct.unpack('>BHBb', record)
        if code == client_code:
            client.add_record(duration, year, month)
    return client


def main() -> None:
    """Главная функция программы."""
    try:
        os.chdir(os.path.dirname(os.path.abspath(__file__)))
        client_code = int(input('Введите код клиента: '))

        data = read_binary_file(FILENAME)
        client = parse_binary_data(data, client_code)
        results = client.get_max_duration_per_year()

        if not results:
            print('Нет данных')
            return

        for year, month, duration in results:
            print(f'{year} {month} {duration}')
    except ValueError:
        # Некорректный код клиента
        print('Неверный ввод')
    except FileNotFoundError:
        # Файл с данными не найден
        print(f'Ошибка: файл {FILENAME} не найден')
    except OSError as e:
        # Ошибка чтения файла
        print(f'Ошибка работы с файлом: {e}')


if __name__ == '__main__':
    main()