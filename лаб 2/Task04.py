"""Дан текстовый файл: в первой строке n, во второй — n целых чисел.

Создать упорядоченный по возрастанию список, вставляя каждый элемент
с сохранением упорядоченности.
"""


class Node:
    """Элемент односвязного списка."""

    def __init__(self, data: int) -> None:
        self.data = data
        self.next: 'Node | None' = None


class LinkedList:
    """Упорядоченный односвязный список."""

    def __init__(self) -> None:
        self.head: Node | None = None

    def insert_sorted(self, data: int) -> None:
        """Вставляет элемент с сохранением порядка."""
        new_node = Node(data)
        if not self.head or self.head.data >= data:
            new_node.next = self.head
            self.head = new_node
            return

        current = self.head
        while current.next and current.next.data < data:
            current = current.next
        new_node.next = current.next
        current.next = new_node

    def print_list(self) -> None:
        """Выводит элементы списка."""
        current = self.head
        while current:
            print(current.data, end=' ')
            current = current.next
        print()

    def get_all_elements(self) -> list[int]:
        """Возвращает все элементы списка."""
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        return elements


def build_sorted_list(filename: str) -> LinkedList:
    """Создаёт упорядоченный список из файла."""
    with open(filename, 'r', encoding='utf-8') as f:
        n = int(f.readline())
        numbers = list(map(int, f.readline().split()))

    if len(numbers) != n:
        raise ValueError('Неверное количество чисел в файле')

    linked_list = LinkedList()
    for number in numbers:
        linked_list.insert_sorted(number)
    return linked_list


def write_list_to_file(filename: str, linked_list: LinkedList) -> None:
    """Записывает список в файл."""
    elements = linked_list.get_all_elements()
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(f'{len(elements)}\n')
        f.write(' '.join(map(str, elements)))


def main() -> None:
    """Главная функция программы."""
    try:
        filename = input('Введите имя текстового файла: ')
        sorted_list = build_sorted_list(filename)

        print('Упорядоченный список:')
        sorted_list.print_list()

        write_list_to_file(filename, sorted_list)
        print(f'Сортированный список записан в файл {filename}')
    except FileNotFoundError:
        # Файл не найден
        print('Файл не найден')
    except ValueError:
        # Некорректные данные в файле
        print('Неверный ввод')
    except OSError as e:
        # Ошибка чтения или записи файла
        print(f'Ошибка работы с файлом: {e}')


if __name__ == '__main__':
    main()