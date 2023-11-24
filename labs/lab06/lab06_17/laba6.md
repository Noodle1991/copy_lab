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
<h1> ОТЧЕТ </h1>
<h3> Лабораторная работа №6 <br> <br>
    «Двоичные деревья поиска (Binary Search Tree)» </h3>
<br>
<h4> Цель работы: </h4>
Изучение структуры данных «Двоичное дерево поиска», а также основных операций над ним.
<br>
<br>
<h4> Постановка задачи: </h4>

1. Написать собственную реализацию двоичного дерева поиска в виде класса. Приэтом каждая его операция должна быть реализована как метод класса и добавлению/удалению элемента должна предшествовать проверка возможности выполнения этих операций.
2. Реализовать программу, выполняющую стандартный набор операций над двоичным деревом поиска:
    * формирование бинарного дерева;
    * обход (прямой, симметричный, обратный) бинарного дерева;
    * удаление заданной вершины из бинарного дерева;
    * поиск заданной вершины в бинарном дереве (по значению);
    * печать бинарного дерева на экран;
    * проверка пустоты бинарного дерева;
    * определение высоты бинарного дерева.
3. Реализовать приложение, для работы с бинарным деревом поиска, которое реализует следующий набор действий:
    * инициализация пустого бинарного дерева;
    * организация диалогового цикла с пользователем;
<br>
<br>
<h4> Code Listing: </h4>

```python
class Node: 
    def __init__(self, data, left = None, right = None)

class BinarySearchTree:
    
    def __init__(self) #инициализация дерева

    def __str__(self) #вывод дерева

    def print(self, root) #вспомогательная функция для вывода дерева
    
    def is_empty(self, root) #проверка дерева на пустоту
    
    def add(self, data) #добавление элемента в дерево
    
    def add_root(self, root, data) #вспомогательная функция для добавления элемента в дерево
    
    def preorder_traversal(self) #прямой обход дерева
    
    def preorder_traversal_root(self, root, result) #вспомогательная функция для прямого обхода дерева
    
    def inorder_traversal(self) #симметричный обход дерева
    
    def inorder_traversal_root(self, root, result) #вспомогательная функция для симметричного обхода дерева
    
    def postorder_traversal(self) #обратный обход дерева
    
    def postorder_traversal_root(self, root, result) #вспомогательная функция для обратного обхода дерева
    
    def find_item(self, data): #поиск элемента по значению в дереве
    
    def find_item_root(self, root, data, path) #вспомогательная функция для поиска элемента по значению в дереве
    
    def remove(self, data) #удаление элемента по значению из дерева
    
    def remove_root(self, root, data) #вспомогательная функция для удаления элемента по значению из дерева
    
    def depth(self, root, level) #подсчет глубины дерева
    
    #additions
    def clear(self): #очистка дерева
    
    def clear_root(self, root) #вспомогательная функция для очистки дерева

    #individuals
    def product_of_elements_even_levels(self) #произведение элементов всех четных уровней

    def product_of_elements_even_levels_root(self, root, result, flag) #вспомогательная функция для произведения элементов всех четных уровней
    
#Взаимодействие с пользователем
x = input("...")
while True:
    ///код
    match x:
        case "menu":
            ///код
        
        case "show":
            ///код

        case "is empty":
            ///код
            
        case "add":
            ///код

        case "traversal":
            ///код
            
        case "find item":
            ///код
            
        case "remove":
            ///код
        
        case "depth":
            ///код
            
        case "product evel levels":
            ///код
            
        case "clear":
            ///код
        
        case "stop":
            ///код
    ///код
```
<br>
<h4> Выводы </h4>
В ходе лабораторной работы была изучена структура данных «двоичноe деревo поиска», написана собственнаяя реализация двоичного дерева поиска в виде класса таким образом, что каждая его операция является методом класса. Реализована программа, выполняющая стандартный набор операций с двоичным деревом поиска и приложение, которое осуществляет диалоговый цикл с пользователем.
<br>
<br>
<h4> Ответы на контрольные вопросы </h4>

