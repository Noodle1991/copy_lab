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
<h3> Лабораторная работа №7 <br> <br>
    «Рандомизированные деревья (Random binary tree)» </h3>
<br>
<h4> Цель работы: </h4>
Изучение рандомизированных двоичных деревьев поиска, а также основных операций над ними.
<br>
<br>
<h4> Постановка задачи: </h4>

1. Написать собственную реализацию рандомизированного двоичного дерева поиска в виде класса. Приэтом каждая его операция должна быть реализована как метод класса и добавлению/удалению элемента должна предшествовать проверка возможности выполнения этих операций.
2. Реализовать программу, выполняющую стандартный набор операций над рандомизированным двоичным деревом поиска:
    * формирование бинарного дерева;
    * обход (прямой, симметричный, обратный) бинарного дерева;
    * удаление заданной вершины из бинарного дерева;
    * поиск заданной вершины в бинарном дереве (по значению);
    * печать бинарного дерева на экран;
    * проверка пустоты бинарного дерева;
    * определение высоты бинарного дерева.
3. Реализовать приложение, для работы с бинарным деревом поиска, которое реализует следующий набор действий:
    * инициализация пустого рандомизированного бинарного дерева;
    * организация диалогового цикла с пользователем;
<br>
<br>
<h4> Code Listing: </h4>

```python
class Node: 
    def __init__(self, data, left = None, right = None)

class RandomBinarySearchTree:
    
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
В ходе лабораторной работы была изучена структура данных «рандомизированное двоичноe деревo поиска», написана собственнаяя реализация рандомизированного двоичного дерева поиска в виде класса таким образом, что каждая его операция является методом класса. Реализована программа, выполняющая стандартный набор операций с рандомизированным двоичным деревом поиска и приложение, которое осуществляет диалоговый цикл с пользователем.
<br>
<br>
<h4> Ответы на контрольные вопросы </h4>

1. *Что такое рандомизованное дерево?* <br>
Рандомизованное дерево – это структура данных, которая является разновидностью двоичного дерева поиска. Главное отличие рандомизованного дерева от обычного двоичного дерева поиска заключается в его случайной природе. <br>
В рандомизованном дереве каждый узел имеет некоторый случайный приоритет. Узлы с более высоким приоритетом имеют больший приоритет при оптимизации структуры дерева. При вставке, удалении или поиске элемента в рандомизованном дереве ключевая операция - случайное перемещение по дереву, основанное на приоритетах узлов. 
2. *По какому правилу оно строится?* <br>
Рандомизированное дерево строится на основе двух основных правил:
    * Правило случайности приоритетов: Каждому узлу в дереве назначается случайный приоритет. Обычно приоритет генерируется случайным образом и может быть целым числом или другим типом данных, который можно сравнить. Приоритет служит для определения порядка расположения узлов в дереве.
    * Правило двоичного дерева поиска: Рандомизированное дерево сохраняет структуру двоичного дерева поиска, где каждый узел имеет ключ и два дочерних узла (левого и правого). Узел с меньшим ключом всегда располагается в левом поддереве, а узел с большим ключом – в правом поддереве. Это правило позволяет эффективно выполнять операции вставки, удаления и поиска элементов в дереве.
3. *Как определяется количество узлов в рандомизованном дереве?* <br>
Количество узлов в рандомизованном дереве зависит от количества элементов, которые были вставлены в дерево. Каждый узел в дереве представляет отдельный элемент, поэтому количество узлов соответствует количеству элементов в дереве. <br>
Количество узлов в рандомизованном дереве может быть определено путем подсчета узлов или элементов в дереве. Для этого можно использовать различные алгоритмы обхода дерева, такие как прямой обход (pre-order), центрированный обход (in-order) или обратный обход (post-order). Подсчет количества узлов можно выполнить рекурсивно, обрабатывая каждый узел и увеличивая счетчик узлов при обходе.
4. *Какие основные операции характерны при использовании деревьев?* <br>
    * Поиск элементов в дереве
    * Добавление элемента в дерево
    * Удаление элемента из дерева
    * Обход дерева
6. *Как происходит добавление элемента в рандомизованное дерево?* <br>
Процедура добавления будет рекурсивной: для пустого дерева она просто создаст новый узел, для непустого – рекурсивно добавит узел в корень левого или правого поддерева, а затем выполнит левое или правое вращение.
7. *Как происходит удаление элемента из рандомизованного дерева?* <br>
Удаление элемента в рандомизованном дереве должно сохранять сбалансированность. Если одно из поддеревьев содержит больше элементов, то разумно, чтобы элемент для замены удаляемого извлекался с большей вероятностью именно из этого дерева. <br>
Оно основано на операции объединения деревьев. После удаления элемента, мы должны объединить его левое и правое поддеревья. Объединение деревьев выполняется рекурсивно. Если одно из деревьев пусто, то результат объединения равен другому дереву. Если оба непусты, то мы в корень объединенного дерева помещаем либо корень левого дерева и присоединяем справа объединение его правого поддерева и второго поддерева, либо корень правого поддерева и аналогично другое дерево присоединяем слева. 
8. *Особенности красно-черных деревьев.* <br>
    * Красно-черное дерево является разновидностью бинарного дерева поиска. Каждый узел имеет ключ и два дочерних узла - левый и правый. Значения ключей левого поддерева меньше значения ключа родительского узла, а значения ключей правого поддерева больше значения ключа родительского узла.
    * Каждый путь от корня к листовому узлу должен содержать одинаковое количество черных узлов. Это свойство гарантирует, что красно-черное дерево сбалансировано и имеет высоту O(log n), где n - количество узлов в дереве.
    * Каждый узел в красно-черном дереве окрашен в красный или черный цвет. Корень всегда окрашен в черный цвет. Другие узлы могут быть окрашены в красный или черный цвет.
    * В красно-черном дереве существуют следующие правила окрашивания:
       - Красный узел имеет только черных дочерних узлов.
       - Если узел окрашен в красный цвет, то оба его дочерних узла должны быть окрашены в черный цвет.
       - Все пути от данного узла до его листьев должны содержать одинаковое количество черных узлов.
    * Вставка и удаление в красно-черном дереве производятся с учетом правил окрашивания, чтобы поддерживать сбалансированность и другие свойства красно-черных деревьев. При вставке или удалении может потребоваться перекрашивание узлов и вращение поддеревьев, чтобы сохранить баланс.
9. *Особенности АВЛ деревьев.* <br>
    * АВЛ-дерево основано на концепции сбалансированности, что означает, что разница высоты левого и правого поддерева каждого узла может быть не более 1. Это гарантирует, что АВЛ-дерево имеет сбалансированную структуру и операции вставки, удаления и поиска выполняются за время O(log n), где n - количество узлов.
    * АВЛ-дерево является разновидностью бинарного дерева поиска. Каждый узел имеет ключ и два дочерних узла - левый и правый. Значения ключей левого поддерева меньше значения ключа родительского узла, а значения ключей правого поддерева больше значения ключа родительского узла.
    * Высота любого поддерева в АВЛ-дереве может быть найдена как разность высоты его левого и правого поддерева. Разница высот должна быть не более 1 по свойству сбалансированности.
    * При вставке или удалении элементов в АВЛ-дерево проверяется сбалансированность каждого узла. Если разница высоты левого и правого поддерева превышает 1, производятся операции вращения, чтобы восстановить баланс.
    * Вращения в АВЛ-дереве могут быть одиночными или двойными. Одиночные вращения используются для поворотов влево или вправо вокруг узла, двойные вращения - для совмещенных операций поворота. Вращения обеспечивают перебалансировку дерева и поддержание свойства сбалансированности.
<!-- #endregion -->

```python
class Node:
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

