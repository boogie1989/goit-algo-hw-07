class Node:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# Створення прикладу двійкового дерева пошуку
root = Node(10)
root.left = Node(5)
root.right = Node(15)
root.right.left = Node(12)
root.right.right = Node(20)  # Найбільше значення