1. *С чем связана популярность использования деревьев в программировании?* <br>
Деревья являются одной из наиболее эффективных структур данных для хранения и организации информации.
2. *Можно ли список отнести к деревьям?* <br>
Нет, список не является деревом. Список - это упорядоченная коллекция элементов, где каждый элемент имеет свой номер или индекс. В списках элементы могут быть связаны друг с другом только на основе их позиции или индекса. <br>
Дерево же представляет собой иерархическую структуру данных, состоящую из узлов (вершин) и ребер (связей) между ними. Каждый узел в дереве может иметь родителя и ноль или более потомков. Дерево обеспечивает более сложные и гибкие способы организации данных и связей между ними. <br>
Хотя список и дерево могут использоваться для представления и организации данных, они имеют различные свойства и функции, поэтому не могут рассматриваться как одно и то же.
4. *Какие данные содержат адресные поля элемента бинарного дерева?* <br>
Каждый элемент бинарного дерева содержит два адресных поля, которые указывают на его потомков. Эти поля называются "левым потомком" и "правым потомком". <br>
Левый потомок: Это адресное поле, которое указывает на левого потомка элемента. Левый потомок находится "ниже" родительского элемента по отношению к иерархии дерева. <br>
Правый потомок: Это адресное поле, которое указывает на правого потомка элемента. Правый потомок также находится "ниже" родительского элемента в иерархии дерева. <br>
5. *Что такое дерево, двоичное дерево, поддерево?* <br>
Дерево - это иерархическая структура данных, состоящая из вершин (узлов) и ребер (связей) между ними. Каждая вершина может иметь ноль или более потомков, то есть других вершин, которые связаны с ней. Есть одна вершина, из которой начинаются все связи и которая называется корневой вершиной. Каждая вершина может быть связана с одной родительской вершиной, кроме корневой, которая не имеет родителя. <br>
Двоичное дерево - это особый тип дерева, где каждая вершина может иметь не более двух потомков: левый потомок и правый потомок. Левый потомок находится слева от родительской вершины, а правый потомок - справа от нее. <br>
Поддерево - это часть дерева, которая включает вершину и все ее потомки и связи между ними. Вершина, включая всех ее потомков, называется корневой вершиной поддерева. Поддерево может быть любым фрагментом иерархической структуры дерева.
6. *Как рекурсивно определяется дерево?* <br>
Дерево состоит из вершины (корня) и некоторого количества поддеревьев, которые являются деревьями в себе. Поддеревья соединены с корнем вершины. Каждое поддерево определяется таким же рекурсивным правилом.
7. *Какие основные понятия связываются с деревьями?* <br>
    * Корень (Root): Корень дерева - это вершина, которая служит начальной точкой для всего дерева. Она не имеет родителя и является вершиной самого верхнего уровня иерархии.
    * Вершина (Node): Вершина (узел) - это элемент дерева, который содержит некоторую информацию (значение) и связан с другими вершинами (потомками или родителями) через ребра.
    * Ребро (Edge): Ребро - это связь между двумя вершинами в дереве. Ребро может быть направленным или ненаправленным, в зависимости от типа дерева.
    * Потомок (Child): Потомок - это вершина, которая связана с другой вершиной (родителем) напрямую нижнего уровня. Родителю может соответствовать несколько потомков.
    * Родитель (Parent): Родитель - это вершина, от которой исходит ребро, связывающее ее с другой вершиной (потомком). Каждая вершина, за исключением корня, может иметь одного родителя.
    * Потомки (Children): Потомки - это множество вершин, которые связаны с родительской вершиной. У одной вершины может быть любое количество потомков, включая ноль.
    * Путь (Path): Путь представляет собой последовательность ребер, связывающих вершины в дереве. Он определяет путь от одной вершины к другой.
    * Глубина (Depth): Глубина дерева - это количество ребер на пути от корневой вершины до конкретной вершины.
8. *Какие основные операции характерны при использовании деревьев?* <br>
    * Поиск элементов в дереве
    * Добавление элемента в дерево
    * Удаление элемента из дерева
    * Обход дерева.
