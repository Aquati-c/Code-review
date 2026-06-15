from collections import deque
import os


def find_reachable_cities(filename, k, l):
    # Проверяем существование файла
    if not os.path.exists(filename):
        print(f"Файл {filename} не найден.")
        return

    # 1. Чтение данных из файла
    with open(filename, 'r') as f:
        lines = f.read().splitlines()

    if not lines:
        print("Файл пуст.")
        return

    # Количество городов
    n = int(lines[0].strip())

    # Считываем матрицу смежности
    matrix = []
    for i in range(1, n + 1):
        matrix.append(list(map(int, lines[i].split())))

    # Приводим номер стартового города к индексам Python (от 0 до n-1)
    start_city = k - 1

    # Словарик/массив для хранения минимального количества перелетов до каждого города
    # По умолчанию ставим -1 (город недостижим)
    distances = [-1] * n
    distances[start_city] = 0  # До самого себя лететь не нужно

    # 2. Алгоритм BFS (Поиск в ширину)
    queue = deque([start_city])

    while queue:
        current = queue.popleft()

        # Проверяем всех соседей текущего города
        for neighbor in range(n):
            # Если есть рейс и в этом городе мы еще не были
            if matrix[current][neighbor] == 1 and distances[neighbor] == -1:
                distances[neighbor] = distances[current] + 1
                queue.append(neighbor)

    # 3. Фильтрация городов по условию задачи
    # Максимально допустимое количество перелетов = L (что соответствует < L пересадкам)
    result_cities = []

    for i in range(n):
        # Сам стартовый город K исключаем из списка (в условии "долететь в города")
        if i == start_city:
            continue

        # Если город достижим и количество перелетов <= L
        if distances[i] != -1 and distances[i] <= l:
            result_cities.append(i + 1)  # Возвращаем нумерацию с 1

    # 4. Вывод результата
    if result_cities:
        # Сортируем по возрастанию (они и так идут по порядку, но для надежности)
        result_cities.sort()
        print(" ".join(map(str, result_cities)))
    else:
        print(-1)


# --- Пример использования ---
# Создадим тестовый файл "routes.txt"
# 4 города. Граф: 1 -> 2 -> 3 -> 4
# Из города 1 в город 3 можно попасть за 2 перелета (1 пересадка)
with open("routes.txt", "w") as f:
    f.write("4\n")
    f.write("0 1 0 0\n")
    f.write("0 0 1 0\n")
    f.write("0 0 0 1\n")
    f.write("0 0 0 0\n")

# Ищем из города K=1, менее чем с L=2 пересадками (то есть <= 2 перелетов)
# Должны подойти города 2 (1 перелет, 0 пересадок) и 3 (2 перелета, 1 пересадка)
find_reachable_cities("routes.txt", k=1, l=2)
"""
Gemini
"""