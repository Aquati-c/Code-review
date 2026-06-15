"""
Условие задачи:
По заданной матрице смежности авиарейсов между городами определить все города,
в которые из начального города K можно долететь менее чем с L пересадками.
Вывести список номеров этих городов в порядке возрастания. Если таких городов
нет или произошла ошибка — вывести -1.
"""

from collections import deque
from typing import Optional


def find_cities_with_limited_transfers(
        matrix: list[list[int]],
        start_city: int,
        max_transfers: int
) -> list[int]:
    """Находит города, достижимые из start_city менее чем за max_transfers пересадок.

    Применяет алгоритм поиска в ширину (BFS) для определения кратчайшего
    количества перелетов. Количество пересадок равно (количество перелетов - 1).

    Args:
        matrix (list[list[int]]): Матрица смежности графа городов.
        start_city (int): Индекс начального города (нумерация с 0).
        max_transfers (int): Максимальное разрешенное количество пересадок.

    Returns:
        list[int]: Список номеров городов (с 1-нумерацией) по возрастанию.
    """
    n: int = len(matrix)
    visited: list[bool] = [False] * n
    distance: list[int] = [-1] * n

    queue: deque[int] = deque()
    queue.append(start_city)
    visited[start_city] = True
    distance[start_city] = 0

    while queue:
        current: int = queue.popleft()

        # Если количество пересадок (перелеты - 1) достигло предела,
        # дальше этой вершины граф не углубляем
        if distance[current] - 1 >= max_transfers:
            continue

        for next_city in range(n):
            if matrix[current][next_city] == 1 and not visited[next_city]:
                visited[next_city] = True
                distance[next_city] = distance[current] + 1
                queue.append(next_city)

    # Собираем города, где (перелеты - 1) < max_transfers
    result: list[int] = []
    for i in range(n):
        if i != start_city and distance[i] != -1:
            if distance[i] - 1 < max_transfers:
                result.append(i + 1)

    result.sort()
    return result


def load_matrix_from_file(filename: str) -> Optional[list[list[int]]]:
    """Считывает количество городов и матрицу смежности из текстового файла.

    Args:
        filename (str): Путь к файлу с данными.

    Returns:
        Optional[list[list[int]]]: Матрица смежности или None в случае ошибки.
    """
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            line: str = file.readline().strip()
            if not line:
                print("[Ошибка]: Файл пуст.")
                return None

            n: int = int(line)
            matrix: list[list[int]] = []

            for _ in range(n):
                row: list[int] = list(map(int, file.readline().split()))
                matrix.append(row)

            return matrix

    except FileNotFoundError:
        # Обязательный поясняющий комментарий по Google Style
        print(f"[Ошибка]: Файл '{filename}' не найден.")
        return None
    except ValueError:
        # Комментарий: обработка некорректного формата чисел в матрице
        print("[Ошибка]: Некорректный формат данных в файле.")
        return None


def main() -> None:
    """Управляет вводом-выводом и координирует работу компонентов программы."""
    print("=== Программа поиска маршрутов с ограничением пересадок ===")
    filename: str = input("Введите имя файла: ").strip()

    matrix: Optional[list[list[int]]] = load_matrix_from_file(filename)
    if matrix is None:
        print(-1)
        return

    n: int = len(matrix)
    if n == 0:
        print(-1)
        return

    try:
        k: int = int(input(f"Введите номер города K (от 1 до {n}): "))
        if k < 1 or k > n:
            print(f"[Ошибка]: Город {k} не существует.")
            print(-1)
            return

        l: int = int(input("Введите максимальное количество пересадок L: "))
        if l < 0:
            print("[Ошибка]: Количество пересадок не может быть отрицательным.")
            print(-1)
            return

    except ValueError:
        # Комментарий: перехват нечислового ввода параметров K или L
        print("[Ошибка]: Введены некорректные числовые параметры.")
        print(-1)
        return

    # Вычисление (Передаем k - 1 для перевода в 0-индексацию)
    result: list[int] = find_cities_with_limited_transfers(matrix, k - 1, l)

    if not result:
        print(-1)
        return

    print(f"Города, в которые можно долететь менее чем с {l} пересадками:")
    print(*result)


if __name__ == "__main__":
    main()