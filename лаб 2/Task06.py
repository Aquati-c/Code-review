"""Даны ссылки A1 и A2 на барьерный и текущий элементы двусвязного списка.

Реализовать класс IntListB с DeleteCurrent, IsBarrier, InsertLast и Put.
Удалить до 5 элементов и вывести их значения и ссылку на новый current.
"""


class Node:
    """Элемент двусвязного списка."""

    def __init__(self, data: int) -> None:
        self.data = data
        self.prev: 'Node | None' = None
        self.next: 'Node | None' = None

    def dispose(self) -> None:
        """Освобождает ресурсы элемента."""
        self.data = 0
        self.prev = None
        self.next = None

    def __repr__(self) -> str:
        return f'Node({self.data})'


class PT:
    """Класс для вывода ссылок."""

    @staticmethod
    def put(node: Node | None) -> None:
        """Выводит ссылку на элемент."""
        print(node)


class IntListB:
    """Двусвязный список с барьерным элементом."""

    def __init__(self, barrier: Node, current: Node) -> None:
        self._barrier = barrier
        self._current = current

    def insert_last(self, d: int) -> None:
        """Добавляет элемент в конец списка."""
        new_node = Node(d)
        last = self._barrier.prev
        last.next = new_node
        new_node.prev = last
        new_node.next = self._barrier
        self._barrier.prev = new_node
        self._current = new_node

    def is_barrier(self) -> bool:
        """Проверяет, является ли текущий элемент барьерным."""
        return self._current == self._barrier

    def delete_current(self) -> int:
        """Удаляет текущий элемент и возвращает его значение."""
        if self.is_barrier():
            return 0

        deleted = self._current
        value = deleted.data
        prev_node = deleted.prev
        next_node = deleted.next

        prev_node.next = next_node
        next_node.prev = prev_node

        if next_node != self._barrier:
            self._current = next_node
        else:
            self._current = prev_node

        deleted.dispose()
        return value

    def put(self) -> None:
        """Выводит ссылку на текущий элемент."""
        PT.put(self._current)


def main() -> None:
    """Главная функция программы."""
    try:
        barrier = Node(0)
        barrier.next = barrier
        barrier.prev = barrier
        lst = IntListB(barrier, barrier)

        n = int(input('Введите количество элементов списка: '))
        for i in range(n):
            lst.insert_last(int(input(f'Введите элемент {i + 1}: ')))

        deleted = []
        for _ in range(5):
            if lst.is_barrier():
                break
            deleted.append(lst.delete_current())

        print('Удалённые элементы:', deleted)
        print('Новый текущий элемент:')
        lst.put()
    except ValueError:
        # Некорректный ввод
        print('Неверный ввод')


if __name__ == '__main__':
    main()