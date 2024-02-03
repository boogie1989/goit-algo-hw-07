from three import root


def sum_of_values(node):
    """
    Функція для знаходження суми всіх значень у двійковому дереві пошуку або в AVL-дереві.
    """
    if node is None:
        return 0
    return node.value + sum_of_values(node.left) + sum_of_values(node.right)


print(f'Сума всіх значень в дереві: {sum_of_values(root)}')
