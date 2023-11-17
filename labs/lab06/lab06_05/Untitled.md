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

<!-- #region -->


# Отчет

## Лабораторная работа №6

### Линейный однонаправленный список

### Цель работы:

Изучение структуры данных «Двоичное дерево поиска», а также основных операций над ним.

### Задачи:

1. Реализовать программу, выполняющую стандартный набор операций над двоичным деревом поиска:

- формирование бинарного дерева;
- обход (прямой, симметричный, обратный) бинарного дерева;
- удаление заданной вершины из бинарного дерева;
- поиск заданной вершины в бинарном дереве (по значению);
- печать бинарного дерева на экран;
- проверка пустоты бинарного дерева;
- определение высоты бинарного дерева.

2. Реализовать приложение, для работы с бинарным деревом поиска, которое реализует следующий набор действий:

а) инициализация пустого дерева;

б) организация диалогового цикла с пользователем;

3 Реализовать индивидуальные задание.

- Найти максимальный элемент бинарного дерева и количество повторений максимального элемента в данном дереве.

### Листинг программного кода с описанием

class Node:
    def __init__(self,data)

class BinaryTree:
    def __init__(self)
        
    def push(self, data) # Добавляет элемент в стек
    
    def pop(self) # Удаляет первй элемент стек
    
    def reverse(self) # Переворачивает список

    def print(self) # Выводит список

    def clear(self) # Очищает список

#Взаимодействие с пользователем

- while x!="start" # Просит ввести start пока пользователь его не введет

- while x!="stop" # программа работает пока пользователь не введет stop

    main() # печатает описание команд
  
    if x=="menu" # показывает меню команд
  
        while x!="end" # возвращает в главное меню
  
    if x=="tree" # содержит операции работы над деревом
  
        while x!="end" # возвращает в главное меню
  
            if x=="add" # содержит операции добавления элемента
  
                while x!="end" # возвращает в главное меню

            if x=="delete" # содержит команды удаления
  
                while x!="end" # возвращает в главное меню
  
            if x=="clear" # очищает список
  
                while x!="end" # возвращает в главное меню

    if x=="max" # находит максимальный элемент в дереве
  
        while x!="end" # возвращает в главное меню

    if x=="find" # находит элемент в дереве
  
        while x!="end" # возвращает в главное меню
 
    if x=="height" # ищет высоту дерева
  
        while x!="end" # возвращает в главное меню

    if x=="print" # печатает дерево разными способами

        while x!="end" # возвращает в главное меню
          
            if x=="print" # печатает дерево

                while x!="end" # возвращает в главное меню
                   
            if x=="preorder": # Прямой обход
                
                while x!="end" # возвращает в главное меню
                
            if x=="inorder": # Смметричный обход
                    
                while x!="end" # возвращает в главное меню
                    
            if x=="postorder": # Обратный обход
                    
                while x!="end" # возвращает в главное меню

### Ответы на контрольные вопросы
1. С чем связана популярность использования деревьев в программировании?

Деревья являются одной из наиболее эффективных структур данных для хранения и организации информации.

2. Можно ли список отнести к деревьям?

Нет, список не является деревом. Список - это упорядоченная коллекция элементов, где каждый элемент имеет свой номер или индекс. В списках элементы могут быть связаны друг с другом только на основе их позиции или индекса.
Дерево же представляет собой иерархическую структуру данных, состоящую из узлов (вершин) и ребер (связей) между ними. Каждый узел в дереве может иметь родителя и ноль или более потомков. Дерево обеспечивает более сложные и гибкие способы организации данных и связей между ними.
Хотя список и дерево могут использоваться для представления и организации данных, они имеют различные свойства и функции, поэтому не могут рассматриваться как одно и то же.

3. Какие данные содержат адресные поля элемента бинарного дерева?

Каждый элемент бинарного дерева содержит два адресных поля, которые указывают на его потомков. Эти поля называются "левым потомком" и "правым потомком".
- Левый потомок: Это адресное поле, которое указывает на левого потомка элемента. Левый потомок находится "ниже" родительского элемента по отношению к иерархии дерева.
- Правый потомок: Это адресное поле, которое указывает на правого потомка элемента. Правый потомок также находится "ниже" родительского элемента в иерархии дерева.

4. Что такое дерево, двоичное дерево, поддерево?

