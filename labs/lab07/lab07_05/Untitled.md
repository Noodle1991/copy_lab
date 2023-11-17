---
jupyter:
  jupytext:
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.3'
      jupytext_version: 1.15.2
  kernelspec:
    display_name: Python 3 (ipykernel)
    language: python
    name: python3
---

```python

```

```python
import random

class Node:
    def __init__(self, data):
        self.left=None
        self.right=None
        self.data=data

class RandomizedTree:
    def __init__(self):
        self.root = None
    
    def push(self, data):
        self.root = self._push(self.root, data)

    def _push(self, node, data):
        if node is None:
            return Node(data)
        elif data < node.data:
            node.left = self._push(node.left, data)
            node = self._rotateRight(node)
        else:
            node.right = self._push(node.right, data)
            node = self._rotateLeft(node)
        return node

    def _rotateLeft(self, node):
        rightChild = node.right
        node.right = rightChild.left
        rightChild.left = node
        return rightChild

    def _rotateRight(self, node):
        leftChild = node.left
        node.left = leftChild.right
        leftChild.right = node
        return leftChild

    def pop(self, data):
        self.root = self._pop(self.root, data)

    def _pop(self, node, data):
        if node is None:
            return node
        elif data < node.data:
            node.left = self._pop(node.left, data)
        elif data > node.data:
            node.right = self._pop(node.right, data)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                if random.random() < 0.5:
                    merged = self._merge(node.left, node.right)
                    node.left = merged
                else:
                    merged = self._merge(node.right, node.left)
                    node.right = merged
                return merged
        return node

    def _merge(self, tree1, tree2):
        if tree1 is None:
            return tree2
        if tree2 is None:
            return tree1
        if tree1.data<tree2.data:
            tree1.right=self._merge(tree1.right, tree2)
            return tree1
        else:
            tree2.left = self._merge(tree1, tree2.left)
            return tree2

    def _find_minimum_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def find_value(self, data):
        return self._find_value(data, self.root)
    
    def _find_value(self, data, node):
        if node is None or node.data == data:
            return node
        if data < node.data:
            return self._find_value(data, node.left)
        return self._find_value(data, node.right)

    def preorder_traversal(self):
        if self.root is not None:
            self._preorder_traversal(self.root)

    def _preorder_traversal(self, node):
        if node is not None:
            print(node.data)
            self._preorder_traversal(node.left)
            self._preorder_traversal(node.right)

    def inorder_traversal(self):
        if self.root is not None:
            self._inorder_traversal(self.root)

    def _inorder_traversal(self, node):
        if node is not None:
            self._inorder_traversal(node.left)
            print(node.data)
            self._inorder_traversal(node.right)

    def postorder_traversal(self):
        if self.root is not None:
            self._postorder_traversal(self.root)
            
    def _postorder_traversal(self, node):
        if node is not None:
            self._postorder_traversal(node.left)
            self._postorder_traversal(node.right)
            print(node.data)

    def height(self):
        if self.root is None:
            return 0
        return self._height(self.root)
            
            
    def _height(self, node):
        if node is None:
            return 0
        else:
            left_height = self._height(node.left)
            right_height = self._height(node.right)
            return max(left_height, right_height) + 1

    def print(self):
        if self.root is not None:
            self.printTree(self.root,level=0)
        else:
            print("This tree is empty")

    def printTree(self,node,level=0):
        if node is not None:
            self.printTree(node.right,level+1)
            print("    "*level+str(node.data)+"<")
            self.printTree(node.left,level+1)

    def clear(self):
        if self.root is not None:
            self._clear(self.root)
        self.root=None

    def _clear(self,node):
        if node is not None:
            self._clear(node.left)
            self._clear(node.right)
            node.left=None
            node.right=None

    #Задание 1_5
    def max(self):
        if self.root is None:
            return None, 0
        max, count=self._max(self.root)
        return max, count

    def _max(self,node):
        if node is None:
            return None, 0
        max=node.data
        count=1
        left_max,left_count=self._max(node.left)
        right_max,right_count=self._max(node.right)
        if left_max is not None:
            if max<left_max:
                max=left_max
                count=left_count
            elif max==left_max:
                count+=left_count
        if right_max is not None:
            if max<right_max:
                max=right_max
                count=right_count
            elif max==right_max:
                count+=right_count
        return max, count
        
            




t=RandomizedTree()
# t.print()
# print(type(4))
# print("~~~~test_push~~~~")
# t.push(8)
# t.push(4)
# t.push(12)
# t.push(2)
# t.push(6)
# t.push(10)
# t.push(14)
# t.push(16)
# t.push(4)
# t.push(7)
# t.push(1)
# t.push(13)
# t.print()
# print("\n")
# print("~~~~test_pop~~~~")
# t.pop(6)
# t.pop(14)
# t.pop(4)
# t.pop(13)
# t.print()
# print("\n")
# print("~~~~test_find_value~~~~")
# node1=t.find_value(16)
# node2=t.find_value(7)
# node3=t.find_value(2)
# node4=t.find_value(4)
# node5=t.find_value(6)
# if node1:
#     print("Узел найден: ",node1.data)
# else:
#     print("Узел не найден")
# print("\n")
# print("\n")
# print("~~~~test_preorder_traversal~~~~")
# # Обход в прямом направлении
# print("Прямой обход:")
# t.preorder_traversal()
# print("\n")
# print("~~~~test_inorder_traversa~~~~")
# # Симметричный обход
# print("Симметричный обход:")
# t.inorder_traversal()
# print("\n")
# print("~~~~test_postorder_traversa~~~~")
# # Обход в обратном направлении
# print("Обратный обход:")
# t.postorder_traversal()
# print("\n")
# print("~~~~test_height~~~~")
# print("Высота дерева =", t.height())
# print("\n")
# print("~~~~test_max~~~~")
# # t2=RandomizedTree()
# max_t, count_t=t.max()
# print(" Максимальное значение =",max_t,"\n","Количество повторений =",count_t)
# print("\n")
# print("~~~~test_clear~~~~")
# t.clear()
# t.print()
# print("\n")





```

