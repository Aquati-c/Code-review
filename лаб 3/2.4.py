"""
Условие задачи:
Реализовать программу для построения и вычисления префиксного дерева выражений.
Программа считывает префиксное выражение из файла, строит по нему двоичное дерево.
Затем выполняется рекурсивный обход: если встречается операция возведения
в степень, программа сворачивает это поддерево, заменяя узел числовым результатом
и удаляя его потомков. Конечный результат и структура дерева выводятся на экран.
"""

import os
from typing import Optional, Union, Any

# Константы для кодирования операций
OP_MAP: dict[str, int] = {
    '+': -1,
    '-': -2,
    '*': -3,
    '/': -4,
    '%': -5,
    '^': -6
}


class Node:
    """Узел двоичного дерева выражений."""

    def __init__(
        self,
        value: int,
        left: Optional['Node'] = None,
        right: Optional['Node'] = None
    ) -> None:
        """Инициализирует узел дерева.

        Args:
            value (int): Числовой операнд (0..9) или код операции (-1..-6).
            left (Optional[Node]): Левое поддерево. Defaults to None.
            right (Optional[Node]): Правое поддерево. Defaults to None.
        """
        self.value: int = value
        self.left: Optional['Node'] = left
        self.right: Optional['Node'] = right

    def __repr__(self) -> str:
        """Возвращает строковое представление дерева в префиксном виде."""
        if self.left is None and self.right is None:
            return f"{self.value}"
        return f"({self.value} {self.left} {self.right})"


def build_tree(tokens: list[str]) -> Optional[Node]:
    """Рекурсивно строит дерево из списка токенов префиксного выражения.

    Args:
        tokens (list[str]): Список строковых токенов выражения.

    Returns:
        Optional[Node]: Корень построенного дерева или None.
    """
    if not tokens:
        return None

    token: str = tokens.pop(0)

    # Если токен — это операция
    if token in OP_MAP:
        node: Node = Node(OP_MAP[token])
        node.left = build_tree(tokens)
        node.right = build_tree(tokens)
        return node

    # Если токен — число (операнд). Избыточный else убран по Code Style.
    return Node(int(token))


def evaluate_node(op_code: int, left_val: int, right_val: int) -> int:
    """Выполняет арифметическую операцию по её целочисленному коду.

    Args:
        op_code (int): Код операции (-1..-6).
        left_val (int): Значение левого операнда.
        right_val (int): Значение правого операнда.

    Returns:
        int: Результат арифметического вычисления.
    """
    if op_code == -1:
        return left_val + right_val
    if op_code == -2:
        return left_val - right_val
    if op_code == -3:
        return left_val * right_val
    if op_code == -4:
        return left_val // right_val  # Деление нацело
    if op_code == -5:
        return left_val % right_val
    if op_code == -6:
        return left_val ** right_val  # Возведение в степень
    return 0


def transform_and_evaluate(root: Optional[Node]) -> tuple[Optional[Node], int]:
    """Рекурсивно обходит дерево и производит свёртку операции степени (-6).

    Если узел является операцией возведения в степень, вычисляет значение
    этого поддерева, удаляет его потомков и перезаписывает значение корня.

    Args:
        root (Optional[Node]): Текущий узел дерева обхода.

    Returns:
        tuple[Optional[Node], int]: Измененный узел и вычисленное значение в нем.
    """
    if root is None:
        return None, 0

    # Если это лист (операнд)
    if root.left is None and root.right is None:
        return root, root.value

    # Рекурсивно обрабатываем поддеревья (Принцип DRY)
    root.left, left_val = transform_and_evaluate(root.left)
    root.right, right_val = transform_and_evaluate(root.right)

    # Вычисляем текущее значение для передачи вверх по стеку
    current_val: int = evaluate_node(root.value, left_val, right_val)

    # Условие свёртки: если текущая операция — возведение в степень
    if root.value == -6:
        root.value = current_val
        root.left = None
        root.right = None

    return root, current_val


def main() -> None:
    """Управляет жизненным циклом программы и интерфейсом пользователя."""
    filename: str = "expression.txt"

    # Подготовка тестового окружения (генерация файла)
    with open(filename, "w", encoding="utf-8") as f:
        f.write("+ * 2 3 ^ 2 3")

    print("=== Программа свёртки дерева выражений ===")

    if not os.path.exists(filename):
        print(f"[Ошибка]: Файл {filename} не найден.")
        return

    try:
        with open(filename, "r", encoding="utf-8") as f:
            expr_str: str = f.read().strip()

        if not expr_str:
            print("[Ошибка]: Файл пуст.")
            return

        tokens: list[str] = expr_str.split()

        # Построение и вывод исходного дерева
        root: Optional[Node] = build_tree(tokens)
        print("Исходное дерево (в префиксном виде с кодами):")
        print(root)

        # Преобразование (свёртка степеней)
        transformed_root, _ = transform_and_evaluate(root)

        print("\nПреобразованное дерево (без степеней):")
        print(transformed_root)
        print(f"\nУказатель на корень полученного дерева: {hex(id(transformed_root))}")

    except (ValueError, IndexError) as ex:
        # Ловим конкретные ошибки валидации данных в файле (Пункт 2, Локальное требование №2)
        print(f"[Ошибка разбора файла]: Некорректный синтаксис выражения. ({ex})")
    except Exception as ex:
        # Резервный перехват непредвиденных системных ошибок
        print(f"[Критическая ошибка]: {ex}")


if __name__ == "__main__":
    main()