- Дерево - это иерархическая структура данных, состоящая из вершин (узлов) и ребер (связей) между ними. Каждая вершина может иметь ноль или более потомков, то есть других вершин, которые связаны с ней. Есть одна вершина, из которой начинаются все связи и которая называется корневой вершиной. Каждая вершина может быть связана с одной родительской вершиной, кроме корневой, которая не имеет родителя.
- Двоичное дерево - это особый тип дерева, где каждая вершина может иметь не более двух потомков: левый потомок и правый потомок. Левый потомок находится слева от родительской вершины, а правый потомок - справа от нее.
- Поддерево - это часть дерева, которая включает вершину и все ее потомки и связи между ними. Вершина, включая всех ее потомков, называется корневой вершиной поддерева. Поддерево может быть любым фрагментом иерархической структуры дерева.

5. Как рекурсивно определяется дерево?
  
Дерево состоит из вершины (корня) и некоторого количества поддеревьев, которые являются деревьями в себе. Поддеревья соединены с корнем вершины. Каждое поддерево определяется таким же рекурсивным правилом.

6. Какие основные понятия связываются с деревьями?

- Корень (Root): Корень дерева - это вершина, которая служит начальной точкой для всего дерева. Она не имеет родителя и является вершиной самого верхнего уровня иерархии.
- Вершина (Node): Вершина (узел) - это элемент дерева, который содержит некоторую информацию (значение) и связан с другими вершинами (потомками или родителями) через ребра.
- Ребро (Edge): Ребро - это связь между двумя вершинами в дереве. Ребро может быть направленным или ненаправленным, в зависимости от типа дерева.
- Потомок (Child): Потомок - это вершина, которая связана с другой вершиной (родителем) напрямую нижнего уровня. Родителю может соответствовать несколько потомков.
- Родитель (Parent): Родитель - это вершина, от которой исходит ребро, связывающее ее с другой вершиной (потомком). Каждая вершина, за исключением корня, может иметь одного родителя.
- Потомки (Children): Потомки - это множество вершин, которые связаны с родительской вершиной. У одной вершины может быть любое количество потомков, включая ноль.
- Путь (Path): Путь представляет собой последовательность ребер, связывающих вершины в дереве. Он определяет путь от одной вершины к другой.
- Глубина (Depth): Глубина дерева - это количество ребер на пути от корневой вершины до конкретной вершины.

7. Какие основные операции характерны при использовании деревьев?
  
- Поиск элементов в дереве
- Добавление элемента в дерево
- Удаление элемента из дерева
- Обход дерева.
  
8. Как программно реализуется алгоритм операции обхода дерева?
9. Как программно реализуется алгоритм операции добавления элемента в дерево?
10. Как программно реализуется алгоритм операции удаления элемента из дерева?
11. Как программно реализуется алгоритм операции поиска элемента в дереве?


<!-- #endregion -->

```python
class Node:
    def __init__(self, data):
        self.left=None
        self.right=None
        self.data=data

class BinaryTree:
    def __init__(self):
        self.root = None
    
    def push(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._push(data, self.root)
    
    def _push(self, data, node):
        if data < node.data:
            if node.left is None:
                node.left = Node(data)
            else:
                self._push(data, node.left)
        else:
            if node.right is None:
                node.right = Node(data)
            else:
                self._push(data, node.right)

    def pop(self, data):
        self.root = self._pop(data, self.root)
    
    def _pop(self, data, node):
        if node is None:
            return node
        if data < node.data:
            node.left = self._pop(data, node.left)
        elif data > node.data:
            node.right = self._pop(data, node.right)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                pop_node = self._find_minimum_node(node.right)
                node.data = pop_node.data
                node.right = self._pop(pop_node.data, node.right)
        return node

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
        
            



t=BinaryTree()
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
# t.pop(13)
# t.pop(14)
# t.pop(1)
# t.pop(6)
# t.print()
# print("\n")
# print("~~~~test_find_value~~~~")
# node1=t.find_value(16)
# node2=t.find_value(7)
# node3=t.find_value(2)
# node4=t.find_value(4)
# node5=t.find_value(6)
# if node5:
#     print("Узел найден: ",node5.data)
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
# t2=BinaryTree()
# max_t, count_t=t2.max()
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
    print("Введите 'stop' для завершения прошраммы.")

print("Пожалуйста введите 'start' чтобы начать.")
x=input()
clear_output()
while x!="start":
    print("Вы ввели неправильную команду. \nПожалуйста введите 'start' чтобы начать.")
    x=input()
    clear_output()
tree1=BinaryTree()
print("Добро пожаловать!")
while x!="stop":
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
print("Программа завершина.\nВсего доброго.")







```

```python

```
