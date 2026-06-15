import math

# Коды операций
ADD = -1
SUB = -2
MUL = -3
DIV = -4
MOD = -5
POW = -6


class Node:
    """Узел дерева выражения"""

    def __init__(self, value):
        self.value = value  # число (0-9) или код операции
        self.left = None
        self.right = None


def build_tree(tokens):
    """Построение дерева из списка токенов (рекурсивно)"""
    if not tokens:
        return None

    token = tokens.pop(0)
    node = Node(token)

    # Если это операция (отрицательное число), читаем два поддерева
    if token < 0:
        node.left = build_tree(tokens)
        node.right = build_tree(tokens)

    return node


def evaluate(node):
    """Вычисление значения поддерева"""
    if node is None:
        return 0

    # Если это лист (число от 0 до 9)
    if 0 <= node.value <= 9:
        return node.value

    left_val = evaluate(node.left)
    right_val = evaluate(node.right)

    if node.value == ADD:
        return left_val + right_val
    elif node.value == SUB:
        return left_val - right_val
    elif node.value == MUL:
        return left_val * right_val
    elif node.value == DIV:
        return left_val // right_val  # целочисленное деление
    elif node.value == MOD:
        return left_val % right_val
    elif node.value == POW:
        return int(math.pow(left_val, right_val))
    else:
        return 0


def replace_power(node):
    """Замена поддеревьев с возведением в степень на их числовое значение"""
    if node is None:
        return

    # Сначала обрабатываем левое и правое поддеревья
    replace_power(node.left)
    replace_power(node.right)

    # Если текущий узел — возведение в степень, вычисляем и заменяем
    if node.value == POW:
        result = evaluate(node)
        node.value = result
        node.left = None
        node.right = None


def read_expression_from_file(filename):
    """Чтение выражения из файла"""
    with open(filename, 'r') as file:
        content = file.read().strip()
        # Разделяем по пробелам и преобразуем в числа
        tokens = [int(x) for x in content.split()]
    return tokens


def print_tree(node, level=0):
    """Вывод дерева для отладки (с отступами)"""
    if node is None:
        return
    print("  " * level + f"({node.value})")
    print_tree(node.left, level + 1)
    print_tree(node.right, level + 1)


def inorder_traversal(node, result):
    """Симметричный обход для вывода дерева в строку"""
    if node is None:
        return
    inorder_traversal(node.left, result)
    result.append(str(node.value))
    inorder_traversal(node.right, result)


def main():
    filename = input("Введите имя файла: ")

    try:
        # Чтение выражения из файла
        tokens = read_expression_from_file(filename)
        print(f"Выражение из файла: {tokens}")

        # Построение дерева
        root = build_tree(tokens)

        print("\nИсходное дерево (значения узлов):")
        print_tree(root)

        # Замена поддеревьев с возведением в степень
        replace_power(root)

        print("\nДерево после замены степени (значения узлов):")
        print_tree(root)

        # Вывод указателя на корень (адрес в памяти)
        print(f"\nУказатель на корень полученного дерева: {id(root)}")

        # Дополнительно: вывод в строковом виде
        result = []
        inorder_traversal(root, result)
        print(f"Дерево в виде списка значений: {result}")

    except FileNotFoundError:
        print(f"Ошибка: файл '{filename}' не найден!")
    except Exception as e:
        print(f"Ошибка при обработке: {e}")


if __name__ == "__main__":
    main()
"""
DeepSeek
"""