9. *Как программно реализуется алгоритм операции обхода дерева?* <br>
```python
def preorder_traversal(self): #прямой обход дерева
    if self.is_empty(self.root):
        raise TypeError("Empty tree")
    result = []
    self.preorder_traversal_root(self.root, result)
    return result

def preorder_traversal_root(self, root, result):
    if not self.is_empty(root):
        result.append(root.data)
        self.preorder_traversal_root(root.left, result)
        self.preorder_traversal_root(root.right, result)
        return result
        
def inorder_traversal(self): #симметричный обход дерева
    if self.is_empty(self.root):
        raise TypeError("Empty tree")
    result = []
    self.inorder_traversal_root(self.root, result)
    return result

def inorder_traversal_root(self, root, result):
    if not self.is_empty(root):
        self.inorder_traversal_root(root.left, result)
        result.append(root.data)
        self.inorder_traversal_root(root.right, result)
        return result
        
def postorder_traversal(self): #обратный обход дерева
    if self.is_empty(self.root):
        raise TypeError("Empty tree")
    result = []
    self.postorder_traversal_root(self.root, result)
    return result

def postorder_traversal_root(self, root, result):
    if not self.is_empty(root):
        self.postorder_traversal_root(root.left, result)
        self.postorder_traversal_root(root.right, result)
        result.append(root.data)
        return result
```
10. *Как программно реализуется алгоритм операции добавления элемента в дерево?* <br>
```python
def add(self, data):
    if not data.isdigit():
        raise TypeError("Only numbers can be added to the tree")
    data = int(data)
    if self.is_empty(self.root):
        self.root = Node(data)
    else:
        self.add_root(self.root, data)
    
def add_root(self, root, data):
    if root.data == data:
        raise ValueError("Such an element has already been added to the tree")
    elif data < root.data:
        if self.is_empty(root.left):
            root.left = Node(data)
        else:
            self.add_root(root.left, data)
    else:
        if self.is_empty(root.right):
            root.right = Node(data)
        else:
            self.add_root(root.right, data)
```
12. *Как программно реализуется алгоритм операции удаления элемента из дерева?* <br>
```python
def remove(self, data):
    if not data.isdigit():
        raise ValueError("Only numbers can be removed from the tree")
    data = int(data)
    if self.is_empty(self.root):
        raise TypeError("Empty tree")
    return self.remove_root(self.root, data)
    
def remove_root(self, root, data):
    if self.is_empty(root):
        return root
    if data < root.data:
        root.left = self.remove_root(root.left, data)
    elif data > root.data:
        root.right = self.remove_root(root.right, data)
    else:
        if self.is_empty(root.right):
            return root.left
        elif self.is_empty(root.left):
            return root.right
        else:
            temp = root.right
            while not self.is_empty(temp.left):
                temp = temp.left
            root.data = temp.data
        root.right = self.remove_root(root.right, temp.data)
return root
```
13. *Как программно реализуется  алгоритм операции поиска элемента в дереве?* <br>
```python
def find_item(self, data):
    if self.is_empty(self.root):
        raise TypeError("Empty tree")
    if not data.isdigit():
        raise ValueError("Only integers can be searched in the tree")
    data = int(data)
    path = "root"
    if self.root.data == data:
        return path
    path = self.find_item_root(self.root, data, path)
    return path

def find_item_root(self, root, data, path):
    if self.is_empty(root):
        raise Exception("ErRoR 404")
    if root.data == data:
        return path
    if data < root.data:
        path = self.find_item_root(root.left, data, path + "->left")
    else:
        path = self.find_item_root(root.right, data, path + "->right")
    return path
```
<!-- #endregion -->

