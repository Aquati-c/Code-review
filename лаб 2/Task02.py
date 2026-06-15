"""Даны две непустые очереди A1–A2 и A3–A4 одинаковой длины.
Объединить очереди чередованием элементов (с первой).
Вывести начало и конец результата. Новые Node не создавать.
"""


class Node:
    """Элемент очереди."""

    def __init__(self, value: int) -> None:
        self.value = value
        self.next: 'Node | None' = None


def create_queue(n: int) -> tuple[Node, Node]:
    """Создаёт очередь из n элементов."""
    values = list(map(int, input(f'Введите {n} элементов очереди через пробел: ').split()))
    if len(values) != n:
        raise ValueError('Неверное количество элементов')

    head = Node(values[0])
    tail = head
    for value in values[1:]:
        tail.next = Node(value)
        tail = tail.next
    return head, tail


def merge_queues(a1: Node, a3: Node) -> tuple[Node, Node]:
    """Объединяет две очереди чередованием без создания новых узлов."""
    head = a1
    tail = None
    cur1, cur2 = a1, a3

    while cur1 and cur2:
        next1, next2 = cur1.next, cur2.next
        cur1.next = cur2
        if next1:
            cur2.next = next1
        else:
            tail = cur2
        cur1, cur2 = next1, next2

    if tail is None:
        tail = a1 if cur1 else a3

    return head, tail


def print_queue(head: Node | None) -> None:
    """Выводит очередь."""
    cur = head
    while cur:
        print(cur.value, end=' -> ')
        cur = cur.next
    print('None')


def main() -> None:
    """Главная функция программы."""
    try:
        n = int(input('Введите количество элементов в каждой очереди: '))
        a1, _ = create_queue(n)
        a3, _ = create_queue(n)

        head, tail = merge_queues(a1, a3)

        print('\nОбъединённая очередь:')
        print_queue(head)
        print(f'Head: {head.value}, Tail: {tail.value}')
    except ValueError:
        # Некорректный ввод
        print('Неверный ввод')


if __name__ == '__main__':
    main()