class RandomBinarySearchTree:
    def __init__(self):
        self.root = None

    def __str__(self):
        if self.is_empty(self.root):
            return "random binary search tree is empty: " + str(self.root)
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
                if self.depth(self.root.right, 0) - self.depth(self.root.left, 0) > 1:
                    self.root = self.left_balance(self.root)
                elif self.depth(self.root.right, 0) - self.depth(self.root.left, 0) < -1:
                    self.root = self.right_balance(self.root)
            else:
                self.add_root(root.left, data)
        else:
            if self.is_empty(root.right):
                root.right = Node(data)
                if self.depth(self.root.right, 0) - self.depth(self.root.left, 0) > 1:
                    self.root = self.left_balance(self.root)
                elif self.depth(self.root.right, 0) - self.depth(self.root.left, 0) < -1:
                    self.root = self.right_balance(self.root)
            else:
                self.add_root(root.right, data)

    def right_balance(self, parent):
        root = parent.left
        parent.left = root.right
        root.right = parent
        return root

    def left_balance(self, parent):
        root = parent.right
        parent.right = root.left
        root.left = parent
        return root
    
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
        self.root = self.remove_root(self.root, data)
        if self.depth(self.root.right, 0) - self.depth(self.root.left, 0) > 1:
            self.root = self.left_balance(self.root)
        elif self.depth(self.root.right, 0) - self.depth(self.root.left, 0) < -1:
            self.root = self.right_balance(self.root)
        return self.root
    
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
mytree = RandomBinarySearchTree()
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

```
