class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


codes = {
    "+": -1,
    "-": -2,
    "*": -3,
    "/": -4,
    "%": -5,
    "^": -6
}


def build_tree(tokens):
    token = tokens.pop(0)

    if token.isdigit():
        return Node(int(token))

    node = Node(codes[token])
    node.left = build_tree(tokens)
    node.right = build_tree(tokens)

    return node


def calc(node):
    if node.value >= 0:
        return node.value

    a = calc(node.left)
    b = calc(node.right)

    if node.value == -1:
        return a + b

    if node.value == -2:
        return a - b

    if node.value == -3:
        return a * b

    if node.value == -4:
        return a // b

    if node.value == -5:
        return a % b

    return a ** b


def remove_power(node):
    if node is None:
        return

    remove_power(node.left)
    remove_power(node.right)

    if node.value == -6:
        value = calc(node)

        node.value = value
        node.left = None
        node.right = None


with open("filename.txt") as file:
    expression = file.read().strip()

tokens = expression.split()

root = build_tree(tokens)

remove_power(root)

print(root)
"""
ChatGPT
"""