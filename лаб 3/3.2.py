"""
DeepSeek имеет аккуратную архитектуру, понятные переменные, а также обработку ошибок
"""
from collections import deque


def find_cities_with_limited_transfers(filename, K, L):
    """
    Определяет города, в которые из города K можно долететь менее чем с L пересадками.

    Параметры:
    filename - имя файла с матрицей смежности
    K - номер начального города (нумерация с 1)
    L - максимальное количество пересадок (исключая прямые перелёты)

    Возвращает:
    список городов в порядке возрастания
    """
    try:
        with open(filename, 'r') as file:
            # Читаем количество городов
            n = int(file.readline().strip())

            # Читаем матрицу смежности
            matrix = []
            for _ in range(n):
                row = list(map(int, file.readline().split()))
                matrix.append(row)

            # Проверка корректности ввода
            if K < 1 or K > n:
                print(f"Ошибка: город {K} не существует (всего городов {n})")
                return [-1]

            # BFS для поиска всех городов с ограничением по пересадкам
            # Пересадки = количество рёбер - 1
            # Если L=0, то только прямые рейсы (1 перелёт, 0 пересадок)

            visited = [False] * n
            distance = [-1] * n  # количество перелётов от K

            # Индексация с 0 (город K-1)
            start = K - 1
            queue = deque()
            queue.append(start)
            visited[start] = True
            distance[start] = 0

            while queue:
                current = queue.popleft()

                # Если достигли предела пересадок, дальше не идём
                # distance[current] - количество перелётов от K
                # Количество пересадок = distance[current] - 1
                if distance[current] > L:
                    continue

                # Проверяем все возможные перелёты из текущего города
                for next_city in range(n):
                    if matrix[current][next_city] == 1 and not visited[next_city]:
                        visited[next_city] = True
                        distance[next_city] = distance[current] + 1
                        queue.append(next_city)

            # Собираем результат
            result = []
            for i in range(n):
                if i != start and distance[i] != -1:
                    # Количество пересадок = distance[i] - 1
                    if distance[i] - 1 < L:
                        result.append(i + 1)  # переводим в 1-нумерацию

            # Сортируем по возрастанию
            result.sort()

            # Если список пуст, возвращаем [-1]
            return result if result else [-1]

    except FileNotFoundError:
        print(f"Ошибка: файл '{filename}' не найден!")
        return [-1]
    except Exception as e:
        print(f"Ошибка при обработке файла: {e}")
        return [-1]


def main():
    # Ввод данных
    filename = input("Введите имя файла: ")

    try:
        with open(filename, 'r') as file:
            n = int(file.readline().strip())
            print(f"Количество городов: {n}")
    except:
        print("Ошибка при чтении файла!")
        return

    K = int(input(f"Введите номер города K (от 1 до {n}): "))
    L = int(input("Введите максимальное количество пересадок L: "))

    # Поиск городов
    result = find_cities_with_limited_transfers(filename, K, L)

    # Вывод результата
    if result == [-1]:
        print(-1)
    else:
        print("Города, в которые можно долететь менее чем с", L, "пересадками:")
        print(*result)


if __name__ == "__main__":
    main()
"""
DeepSeek
"""