```python
class Node:
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def __str__(self):
        if self.is_empty(self.root):
            return "binary search tree is empty: " + str(self.root)
        else:
            lines, *_ = self.print(self.root)
            for line in lines:
                print(line)
            return ""

    def print(self, root):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if self.is_empty(root.right) and self.is_empty(root.left):
            line = "%s" % root.data
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle
        # Only left child.
        if self.is_empty(root.right):
            lines, n, p, x = self.print(root.left)
            s = "%s" % root.data
            u = len(s)
            first_line = (x + 1) * " " + (n - x - 1) * "_" + s
            second_line = x * " " + "/" + (n - x - 1 + u) * " "
            shifted_lines = [line + u * " " for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2
        # Only right child.
        if self.is_empty(root.left):
            lines, n, p, x = self.print(root.right)
            s = "%s" % root.data
            u = len(s)
            first_line = s + x * "_" + (n - x) * " "
            second_line = (u + x) * " " + "\\" + (n - x - 1) * " "
            shifted_lines = [u * " " + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2
        # Two children.
        left, n, p, x = self.print(root.left)
        right, m, q, y = self.print(root.right)
        s = "%s" % root.data
        u = len(s)
        first_line = (x + 1) * " " + (n - x - 1) * "_" + s + y * "_" + (m - y) * " "
        second_line = x * " " + "/" + (n - x - 1 + u + y) * " " + "\\" + (m - y - 1) * " "
        if p < q:
            left += [n * " "] * (q - p)
        elif q < p:
            right += [m * " "] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * " " + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2

    def is_empty(self, root):
        if root == None:
            return True
        else:
            return False
            
    def add(self, data):
        if not data.isdigit():
            raise TypeError("Only numbers can be added to the tree")
        data = int(data)
        if self.is_empty(self.root):
            self.root = Node(data)
        else:
            self.add_root(self.root, data)
    
    def add_root(self, root, data):
        if root.data == data:
            raise ValueError("Such an element has already been added to the tree")
        elif data < root.data:
            if self.is_empty(root.left):
                root.left = Node(data)
            else:
                self.add_root(root.left, data)
        else:
            if self.is_empty(root.right):
                root.right = Node(data)
            else:
                self.add_root(root.right, data)

    def preorder_traversal(self):
        if self.is_empty(self.root):
            raise TypeError("Empty tree")
        result = []
        self.preorder_traversal_root(self.root, result)
        return result

    def preorder_traversal_root(self, root, result):
        if not self.is_empty(root):
            result.append(root.data)
            self.preorder_traversal_root(root.left, result)
            self.preorder_traversal_root(root.right, result)
            return result
        
    def inorder_traversal(self):
        if self.is_empty(self.root):
            raise TypeError("Empty tree")
        result = []
        self.inorder_traversal_root(self.root, result)
        return result

    def inorder_traversal_root(self, root, result):
        if not self.is_empty(root):
            self.inorder_traversal_root(root.left, result)
            result.append(root.data)
            self.inorder_traversal_root(root.right, result)
            return result

    def postorder_traversal(self):
        if self.is_empty(self.root):
            raise TypeError("Empty tree")
        result = []
        self.postorder_traversal_root(self.root, result)
        return result

    def postorder_traversal_root(self, root, result):
        if not self.is_empty(root):
            self.postorder_traversal_root(root.left, result)
            self.postorder_traversal_root(root.right, result)
            result.append(root.data)
            return result

    def find_item(self, data): #поиск элемента по значению
        if self.is_empty(self.root):
            raise TypeError("Empty tree")
        if not data.isdigit():
            raise ValueError("Only integers can be searched in the tree")
        data = int(data)
        path = "root"
        if self.root.data == data:
            return path
        path = self.find_item_root(self.root, data, path)
        return path

    def find_item_root(self, root, data, path):
        if self.is_empty(root):
            raise Exception("ErRoR 404")
        if root.data == data:
            return path
        if data < root.data:
            path = self.find_item_root(root.left, data, path + "->left")
        else:
            path = self.find_item_root(root.right, data, path + "->right")
        return path

    def remove(self, data):
        if not data.isdigit():
            raise ValueError("Only numbers can be removed from the tree")
        data = int(data)
        if self.is_empty(self.root):
            raise TypeError("Empty tree")
        return self.remove_root(self.root, data)
    
    def remove_root(self, root, data):
        if self.is_empty(root):
            return root
        if data < root.data:
            root.left = self.remove_root(root.left, data)
        elif data > root.data:
            root.right = self.remove_root(root.right, data)
        else:
            if self.is_empty(root.right):
                return root.left
            elif self.is_empty(root.left):
                return root.right
            else:
                temp = root.right
                while not self.is_empty(temp.left):
                    temp = temp.left
                root.data = temp.data
                root.right = self.remove_root(root.right, temp.data)
        return root
    
    def depth(self, root, level):
        if self.is_empty(root):
            return level
        return max(self.depth(root.right, level + 1), self.depth(root.left, level + 1))
    
    #additions
    def clear(self):
        if self.is_empty(self.root):
            raise TypeError("Empty tree")
        self.clear_root(self.root)
        self.root = None

    def clear_root(self, root):
        if not self.is_empty(root):
            self.clear_root(root.left)
            self.clear_root(root.right)
            root.left = None
            root.right = None

    #individuals
    def product_of_elements_even_levels(self):
        if self.is_empty(self.root):
            raise TypeError("Empty tree")
        result = 1
        result *= self.product_of_elements_even_levels_root(self.root, result, True)
        return result

    def product_of_elements_even_levels_root(self, root, result, flag):
        if not self.is_empty(root):
            if flag:
                result *= root.data
                result *= self.product_of_elements_even_levels_root(root.right, 1, not flag)
                result *= self.product_of_elements_even_levels_root(root.left, 1, not flag)
            else:
                result *= self.product_of_elements_even_levels_root(root.right, 1, not flag)
                result *= self.product_of_elements_even_levels_root(root.left, 1, not flag)
        return result

# Взаимодействие с пользователем
x = input("Добро пожаловать!\nЕсли вы хотите вывести набор команд: введите Menu\nЕсли вы хотите посмотреть дерево: введите Show\nЕсли вы хотите проверить пустое ли дерево: введите Is Empty\nЕсли вы хотите добавить элементы в дерево: введите Add\nЕсли вы хотите обойти дерево: введите Traversal\nЕсли вы хотите узнать распоожение элемента в дереве: введите Find Item\nЕсли вы хотите удалить элементы из дерева: введите Remove\nЕсли вы хотите узнать глубину дерева: введите Depth\nЕсли вы хотите очистить дерево: введите Clear\nЕсли вы хотите найти произведение элементов всех четных уровней: введите Product Even Levels\nЕсли вы хотите закончить: введите Stop\n")
mytree = BinarySearchTree()
while True:
    x = x.lower()
    match x:
        case "menu":
            print("Если вы хотите вывести набор команд: введите Menu\nЕсли вы хотите посмотреть дерево: введите Show\nЕсли вы хотите проверить пустое ли дерево: введите Is Empty\nЕсли вы хотите добавить элементы в дерево: введите Add\nЕсли вы хотите обойти дерево: введите Traversal\nЕсли вы хотите узнать распоожение элемента в дереве: введите Find Item\nЕсли вы хотите удалить элементы из дерева: введите Remove\nЕсли вы хотите узнать глубину дерева: введите Depth\nЕсли вы хотите очистить дерево: введите Clear\nЕсли вы хотите найти произведение элементов всех четных уровней: введите Product Even Levels\nЕсли вы хотите закончить: введите Stop\n")
        case "show":
            print(mytree)
        case "is empty":
            if mytree.is_empty(mytree.root):
                print("Дерево пустое")
            else:
                print("Дерево не пустое")
        case "add":
            message = input("Если вы хотите линейно заполнить дерево: введите Fill, если же добавить один элемент: введите Add\n")
            if not message.isalpha():
                print("YOU LOSER")
                print("Надо было ввести команду :З")
            else:
                if message == "fill":
                    length = input("Введите количество элементов которое хотите добавить: ")
                    if not length.isdigit():
                        print("YOU LOSER")
                        print("Надо было ввести число :З")
                    else:
                        print("Если вдруг вы устанете заполнять дерево и захотите прервать процесс: введите ~I'm LoSeR~")
                        count_elements = 0
                        for i in range(0, int(length)):
                            item = input("Введите элемент: ")
                            if item == "~I'm LoSeR~":
                                print("Элементы успешно добавились, процесс прерван")
                                break
                            else:
                                try:
                                    mytree.add(item)
                                except ValueError:
                                    print("Такой элемент уже есть в дереве")
                                except TypeError:
                                    print("В дерево можно добавлять только числа")
                                count_elements += 1
                        if count_elements == length:
                            print("Дерево успешно заполнено")
                elif message == "add":
                    item = input("Введите элемент: ")
                    flag = True
                    try:
                        mytree.add(item)
                    except ValueError:
                        flag = False
                        print("Такой элемент уже есть в дереве")
                    except TypeError:
                        flag = False
                        print("В дерево можно добавлять только числа")
                    if flag:
                        print("Вы добавили элемент", item)
                else:
                    print("YOU LOSER")
                    print("Вы ввели неправильную команду :З")
        case "traversal":
            message = input("Если вы хотите посмотреть прямой обход дерева: введите Preorder, если симметричный: введите Inorder, если обратный: введите Postorder")
            message = message.lower()
            match message:
                case "preorder":
                    try:
                        print("Прямой обход:", mytree.preorder_traversal())
                    except TypeError:
                        print(mytree)
                case "inorder":
                    try:
                        print("Симметричный обход:", mytree.inorder_traversal())
                    except TypeError:
                        print(mytree)
                case "postorder":
                    try:
                        print("Обратный обход:", mytree.postorder_traversal())
                    except TypeError:
                        print(mytree)
                case _:
                    print("YOU LOSER")
                    print("Вы ввели неправильную команду :З")
        case "remove":
            message = input("Если вы хотите удалить несколько элементов: введите Remove, если один: введите Pop")
            if not message.isalpha():
                print("YOU LOSER")
                print("Надо было ввести команду :З")
            else:
                message = message.lower()
                if message == "remove":
                    length = input("Введите количество элементов для удаления: ")
                    if not length.isdigit():
                        print("YOU LOSER")
                        print("В следующий раз стоит вводить корректное количество элементов для удаления :З")
                    else:
                        print("Если вдруг вы устанете удалять элементы и захотите прервать процесс: введите ~I'm LoSeR~")
                        for i in range(0, int(length)):
                            item = input("Введите элемент, который хотите удалить: ")
                            if item == "~I'm LoSeR~":
                                print("Элементы успешно удалены, процесс прерван")
                                break
                            else:
                                try:
                                    mytree.remove(item)
                                    print("Вы удалили элемент", item)
                                except TypeError:
                                    print("YOU LOSER")
                                    print("А что вы собрались удалять в пустом дереве (｡· v ·｡)?")
                                except ValueError:
                                    print("В дереве присутствуют только целочисленные элементы")
                elif message == "pop":
                    item = input("Введите элемент, который хотите удалить: ")
                    try:
                        mytree.remove(item)
                        print("Вы удалили элемент", item)
                    except TypeError:
                        print("YOU LOSER")
                        print("А что вы собрались удалять в пустом дереве (｡· v ·｡)?")
                    except ValueError:
                        print("В дереве присутствуют только целочисленные элементы")
                else:
                        print("YOU LOSER")
                        print("Вы ввели неправильную команду :З")
        case "find item":
            value = input("Введите элемент: ")
            try:
                result = mytree.find_item(value)
                print("Элемент", value, "находится в списке по пути:", result)
            except TypeError:
                print("Что вы собрались искать в пустом дереве (｡· v ·｡)?")
            except ValueError:
                print("В дереве можно искать только целые числа")
            except Exception:
                print("YOU LOSER")
                print("Такого элемента в дереве не нашлось :З")
        case "depth":
            print("Глубина дерева:", mytree.depth(mytree.root, 0))
        case "product even levels":
            try:
                print("Произведение элементов всех четных уровней:", mytree.product_of_elements_even_levels())
            except TypeError:
                print("А что вы собрались умножать в пустом дереве (｡· v ·｡)?")
        case "clear":
            try:
                mytree.clear()
                print("Вы очистили дерево, его элементы больше не доступны :(")
            except TypeError:
                print("YOU LOSER")
                print("Не стоит пытаться очистить пустое дерево :З")
        case "stop":
            break
        case _:
            print("Научись вводить команды правильно :З")
    x = input("Введите еще команду: ")

```

```python
for x in range(0,2):
    for y in range(0,2):
        for z in range(0,2):
            for w in range(0,2):
                for e in range(0,2):
                    f1 = (not(not(y) or ((y and not(z)) and (y or not(e)))) or ((x and w) or (not(w) and x)))
                    f2 = (((not(x) or not(y) or not(z)) and (x or (y and z))) and (not(w) or ((e and w) or (w and not(e)))))
                    if f1 != f2:
                        print(x, y, z, w, e)
```

```python

```