```python

```

```python
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1
        self.count = 1

class AVLTree:
    def __init__(self):
        self.root = None

    def push(self, key):
        self.root = self._push(self.root, key)

    def _push(self, root, key):
        if root is None:
            return Node(key)
        elif key < root.key:
            root.left = self._push(root.left, key)
        elif key > root.key:
            root.right = self._push(root.right, key)
        else:
            root.count += 1
        root.height = 1 + max(self._getHeight(root.left), self._getHeight(root.right))
        balanceFactor = self._getBalanceFactor(root)
        if balanceFactor > 1:
            if key > root.left.key:
                root.left = self._rotateLeft(root.left)
            return self._rotateRight(root)
        if balanceFactor < -1:
            if key < root.right.key:
                root.right = self._rotateRight(root.right)
            return self._rotateLeft(root)
        return root

    def pop(self, key):
        self.root = self._delete_node(self.root, key)
    
    def _delete_node(self, root, key):
        if root is None:
            return root
        if key < root.key:
            root.left = self._delete_node(root.left, key)
        elif key > root.key:
            root.right = self._delete_node(root.right, key)
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp
            temp = self._find_min_node(root.right)
            root.key = temp.key
            root.right = self._delete_node(root.right, temp.key)
        self._update_height(root)
        balance = self._getBalanceFactor(root)
        if balance > 1 and self._getBalanceFactor(root.left) >= 0:
            return self._rotateRight(root)
        if balance < -1 and self._getBalanceFactor(root.right) <= 0:
            return self._rotateLeft(root)
        if balance > 1 and self._getBalanceFactor(root.left) < 0:
            root.left = self._rotateLeft(root.left)
            return self._rotateRight(root)
        if balance < -1 and self._getBalanceFactor(root.right) > 0:
            root.right = self._rotateRight(root.right)
            return self._rotateLeft(root)
        return root

    
    def max(self):
        if self.root is None:
            return None, 0
        curr = self.root
        while curr.right:
            curr = curr.right
        return curr.key, curr.count

    def _find_min_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current
    
    def _getHeight(self, node):
        if node is None:
            return 0
        return node.height

    def _update_height(self, node):
        node.height = max(self._getHeight(node.left), self._getHeight(node.right)) + 1


    def _getBalanceFactor(self, node):
        if node is None:
            return 0
        return self._getHeight(node.left) - self._getHeight(node.right)

    def _rotateLeft(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        z.height = 1 + max(self._getHeight(z.left), self._getHeight(z.right))
        y.height = 1 + max(self._getHeight(y.left), self._getHeight(y.right))
        return y

    def _rotateRight(self, z):
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3
        z.height = 1 + max(self._getHeight(z.left), self._getHeight(z.right))
        y.height = 1 + max(self._getHeight(y.left), self._getHeight(y.right))
        return y

    def find_value(self, data):
        return self._find_value(data, self.root)
    
    def _find_value(self, data, node):
        if node is None or node.key == data:
            return node
        if data < node.key:
            return self._find_value(data, node.left)
        return self._find_value(data, node.right)

    def preorder_traversal(self):
        if self.root is not None:
            self._preorder_traversal(self.root)

    def _preorder_traversal(self, node):
        if node is not None:
            print(node.key)
            self._preorder_traversal(node.left)
            self._preorder_traversal(node.right)

    def inorder_traversal(self):
        if self.root is not None:
            self._inorder_traversal(self.root)

    def _inorder_traversal(self, node):
        if node is not None:
            self._inorder_traversal(node.left)
            print(node.key)
            self._inorder_traversal(node.right)

    def postorder_traversal(self):
        if self.root is not None:
            self._postorder_traversal(self.root)
            
    def _postorder_traversal(self, node):
        if node is not None:
            self._postorder_traversal(node.left)
            self._postorder_traversal(node.right)
            print(node.key)

    def height(self):
        if self.root is None:
            return 0
        return self._height(self.root)
            
            
    def _height(self, node):
        if node is None:
            return 0
        else:
            left_height = self._height(node.left)
            right_height = self._height(node.right)
            return max(left_height, right_height) + 1

    def print(self):
        if self.root is not None:
            self.printTree(self.root,level=0)
        else:
            print("This tree is empty")

    def printTree(self,node,level=0):
        if node is not None:
            self.printTree(node.right,level+1)
            print("    "*level+str(node.key)+"<")
            self.printTree(node.left,level+1)

    def clear(self):
        if self.root is not None:
            self._clear(self.root)
        self.root=None

    def _clear(self,node):
        if node is not None:
            self._clear(node.left)
            self._clear(node.right)
            node.left=None
            node.right=None

    #Задание 1_5
    




# t=AVLTree()
# # t.print()
# # print(type(4))
# print("~~~~test_push~~~~")
# t.push(8)
# t.push(4)
# t.push(12)
# t.push(2)
# t.push(6)
# t.push(10)
# t.push(14)
# t.push(16)
# t.push(4)
# t.push(7)
# t.push(1)
# t.push(13)
# t.print()
# print("\n")
# print("~~~~test_pop~~~~")
# t.pop(6)
# t.pop(14)
# t.pop(4)
# t.pop(13)
# t.print()
# print("\n")
# print("~~~~test_find_value~~~~")
# node1=t.find_value(16)
# node2=t.find_value(7)
# node3=t.find_value(2)
# node4=t.find_value(4)
# node5=t.find_value(6)
# if node1:
#     print("Узел найден: ",node1.key)
# else:
#     print("Узел не найден")
# print("\n")
# print("\n")
# print("~~~~test_preorder_traversal~~~~")
# # Обход в прямом направлении
# print("Прямой обход:")
# t.preorder_traversal()
# print("\n")
# print("~~~~test_inorder_traversa~~~~")
# # Симметричный обход
# print("Симметричный обход:")
# t.inorder_traversal()
# print("\n")
# print("~~~~test_postorder_traversa~~~~")
# # Обход в обратном направлении
# print("Обратный обход:")
# t.postorder_traversal()
# print("\n")
# print("~~~~test_height~~~~")
# print("Высота дерева =", t.height())
# print("\n")
# print("~~~~test_max~~~~")
# # t2=RandomizedTree()
# max_t, count_t=t.max()
# print(" Максимальное значение =",max_t,"\n","Количество повторений =",count_t)
# print("\n")
# print("~~~~test_clear~~~~")
# t.clear()
# t.print()
# print("\n")




```

