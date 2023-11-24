import random


class RandomBinaryTree:
    class Node:
        def __init__(self, key):
            self.key = key
            self.left = None
            self.right = None
            self.size = 1

    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert_recursive(self.root, key)

    def _insert_recursive(self, current, key):
        if current is None:
            return self.Node(key)

        current.size += 1
        if random.random() * current.size < 1:
            return self._insert_at_root(current, key)

        if key < current.key:
            current.left = self._insert_recursive(current.left, key)
        else:
            current.right = self._insert_recursive(current.right, key)

        return current

    def _insert_at_root(self, current, key):
        new_node = self.Node(key)
        left_size = 0 if current.left is None else current.left.size
        right_size = 0 if current.right is None else current.right.size

        if random.random() * (left_size + right_size + 1) < 1:
            new_node.left = current.left
            new_node.right = current
            current.left = None
        else:
            new_node.right = current.right
            new_node.left = current
            current.right = None

        new_node.size = left_size + right_size + 1
        return new_node

    def rotate_right(self, key):
        self.root = self._rotate_right_recursive(self.root, key)

    def rotate_left(self, key):
        self.root = self._rotate_left_recursive(self.root, key)

    def _rotate_right_recursive(self, node, key):
        if node is None:
            return None

        if key < node.key:
            node.left = self._rotate_right_recursive(node.left, key)
        elif key > node.key:
            node.right = self._rotate_right_recursive(node.right, key)
        else:
            if node.left is None:
                return node

            new_root = node.left
            node.left = new_root.right
            new_root.right = node
            new_root.size = node.size
            node.size = 1 + (node.left.size if node.left else 0) + (node.right.size if node.right else 0)
            return new_root

        return node

    def _rotate_left_recursive(self, node, key):
        if node is None:
            return None

        if key < node.key:
            node.left = self._rotate_left_recursive(node.left, key)
        elif key > node.key:
            node.right = self._rotate_left_recursive(node.right, key)
        else:
            if node.right is None:
                return node

            new_root = node.right
            node.right = new_root.left
            new_root.left = node
            new_root.size = node.size
            node.size = 1 + (node.left.size if node.left else 0) + (node.right.size if node.right else 0)
            return new_root

        return node
    def remove(self, key):
        self.root = self._remove_recursive(self.root, key)

    def _remove_recursive(self, root, key):
        if not root:
            return root
        if key < root.key:
            root.left = self._remove_recursive(root.left, key)
        elif key > root.key:
            root.right = self._remove_recursive(root.right, key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            root.key = self._get_min_value_node(root.right).key
            root.right = self._remove_recursive(root.right, root.key)
        return root

    def is_empty(self):
        return self.root is None

    def _get_min_value_node(self, node):
        while node.left:
            node = node.left
        return node

    def _merge(self, left, right):
        if left is None:
            return right
        if right is None:
            return left

        if random.random() * (left.size + right.size) < left.size:
            left.right = self._merge(left.right, right)
            left.size = left.size + right.size + 1
            return left
        else:
            right.left = self._merge(left, right.left)
            right.size = left.size + right.size + 1
            return right

    def search(self, key):
        return self._search_recursive(self.root, key)

    def _search_recursive(self, node, key):
        if node is None or node.key == key:
            return node
        if key < node.key:
            return self._search_recursive(node.left, key)
        return self._search_recursive(node.right, key)

    def print_tree(self):
        result = []
        self._symmetrical_traversal(self.root, result)
        print("Симметричный обход (symmetrical):", result)

    def print_preorder(self):
        result = self._preorder_traversal()
        print("Прямой обход (preorder):", result)

    def print_postorder(self):
        result = self._postorder_traversal()
        print("Обратный обход (postorder):", result)

    def _symmetrical_traversal(self, node, result):
        if node:
            self._symmetrical_traversal(node.left, result)
            result.append(node.key)
            self._symmetrical_traversal(node.right, result)

    def _preorder_traversal(self):
        result = []
        stack = [self.root]
        while stack:
            node = stack.pop()
            if node:
                result.append(node.key)
                stack.append(node.right)
                stack.append(node.left)

        return result

    def _postorder_traversal(self):
        result = []
        stack = [(self.root, False)]
        while stack:
            node, visited = stack.pop()
            if node:
                if visited:
                    result.append(node.key)
                else:
                    stack.append((node, True))
                    stack.append((node.right, False))
                    stack.append((node.left, False))

        return result

    def height(self):
        return self._height_recursive(self.root)

    def _height_recursive(self, node):
        if node is None:
            return 0
        left_height = self._height_recursive(node.left)
        right_height = self._height_recursive(node.right)
        return max(left_height, right_height) + 1

    def print_pretty_tree(self):
        print("Красивый вывод дерева:")
        self._print_pretty_tree_recursive(self.root, 0)
        print()

    def _print_pretty_tree_recursive(self, node, level):
        if node is not None:
            self._print_pretty_tree_recursive(node.right, level + 1)
            print("  " * level + str(node.key))
            self._print_pretty_tree_recursive(node.left, level + 1)

    def is_binary_search_tree(self):
        return self._is_binary_search_tree_recursive(self.root)

    def _is_binary_search_tree_recursive(self, node, min_val=float('-inf'), max_val=float('inf')):
        if node is None:
            return True

        if not (min_val <= node.key <= max_val):
            return False

        left_check = self._is_binary_search_tree_recursive(node.left, min_val, node.key - 1)
        right_check = self._is_binary_search_tree_recursive(node.right, node.key + 1, max_val)

        return left_check and right_check
'''
# Пример использования
if __name__ == "__main__":
    random_tree = RandomBinaryTree()
    elements = [5, 3, 7, 2, 4, 6, 8, 1, 9]
    for element in elements:
        random_tree.insert(element)

    random_tree.print_tree()
    print("Высота дерева:", random_tree.height())

    random_tree.print_pretty_tree()

import random'''



def main():
    random_bst = RandomBinaryTree()

    while True:
        print("\nВыберите действие:")
        print("1. Добавить элемент")
        print("2. Удалить элемент")
        print("3. Поиск элемента")
        print("4. Проверить на пустоту")
        print("5. Вывести высоту дерева")
        print("6. Вывести дерево")
        print("7. Прямой обход")
        print("8. Обратный обход")
        print("9. Симметричный обход")
        print("10. Проверка на дерево поиска")
        print("0. Выйти из программы")

        choice = input("Ваш выбор: ")

        if choice == '1':
            key = int(input("Введите ключ для добавления: "))
            random_bst.insert(key)
        elif choice == '2':
            key = int(input("Введите ключ для удаления: "))
            random_bst.remove(key)
        elif choice == '3':
            key = int(input("Введите ключ для поиска: "))
            if random_bst.search(key):
                print("Элемент найден.")
            else:
                print("Элемент не найден.")
        elif choice == '4':
            if random_bst.is_empty():
                print("Дерево пусто.")
            else:
                print("Дерево не пусто.")
        elif choice == '5':
            print("Высота дерева:", random_bst.height())
        elif choice == '6':
            random_bst.print_pretty_tree()
        elif choice == '7':
            print("Прямой обход:")
            random_bst.print_preorder()
        elif choice == '8':
            print("Обратный обход:")
            random_bst.print_postorder()
        elif choice == '9':
            print("Симметричный обход:")
            random_bst.print_tree()
        elif choice == '10':
            if random_bst.is_binary_search_tree():
                print("Дерево является деревом поиска.")
            else:
                print("Дерево не является деревом поиска.")
        # elif choice == '11':
        #     key = int(input("Введите ключ вершины для правого поворота: "))
        #     random_bst.rotate_right(key)
        # elif choice == '12':
        #     key = int(input("Введите ключ вершины для левого поворота: "))
        #     random_bst.rotate_left(key)
        elif choice == '0':
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")


if __name__ == "__main__":
    main()
