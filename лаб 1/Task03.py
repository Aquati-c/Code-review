"""Вычислить значение целочисленного выражения, заданного строкой S.

<выражение> ::= <цифра> | <выражение> + <цифра> | <выражение> − <цифра>
"""


def evaluate_expression(expression: str) -> int:
    """Вычисляет значение выражения."""
    result = int(expression[0])
    i = 1
    while i < len(expression):
        operator = expression[i]
        digit = int(expression[i + 1])
        if operator == '+':
            result += digit
        elif operator == '-':
            result -= digit
        else:
            raise ValueError('Недопустимый оператор')
        i += 2
    return result


def main() -> None:
    """Главная функция программы."""
    try:
        expression = input('Введите выражение: ')
        result = evaluate_expression(expression)
        print(f"Результат выражения '{expression}': {result}")
    except (ValueError, IndexError):
        # Некорректный формат выражения
        print('Неверный ввод')


if __name__ == '__main__':
    main()