```python

```

```python
RED = 0
BLACK = 1

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None
        self.color = BLACK
        self.count = 1

class RedBlackTree:
    def __init__(self):
        self.root = None
        self.TNULL = Node(0)
        self.TNULL.color = BLACK

    def push(self, key):
        node = Node(key)
        node.left = self.TNULL
        node.right = self.TNULL
        if self.root is None:
            node.color = BLACK
            self.root = node
        else:
            self._insert_helper(node)

    def _insert_helper(self, node):
        y = None
        x = self.root
        while x != self.TNULL:
            y = x
            if node.key < x.key:
                x = x.left
            elif node.key > x.key:
                x = x.right
            else:
                x.count += 1
                return
        node.parent = y
        if y is None:
            self.root = node
        elif node.key < y.key:
            y.left = node
        else:
            y.right = node
        if node.parent is None:
            node.color = BLACK
            return
        if node.parent.parent is None:
            return
        self._fix_insert(node)

    def _fix_insert(self, node):
        while node.parent is not None and node.parent.color == RED:
            if node.parent == node.parent.parent.left:
                y = node.parent.parent.right
                if y is not None and y.color == RED:
                    node.parent.color = BLACK
                    y.color = BLACK
                    node.parent.parent.color = RED
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        node = node.parent
                        self._rotate_left(node)
                    node.parent.color = BLACK
                    node.parent.parent.color = RED
                    self._rotate_right(node.parent.parent)
            else:
                y = node.parent.parent.left
                if y is not None and y.color == RED:
                    node.parent.color = BLACK
                    y.color = BLACK
                    node.parent.parent.color = RED
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self._rotate_right(node)
                    node.parent.color = BLACK
                    node.parent.parent.color = RED
                    self._rotate_left(node.parent.parent)
        self.root.color = BLACK

    def pop(self, data):
        self.root = self._pop(data, self.root)
    
    def _pop(self, data, node):
        if node is None:
            return node
        if data < node.key:
            node.left = self._pop(data, node.left)
        elif data > node.key:
            node.right = self._pop(data, node.right)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                pop_node = self._find_minimum_node(node.right)
                node.key = pop_node.key
                node.right = self._pop(pop_node.key, node.right)
        return node

    def _find_minimum_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current
    
    def find_predecessor(self,node):
        while node.right:
            node = node.right
        return node
    
    def max(self):
        if self.root is None:
            return None, 0
        curr = self.root
        while curr.right != self.TNULL:
            curr = curr.right
        return curr.key, curr.count

    def _rotate_left(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.TNULL:
            y.left.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def _rotate_right(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.TNULL:
            y.right.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    def find_value(self, data):
        return self._find_value(data, self.root)
    
    def _find_value(self, data, node):
        if node is None or node.key == data:
            return node
        if data < node.key:
            return self._find_value(data, node.left)
        return self._find_value(data, node.right)

    def preorder_traversal(self):
        if self.root is not None:
            self._preorder_traversal(self.root)

    def _preorder_traversal(self, node):
        if node is not None:
            print(node.key)
            self._preorder_traversal(node.left)
            self._preorder_traversal(node.right)

    def inorder_traversal(self):
        if self.root is not None:
            self._inorder_traversal(self.root)

    def _inorder_traversal(self, node):
        if node is not None:
            self._inorder_traversal(node.left)
            print(node.key)
            self._inorder_traversal(node.right)

    def postorder_traversal(self):
        if self.root is not None:
            self._postorder_traversal(self.root)
            
    def _postorder_traversal(self, node):
        if node is not None:
            self._postorder_traversal(node.left)
            self._postorder_traversal(node.right)
            print(node.key)

    def height(self):
        if self.root is None:
            return 0
        return self._height(self.root)
            
            
    def _height(self, node):
        if node is None:
            return 0
        else:
            left_height = self._height(node.left)
            right_height = self._height(node.right)
            return max(left_height, right_height) + 1

    def print(self):
        if self.root is not None:
            self.printTree(self.root,level=0)
        else:
            print("This tree is empty")

    def printTree(self,node,level=0):
        if node is not None:
            self.printTree(node.right,level+1)
            print("    "*level+str(node.key)+"<")
            self.printTree(node.left,level+1)

    def clear(self):
        if self.root is not None:
            self._clear(self.root)
        self.root=None

    def _clear(self,node):
        if node is not None:
            self._clear(node.left)
            self._clear(node.right)
            node.left=None
            node.right=None



t=RedBlackTree()
# t.print()
# print(type(4))
# print("~~~~test_push~~~~")
# t.push(8)
# t.push(4)
# t.push(12)
# t.push(2)
# t.push(6)
# t.push(10)
# t.push(14)
# t.push(16)
# t.push(4)
# t.push(7)
# t.push(1)
# t.push(13)
# t.print()
# print("\n")
# print("~~~~test_pop~~~~")
# t.pop(6)
# t.pop(14)
# t.pop(4)
# t.pop(13)
# t.print()
# print("\n")
# print("~~~~test_find_value~~~~")
# node1=t.find_value(16)
# node2=t.find_value(7)
# node3=t.find_value(2)
# node4=t.find_value(4)
# node5=t.find_value(6)
# if node1:
#     print("Узел найден: ",node1.key)
# else:
#     print("Узел не найден")
# print("\n")
# print("\n")
# print("~~~~test_preorder_traversal~~~~")
# # Обход в прямом направлении
# print("Прямой обход:")
# t.preorder_traversal()
# print("\n")
# print("~~~~test_inorder_traversa~~~~")
# # Симметричный обход
# print("Симметричный обход:")
# t.inorder_traversal()
# print("\n")
# print("~~~~test_postorder_traversa~~~~")
# # Обход в обратном направлении
# print("Обратный обход:")
# t.postorder_traversal()
# print("\n")
# print("~~~~test_height~~~~")
# print("Высота дерева =", t.height())
# print("\n")
# print("~~~~test_max~~~~")
# # t2=RandomizedTree()
# max_t, count_t=t.max()
# print(" Максимальное значение =",max_t,"\n","Количество повторений =",count_t)
# print("\n")
# print("~~~~test_clear~~~~")
# t.clear()
# t.print()
# print("\n")


```

