from three import root


def find_max_value(node):
    """
    Функція для знаходження найбільшого значення в двійковому дереві пошуку або в AVL-дереві.
    """
    current = node
    # Йдемо вправо до останнього вузла
    while current.right is not None:
        current = current.right
    return current.value


print(f'Найбільше значення в дереві: {find_max_value(root)}')
