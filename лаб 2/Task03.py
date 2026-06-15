"""Дан односвязный список с головой P1.

Вставить значение M после каждого четвёртого элемента.
Вывести ссылку на последний элемент P2.
"""


class Node:
    """Элемент односвязного списка."""

    def __init__(self, data: int) -> None:
        self.data = data
        self.next: 'Node | None' = None

    def __repr__(self) -> str:
        return f'Node({self.data})'


class LinkedList:
    """Односвязный линейный список."""

    def __init__(self) -> None:
        self.head: Node | None = None

    def append(self, data: int) -> None:
        """Добавляет элемент в конец списка."""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def insert_after_every_fourth(self, m: int) -> None:
        """Вставляет M после каждого четвёртого элемента."""
        current = self.head
        count = 1
        while current:
            if count == 4:
                new_node = Node(m)
                new_node.next = current.next
                current.next = new_node
                count = 0
            current = current.next
            count += 1

    def get_last_element(self) -> Node | None:
        """Возвращает последний элемент списка."""
        current = self.head
        while current and current.next:
            current = current.next
        return current

    def display(self) -> None:
        """Выводит список."""
        current = self.head
        while current:
            print(current.data, end=' -> ')
            current = current.next
        print('None')


def main() -> None:
    """Главная функция программы."""
    try:
        n = int(input('Введите количество элементов в списке (не менее 4): '))
        if n < 4:
            raise ValueError('Количество элементов должно быть не менее 4')

        m = int(input('Введите значение M: '))
        ll = LinkedList()
        for i in range(n):
            ll.append(int(input(f'Введите значение для элемента {i + 1}: ')))

        ll.insert_after_every_fourth(m)
        print('Содержимое списка после вставки:')
        ll.display()

        p2 = ll.get_last_element()
        if p2 is None:
            print('Список пуст')
            return
        print(f'Ссылка на последний элемент P2: {p2}')
    except ValueError:
        # Некорректный ввод
        print('Неверный ввод')


if __name__ == '__main__':
    main()