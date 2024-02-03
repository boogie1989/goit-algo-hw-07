from three import root


def find_min_value(node):
    """
    Функція для знаходження найменшого значення в двійковому дереві пошуку або в AVL-дереві.
    """
    current = node
    # Йдемо вліво до останнього вузла
    while current.left is not None:
        current = current.left
    return current.value


print(f'Найменше значення в дереві: {find_min_value(root)}')