```python

```

```python
#Взаимодействие с пользователем

from IPython.display import clear_output
# clear_output()

# from time import sleep
# sleep(5.0)

def main():
    print("Введите 'menu', чтобы получить список всех доступных команд с их коротким описанием.")
    print("Введите 'tree', если хотите изменять дерево.")
    print("Введите 'find', если хотите найти элемент в дереве.")
    print("Введите 'heigth' чтобы узнать высоту дерева.")
    print("Введите 'max' для нахождения максимального элемента и количества его повторений.")
    print("Введите 'print' для просмотра дерева.")
    print("Введите 'type' чтобы выбрать тип дерева.")
    print("Введите 'stop' для завершения прошраммы.")

print("Пожалуйста введите 'start' чтобы начать.")
x=input()
clear_output()
while x!="start":
    print("Вы ввели неправильную команду. \nПожалуйста введите 'start' чтобы начать.")
    x=input()
    clear_output()
tree1=RandomizedTree()
tree2=AVLTree()
tree3=RedBlackTree()
print("Добро пожаловать!")
while x!="stop":
    print("Выберети тип дерева:")
    print("Введите '1' чтобы работать с рандомизированным деревом.")
    print("Введите '2' чтобы работать с AVL деревом.")
    print("Введите '3' чтобы работать с черно-красным деревом.")
    x=input()
    clear_output()
    if x=="1":
        while x!="type" and x!="stop":
            main()
            x=input()
            clear_output()
            if x=="menu":
                while x!="end":
                    print("Комонда 'menu': вызывается из главной страницы. Она позволяет просмотреть список доступных для пользователя на главной странице команд и дает их короткое описание для понимания за что отвечает каждый раздел.")
                    print("Чтобы выйти из этого раздела, необходимо ввести команду 'end'. \n")
                    print("Команда 'list': позволяет добавлять элементы в стек, удалять элементы, очищать стек. Невозможно добавить или удалить элемент за пределами списка")
                    print("Команда 'empty': позволяет проверить пустой стек или нет. Если стек пуст выведется True, иначе - False.")
                    print("Команда 'size': позволяет узнать количество элементов в стеке.")
                    print("Команда 'print': ввыводит элементы списка.")
                    print("Команда 'type': позволяет выбрать тип дерева.")
                    print("Команда 'stop': позволяет завершить работу программы.")
                    x=input()
                    clear_output()
            if x=="tree":
                while x!="end":
                    print("Введите 'add', чтобы добавить элементы в дереве.")
                    print("Введите 'delete', если хотите удалить элементы из дерева, если такого элемента нет, то ничего не произойдет.")
                    print("Введите 'clear', если хотите очистить дерево.")
                    print("Введите 'end', чтобы выйти из этого раздела.")
                    x=input()
                    clear_output()
                    if x=="add":
                        while x!="end":
                            print("Введите количество элементов, которое хотите добавить в дерево.")
                            count=int(input())
                            for i in range(0,count):
                                print("Введите элемент")
                                element=input()
                                tree1.push(element)
                            print("Элементы добавлены.")
                            print("Введите 'end', чтобы выйти.")
                            x=input()
                            clear_output()
                    if x=="delete":
                        while x!="end":
                            print("Так ваше дерево выглядит сейчас.")
                            tree1.print()
                            print("Введите количество элементов, которое хотите удалить из дерева.")
                            count=int(input())
                            for i in range(0,count):
                                print("Введите элемент, который хотите удалить.")
                                element=input()
                                if tree1.find_value(element):
                                    tree1.pop(element)
                                else:
                                    print("Такого элемента не существует в этом дереве.")
                            print("Элементы удалены.")
                            print("Теперь ваш стек выглядит так.")
                            tree1.print()
                            print("Введите 'end', чтобы выйти.")
                            x=input()
                            clear_output()
                    if x=="clear":
                        while x!="end":
                            print("Вы точно хотите очистить дерево? Если да введите 'y', иначе 'n'.")
                            ok=input()
                            if ok=="y":
                                tree1.clear()
                                print("Ваше дерево очищено.")
                            print("Введите 'end', чтобы выйти.")
                            x=input()
                            clear_output()
            if x=="max":
                while x!="end":
                    max_t, count_t=tree1.max()
                    print(" Максимальное значение =",max_t,"\n","Количество повторений =",count_t)
                    print("Так выглядит ваше дерево.")
                    tree1.print()
                    print("Введите 'end', чтобы выйти.")
                    x=input()
                    clear_output()
            if x=="height":
                while x!="end":
                    print("Высота дерева =", tree1.height())
                    print("Так выглядит ваше дерево.")
                    tree1.print()
                    print("Введите 'end', чтобы выйти.")
                    x=input()
                    clear_output()
            if x=="find":
                while x!="end":
                    print("Введите элемент, который хотите найти.")
                    value=input()
                    node=tree1.find_value(value)
                    if node:
                        print("Узел найден: ",node.data)
                    else:
                        print("Узел не найден")
                    print("Введите 'end', чтобы выйти.")
                    x=input()
                    clear_output()
            if x=="print":
                while x!="end":
                    print("Введите 'print' чтобы распечатать дерево.")
                    print("Введите 'preorder' чтобы распечатать дерево обходом в прямом направлении.")
                    print("Введите 'inorder' чтобы распечатать дерево обходом в симметричном направлении.")
                    print("Введите 'postorder' чтобы распечатать дерево обходом в обратном направлении.")
                    print("Введите 'end', чтобы выйти.")
                    x=input()
                    clear_output()
                    if x=="print":
                        while x!="end":
                            print("Сейчас ваше дерево выглядит так.")
                            tree1.print()
                            print("Введите 'end', чтобы выйти.")
                            x=input()
                            clear_output()
                    if x=="preorder":
                        while x!="end":
                            print("Сейчас ваше дерево выглядит так.")
                            tree1.print()
                            print("Прямой обход:")
                            tree1.preorder_traversal()
                            print("Введите 'end', чтобы выйти.")
                            x=input()
                            clear_output()
                    if x=="inorder":
                        while x!="end":
                            print("Сейчас ваше дерево выглядит так.")
                            tree1.print()
                            print("Симметричный обход:")
                            tree1.inorder_traversal()
                            print("Введите 'end', чтобы выйти.")
                            x=input()
                            clear_output()
                    if x=="postorder":
                        while x!="end":
                            print("Сейчас ваше дерево выглядит так.")
                            tree1.print()
                            print("Обратный обход:")
                            tree1.postorder_traversal()
                            print("Введите 'end', чтобы выйти.")
                            x=input()
                            clear_output()
    if x=="2":
        while x!="type" and x!="stop":
            main()
            x=input()
            clear_output()
            if x=="menu":
                while x!="end":
                    print("Комонда 'menu': вызывается из главной страницы. Она позволяет просмотреть список доступных для пользователя на главной странице команд и дает их короткое описание для понимания за что отвечает каждый раздел.")
                    print("Чтобы выйти из этого раздела, необходимо ввести команду 'end'. \n")
                    print("Команда 'list': позволяет добавлять элементы в стек, удалять элементы, очищать стек. Невозможно добавить или удалить элемент за пределами списка")
                    print("Команда 'empty': позволяет проверить пустой стек или нет. Если стек пуст выведется True, иначе - False.")
                    print("Команда 'size': позволяет узнать количество элементов в стеке.")
                    print("Команда 'print': ввыводит элементы списка.")
                    print("Команда 'type': позволяет выбрать тип дерева.")
                    print("Команда 'stop': позволяет завершить работу программы.")
                    x=input()
                    clear_output()
            if x=="tree":
                while x!="end":
                    print("Введите 'add', чтобы добавить элементы в дереве.")
                    print("Введите 'delete', если хотите удалить элементы из дерева, если такого элемента нет, то ничего не произойдет.")
                    print("Введите 'clear', если хотите очистить дерево.")
                    print("Введите 'end', чтобы выйти из этого раздела.")
                    x=input()
                    clear_output()
                    if x=="add":
                        while x!="end":
                            print("Введите количество элементов, которое хотите добавить в дерево.")
                            count=int(input())
                            for i in range(0,count):
                                print("Введите элемент")
                                element=input()
                                tree2.push(element)
                            print("Элементы добавлены.")
                            print("Введите 'end', чтобы выйти.")
                            x=input()
                            clear_output()
                    if x=="delete":
                        while x!="end":
                            print("Так ваше дерево выглядит сейчас.")
                            tree2.print()
                            print("Введите количество элементов, которое хотите удалить из дерева.")
                            count=int(input())
                            for i in range(0,count):
                                print("Введите элемент, который хотите удалить.")
                                element=input()
                                if tree2.find_value(element):
                                    tree2.pop(element)
                                else:
                                    print("Такого элемента не существует в этом дереве.")
                            print("Элементы удалены.")
                            print("Теперь ваш стек выглядит так.")
                            tree2.print()
                            print("Введите 'end', чтобы выйти.")
                            x=input()
                            clear_output()
                    if x=="clear":
                        while x!="end":
                            print("Вы точно хотите очистить дерево? Если да введите 'y', иначе 'n'.")
                            ok=input()
                            if ok=="y":
                                tree2.clear()
                                print("Ваше дерево очищено.")
                            print("Введите 'end', чтобы выйти.")
                            x=input()
                            clear_output()
            if x=="max":
                while x!="end":
                    max_t, count_t=tree2.max()
                    print(" Максимальное значение =",max_t,"\n","Количество повторений =",count_t)
                    print("Так выглядит ваше дерево.")
                    tree1.print()
                    print("Введите 'end', чтобы выйти.")
                    x=input()
                    clear_output()
            if x=="height":
                while x!="end":
                    print("Высота дерева =", tree2.height())
                    print("Так выглядит ваше дерево.")
                    tree2.print()
                    print("Введите 'end', чтобы выйти.")
                    x=input()
                    clear_output()
            if x=="find":
                while x!="end":
                    print("Введите элемент, который хотите найти.")
                    value=input()
                    node=tree2.find_value(value)
                    if node:
                        print("Узел найден: ",node.key)
                    else:
                        print("Узел не найден")
                    print("Введите 'end', чтобы выйти.")
                    x=input()
                    clear_output()
            if x=="print":
                while x!="end":
                    print("Введите 'print' чтобы распечатать дерево.")
                    print("Введите 'preorder' чтобы распечатать дерево обходом в прямом направлении.")
                    print("Введите 'inorder' чтобы распечатать дерево обходом в симметричном направлении.")
                    print("Введите 'postorder' чтобы распечатать дерево обходом в обратном направлении.")
                    print("Введите 'end', чтобы выйти.")
                    x=input()
                    clear_output()
                    if x=="print":
                        while x!="end":
                            print("Сейчас ваше дерево выглядит так.")
                            tree2.print()
                            print("Введите 'end', чтобы выйти.")
                            x=input()
                            clear_output()
                    if x=="preorder":
                        while x!="end":
                            print("Сейчас ваше дерево выглядит так.")
                            tree2.print()
                            print("Прямой обход:")
                            tree2.preorder_traversal()
                            print("Введите 'end', чтобы выйти.")
                            x=input()
                            clear_output()
                    if x=="inorder":
                        while x!="end":
                            print("Сейчас ваше дерево выглядит так.")
                            tree2.print()
                            print("Симметричный обход:")
                            tree2.inorder_traversal()
                            print("Введите 'end', чтобы выйти.")
                            x=input()
                            clear_output()
                    if x=="postorder":
                        while x!="end":
                            print("Сейчас ваше дерево выглядит так.")
                            tree2.print()
                            print("Обратный обход:")
                            tree2.postorder_traversal()
                            print("Введите 'end', чтобы выйти.")
                            x=input()
                            clear_output()
    if x=="3":
        while x!="type" and x!="stop":
            main()
            x=input()
            clear_output()
            if x=="menu":
                while x!="end":
                    print("Комонда 'menu': вызывается из главной страницы. Она позволяет просмотреть список доступных для пользователя на главной странице команд и дает их короткое описание для понимания за что отвечает каждый раздел.")
                    print("Чтобы выйти из этого раздела, необходимо ввести команду 'end'. \n")
                    print("Команда 'list': позволяет добавлять элементы в стек, удалять элементы, очищать стек. Невозможно добавить или удалить элемент за пределами списка")
                    print("Команда 'empty': позволяет проверить пустой стек или нет. Если стек пуст выведется True, иначе - False.")
                    print("Команда 'size': позволяет узнать количество элементов в стеке.")
                    print("Команда 'print': ввыводит элементы списка.")
                    print("Команда 'type': позволяет выбрать тип дерева.")
                    print("Команда 'stop': позволяет завершить работу программы.")
                    x=input()
                    clear_output()
            if x=="tree":
                while x!="end":
                    print("Введите 'add', чтобы добавить элементы в дереве.")
                    print("Введите 'delete', если хотите удалить элементы из дерева, если такого элемента нет, то ничего не произойдет.")
                    print("Введите 'clear', если хотите очистить дерево.")
                    print("Введите 'end', чтобы выйти из этого раздела.")
                    x=input()
                    clear_output()
                    if x=="add":
                        while x!="end":
                            print("Введите количество элементов, которое хотите добавить в дерево.")
                            count=int(input())
                            for i in range(0,count):
                                print("Введите элемент")
                                element=input()
                                tree3.push(element)
                            print("Элементы добавлены.")
                            print("Введите 'end', чтобы выйти.")
                            x=input()
                            clear_output()
                    if x=="delete":
                        while x!="end":
                            print("Так ваше дерево выглядит сейчас.")
                            tree3.print()
                            print("Введите количество элементов, которое хотите удалить из дерева.")
                            count=int(input())
                            for i in range(0,count):
                                print("Введите элемент, который хотите удалить.")
                                element=input()
                                if tree3.find_value(element):
                                    tree3.pop(element)
                                else:
                                    print("Такого элемента не существует в этом дереве.")
                            print("Элементы удалены.")
                            print("Теперь ваш стек выглядит так.")
                            tree3.print()
                            print("Введите 'end', чтобы выйти.")
                            x=input()
                            clear_output()
                    if x=="clear":
                        while x!="end":
                            print("Вы точно хотите очистить дерево? Если да введите 'y', иначе 'n'.")
                            ok=input()
                            if ok=="y":
                                tree3.clear()
                                print("Ваше дерево очищено.")
                            print("Введите 'end', чтобы выйти.")
                            x=input()
                            clear_output()
            if x=="max":
                while x!="end":
                    max_t, count_t=tree3.max()
                    print(" Максимальное значение =",max_t,"\n","Количество повторений =",count_t)
                    print("Так выглядит ваше дерево.")
                    tree3.print()
                    print("Введите 'end', чтобы выйти.")
                    x=input()
                    clear_output()
            if x=="height":
                while x!="end":
                    print("Высота дерева =", tree3.height())
                    print("Так выглядит ваше дерево.")
                    tree3.print()
                    print("Введите 'end', чтобы выйти.")
                    x=input()
                    clear_output()
            if x=="find":
                while x!="end":
                    print("Введите элемент, который хотите найти.")
                    value=input()
                    node=tree3.find_value(value)
                    if node:
                        print("Узел найден: ",node.key)
                    else:
                        print("Узел не найден")
                    print("Введите 'end', чтобы выйти.")
                    x=input()
                    clear_output()
            if x=="print":
                while x!="end":
                    print("Введите 'print' чтобы распечатать дерево.")
                    print("Введите 'preorder' чтобы распечатать дерево обходом в прямом направлении.")
                    print("Введите 'inorder' чтобы распечатать дерево обходом в симметричном направлении.")
                    print("Введите 'postorder' чтобы распечатать дерево обходом в обратном направлении.")
                    print("Введите 'end', чтобы выйти.")
                    x=input()
                    clear_output()
                    if x=="print":
                        while x!="end":
                            print("Сейчас ваше дерево выглядит так.")
                            tree3.print()
                            print("Введите 'end', чтобы выйти.")
                            x=input()
                            clear_output()
                    if x=="preorder":
                        while x!="end":
                            print("Сейчас ваше дерево выглядит так.")
                            tree3.print()
                            print("Прямой обход:")
                            tree3.preorder_traversal()
                            print("Введите 'end', чтобы выйти.")
                            x=input()
                            clear_output()
                    if x=="inorder":
                        while x!="end":
                            print("Сейчас ваше дерево выглядит так.")
                            tree3.print()
                            print("Симметричный обход:")
                            tree3.inorder_traversal()
                            print("Введите 'end', чтобы выйти.")
                            x=input()
                            clear_output()
                    if x=="postorder":
                        while x!="end":
                            print("Сейчас ваше дерево выглядит так.")
                            tree3.print()
                            print("Обратный обход:")
                            tree3.postorder_traversal()
                            print("Введите 'end', чтобы выйти.")
                            x=input()
                            clear_output()
print("Программа завершина.\nВсего доброго.")







```

```python

```

```python

```

```python

```
