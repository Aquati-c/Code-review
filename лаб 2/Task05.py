"""
Дано число K (> 0) и ссылки A1 и A2 на первый и последний элементы не пустого двусвязного списка. Осуществить
циклический сдвиг элементов списка на K позиций назад(т. е. в направлении от конца к началу списка) и вывести
ссылки на первый и последний элементы полученного списка. Для выполнения циклического сдвига преобразовать
исходный список в циклический (см. задание Dynamic55), после чего «разорвать» его в позиции, соответствующей
данному значению K. Новые объекты типа Node не создавать

Dynamic55. Дан первый элемент A1 непустого двусвязного списка. Преобразовать список в циклический, записав в
свойство Next последнего элемента списка ссылку на его первый элемент, а в свойство Prev первого элемента —
ссылку на последний элемент. Вывести ссылку на элемент, который был последним элементом исходного списка.
"""


class Node:
    def __init__(self, data = None, next = None, prev = None):
        self.data = data
        self.next = next
        self.prev = prev


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insertAtBegin(self, data): # вставляет новый узел с данными в начало списка
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def make_circular(self): # преобразует список в циклический
        if self.head is None:
            return None
        self.tail.next = self.head
        self.head.prev = self.tail
        return self.tail  # возвращаем ссылку на последний элемент (Dynamic55)

    def cyclic_shift(self, k): # выполняет сдвиг на к позиций
        if self.head is None or self.head.next is None: # пустой или одно-элементный список
            return self.head, self.tail

        self.make_circular()

        for _ in range(k):
            self.head = self.head.prev
            self.tail = self.tail.prev
        self.tail.next = None
        self.head.prev = None
        return self.head, self.tail

    def print_list(self): # вывод списка
        current = self.head
        while current:
            print(current.data)
            current = current.next




listi = DoublyLinkedList()
listi.insertAtBegin(1)
listi.insertAtBegin(2)
listi.insertAtBegin(3)
listi.insertAtBegin(4)
listi.insertAtBegin(5)

print("Исходный список:")
listi.print_list()

k = int(input('Введите число K (> 0): '))

new_head, new_tail = listi.cyclic_shift(k)

print(f"Список после циклического сдвига на {k} позиций:")
listi.print_list()
print("Первый элемент:", new_head)
print("Последний элемент:", new_tail)
"""Дано число K (> 0) и ссылки A1, A2 на двусвязный список.

Циклически сдвинуть элементы на K позиций назад через преобразование
в циклический список и разрыв в нужной позиции. Новые Node не создавать.
"""


class Node:
    """Элемент двусвязного списка."""

    def __init__(
        self,
        data: int,
        next_node: 'Node | None' = None,
        prev_node: 'Node | None' = None,
    ) -> None:
        self.data = data
        self.next = next_node
        self.prev = prev_node

    def __repr__(self) -> str:
        return f'Node({self.data})'


class DoublyLinkedList:
    """Двусвязный список."""

    def __init__(self) -> None:
        self.head: Node | None = None
        self.tail: Node | None = None

    def insert_at_begin(self, data: int) -> None:
        """Вставляет элемент в начало списка."""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return

        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

    def make_circular(self) -> Node | None:
        """Преобразует список в циклический."""
        if self.head is None:
            return None
        self.tail.next = self.head
        self.head.prev = self.tail
        return self.tail

    def cyclic_shift(self, k: int) -> tuple[Node | None, Node | None]:
        """Выполняет циклический сдвиг на K позиций назад."""
        if self.head is None or self.head.next is None:
            return self.head, self.tail

        self.make_circular()
        for _ in range(k):
            self.head = self.head.prev
            self.tail = self.tail.prev

        self.tail.next = None
        self.head.prev = None
        return self.head, self.tail

    def print_list(self) -> None:
        """Выводит элементы списка."""
        current = self.head
        while current:
            print(current.data)
            current = current.next


def main() -> None:
    """Главная функция программы."""
    try:
        linked_list = DoublyLinkedList()
        for value in (5, 4, 3, 2, 1):
            linked_list.insert_at_begin(value)

        print('Исходный список:')
        linked_list.print_list()

        k = int(input('Введите число K (> 0): '))
        if k <= 0:
            raise ValueError('K должно быть больше 0')

        new_head, new_tail = linked_list.cyclic_shift(k)

        print(f'Список после циклического сдвига на {k} позиций:')
        linked_list.print_list()
        print(f'Первый элемент: {new_head}')
        print(f'Последний элемент: {new_tail}')
    except ValueError:
        # Некорректный ввод
        print('Неверный ввод')


if __name__ == '__main__':
    main()