"""Дана вершина A1 стека (если стек пуст, A1 = null).
Извлечь все элементы, вывести их значения и количество N.
Освободить ресурсы элементов методом dispose.
"""

import gc
import random
from typing import Any


class Node:
    """Элемент связного списка стека."""

    def __init__(self, data: Any, next_node: 'Node | None' = None) -> None:
        self.data = data
        self.next = next_node

    def dispose(self) -> None:
        """Освобождает ресурсы элемента."""
        self.data = None
        self.next = None

    def __str__(self) -> str:
        return str(self.data)


class Stack:
    """Стек на основе связного списка."""

    def __init__(self) -> None:
        self.head: Node | None = None

    def is_empty(self) -> bool:
        """Проверяет, пуст ли стек."""
        return self.head is None

    def push(self, data: Any) -> None:
        """Добавляет элемент в стек."""
        self.head = Node(data, self.head)

    def pop(self) -> Any | None:
        """Извлекает элемент из стека."""
        if self.is_empty():
            return None
        node = self.head
        self.head = node.next
        data = node.data
        node.dispose()
        return data

    def dispose(self) -> None:
        """Освобождает оставшиеся ресурсы стека."""
        while not self.is_empty():
            self.pop()
        gc.collect()


def main() -> None:
    """Главная функция программы."""
    stack = Stack()
    for _ in range(random.randint(0, 20)):
        stack.push(random.randint(1, 100))

    count = 0
    while not stack.is_empty():
        print(stack.pop())
        count += 1
    print(count)
    stack.dispose()


if __name__ == '__main__':
    main()