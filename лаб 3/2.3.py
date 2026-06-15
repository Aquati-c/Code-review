"""
Отличная архитектура, легко читается, полностью соответствует структуре,
Каждая функция отвечает за свою задачу,
но используются повторные вычисления поддеревьев
"""
import os

# Константы для кодирования операций
OP_MAP = {
    '+': -1,
    '-': -2,
    '*': -3,
    '/': -4,
    '%': -5,
    '^': -6
}


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value  # Число (0..9), либо код операции (-1..-6)
        self.left = left  # Левое поддерево
        self.right = right  # Правое поддерево

    def __repr__(self):
        # Вспомогательный метод для удобного вывода дерева в консоль
        if self.left is None and self.right is None:
            return f"{self.value}"
        return f"({self.value} {self.left} {self.right})"


def build_tree(tokens):
    """
    Рекурсивно строит дерево из списка токенов префиксного выражения.
    """
    if not tokens:
        return None

    token = tokens.pop(0)

    # Если токен — это операция
    if token in OP_MAP:
        node = Node(OP_MAP[token])
        node.left = build_tree(tokens)
        node.right = build_tree(tokens)
        return node
    else:
        # Если токен — число (операнд)
        return Node(int(token))


def evaluate_node(op_code, left_val, right_val):
    """
    Выполняет арифметическую операцию по её коду.
    """
    if op_code == -1: return left_val + right_val
    if op_code == -2: return left_val - right_val
    if op_code == -3: return left_val * right_val
    if op_code == -4: return left_val // right_val  # Деление нацело
    if op_code == -5: return left_val % right_val
    if op_code == -6: return left_val ** right_val  # Возведение в степень
    return 0


def transform_and_evaluate(root):
    """
    Рекурсивно обходит дерево. Если встречает операцию возведения в степень (-6),
    вычисляет всё это поддерево, удаляет потомков и заменяет корень результатом.
    Для остальных узлов возвращает их (возможно, измененное) поддерево и текущее значение.
    """
    if root is None:
        return None, 0

    # Если это лист (просто число)
    if root.left is None and root.right is None:
        return root, root.value

    # Рекурсивно обрабатываем левое и правое поддеревья
    root.left, left_val = transform_and_evaluate(root.left)
    root.right, right_val = transform_and_evaluate(root.right)

    # Вычисляем значение в текущем узле (оно нужно для верхних уровней)
    current_val = evaluate_node(root.value, left_val, right_val)

    # Условие задачи: если текущая операция — возведение в степень
    if root.value == -6:
        root.value = current_val  # Заменяем операцию на посчитанное значение
        root.left = None  # Удаляем левое поддерево
        root.right = None  # Удаляем правое поддерево

    return root, current_val


# --- Демонстрация работы программы ---

# Создадим временный файл для теста.
# Выражение: + * 2 3 ^ 2 3  ->  (2 * 3) + (2 ^ 3) = 6 + 8 = 14
filename = "expression.txt"
with open(filename, "w") as f:
    f.write("+ * 2 3 ^ 2 3")

# 1. Чтение из файла
if os.path.exists(filename):
    with open(filename, "r") as f:
        expr_str = f.read().strip()

    # Разбираем строку на отдельные символы/токены
    tokens = expr_str.split()

    # 2. Построение исходного дерева
    root = build_tree(tokens)
    print("Исходное дерево (в префиксном виде с кодами):")
    print(root)
    # Вывод: (-1 (-3 2 3) (-6 2 3))

    # 3. Преобразование дерева (свёртка степеней)
    transformed_root, _ = transform_and_evaluate(root)

    print("\nПреобразованное дерево (без степеней):")
    print(transformed_root)
    # Вывод: (-1 (-3 2 3) 8) -> Поддерево (-6 2 3) превратилось в узел 8

    print(f"\nУказатель на корень полученного дерева: {hex(id(transformed_root))}")
else:
    print(f"Файл {filename} не найден.")
"""
Gemini
"""