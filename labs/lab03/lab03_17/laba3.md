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
<h3> Лабораторная работа №3 <br> <br>
    «Линейные двунаправленные списки (Doubly Linked Lists)» </h3>
<br>
<h4> Цель работы: </h4>
Изучение структуры данных «линейные двунаправленные списки», а также основных операций над ними.
<br>
<br>
<h4> Постановка задачи: </h4>

1. Написать собственную реализацию двунаправленного списка в виде класса. Приэтом каждая его операция должна быть реализована как метод класса и добавлению/удалению элемента должна предшествовать проверка возможности выполнения этих операций.
2. Реализовать программу, выполняющую стандартный набор операций с линейным двунаправленным списком:
    * просмотр линейного двунаправленного списка;
    * вставка элемента в начало списка;
    * вставка элемента в середину списка перед указанным значением;
    * вставка элемента в середину списка после указанного значения;
    * вставка элемента в конец списка;
    * удаление элемента в начале списка;
    * удаление элемента, стоящего перед указанным значением списка;
    * удаление элемента, стоящего после указанного значением списка;
    * удаление определенного элемента в списке;
    * удаление элемента в конце списка;
    * очистка списка;
    * поиск элемента списка по его значяению;
    * реверс списка (переворачивание списка задом на перед).
3. Реализовать приложение, для работы со списком, которое реализует следующий набор действий:
    * инициализация пустого линейного однонаправленного списка;
    * организация диалогового цикла с пользователем;
<br>
<br>
<h4> Code Listing: </h4>

```python
class Node: 
    def __init__(self, data, next = None)

class Singly_Linked_List:
    def __init__(self)

    def __str__(self) #вывод списка

    def push_front(self, data) #вставка элемента в начало списка

    def push_back(self, data) #вставка элемента в конец списка

    def insert(self, index, data) #вставка элемента по индексу

    def insert_before(self, item, data) #вставка элемента перед первым вхождением указанного элемента

    def insert_after(self, item, data) #вставка элемента после первого вхождения указанного элемента

    def find_item(self, data) #поиск элемента по значению
    
    def find_index(self, index) #поиск элемента по индексу
    
    def pop_front(self) #удаление элемента из начала списка
    
    def pop_back(self) #удаление элемента из конца списка
    
    def pop(self, index) #удаление элемента по индексу

    def pop_before(self, item) #удаление элемента перед первым вхождением указанного элемента
    
    def pop_after(self, item) #удаление элемента после первого вхождения указанного элемента

    def remove(self, index, length): #удаление нескольких элементов по индексу и количеству
    
    def reverse(self) #поворот списка задом наперед
    
    def clear(self) #очистка списка
    
    #addition
    def count(self, item) #подсчет количества элементов с заданным значением

    def sort(self) #сортировка списка

    #individuals
    def is_digit(self) #провека списка на численные элементы

    def only_odd_numbers(self) #Индивидуальное задание 1-17: удаление из списка всех четных чисел

    def more_than_sum(self) #Индивидуальное задание 2-17: подсчет количества элементов, превосходящих сумму всех элементов списка

#Взаимодействие с пользователем
x = input("...")
while (x):
    ///код
    match x:
        case "menu":
            ///код
        
        case "show":
            ///код
        
        case "add":
            ///код
        
        case "remove":
            ///код
            
        case "find value":
            ///код

        case "find index":
            ///код
        
        case "reverse":
            ///код
        
        case "clear":
            ///код

        case "count":
            ///код

        case "sort":
            ///код
            
        case "is digit":
            ///код

        case "only odd numbers":
            ///код

        case "more than sum":
            ///код
            
        case "stop":
            ///код
    ///код
```
<br>
<h4> Выводы </h4>
В ходе лабораторной работы была изучена структура данных «линейные двунаправленные 
списки», написана собственнаяя реализация двунаправленного списка в виде класса 
таким образом, что каждая его операция является методом класса. Реализована 
программа, выполняющая стандартный набор операций с линейным двунаправленным 
списком и приложение, которое осуществляет диалоговый цикл с пользователем.
<br>
<br>
<h4> Ответы на контрольные вопросы </h4>

1. *Что такое динамическая структура данных?* <br>
Динамические структуры данных – это структуры данных, память под которые выделяется и освобождается по мере необходимости в процессе выполнения программы, а не в момент ее запуска. Динамические структуры данных в процессе существования в памяти могут изменять не только число составляющих их элементов, но и характер связей между элементами. <br>
2. *Что такое список?* <br>
Список — это упорядоченный набор элементов, каждый из которых имеет свой номер, или индекс, позволяющий быстро получить к нему доступ.<br>
3. *Какие виды списков существуют?*<br>
    * Односвязный линейный список: каждый узел содержит 1 поле указателя на следующий узел; поле указателя последнего узла содержит нулевое значение (указывает на NULL)<br>
    * Односвязный циклический список: каждый узел ОЦС содержит 1 поле указателя на следующий узел; поле указателя последнего узла содержит адрес первого узла (корня списка)<br>
    * Двусвязный линейный список: каждый узел ДЛС содержит два поля указателей: на следующий и на предыдущий узел; поле указателя на следующий узел последнего узла содержит нулевое значение (указывает на NULL); поле указателя на предыдущий узел первого узла (корня списка) также содержит нулевое значение (указывает на NULL)<br>
    * Двусвязный циклический список: каждый узел ДЦС содержит два поля указателей: на следующий и на предыдущий узел; поле указателя на следующий узел последнего узла содержит адрес первого узла (корня списка); поле указателя на предыдущий узел первого узла (корня списка) содержит адрес последнего узла<br>
4. *Какие основные операции выполняются над списком?*<br>
    * Добавление элементов в список<br>
    * Вставка элемента в список<br>
    * Удаление элемента из списка<br>
    * Поиск элемента в списке<br>
    * Реверс списка (переворачивание списка задом на перед)<br>
    * Подсчет количества элементов с заданным значением<br>
    * Сортировка списка на основе функции<br>
    * Очистка списка<br>
5. *Особенности выполнения операции вставки первого и не первого элемента в двунаправленный список.* <br>
В линейном двунаправленном списке при вставке первого элемента надо менять указатель head, а при вставке последующих элементов нужно изменять указатели предыдущего элемента.<br>
6. *Особенности выполнения операций удаления первого и не первого элемента.* <br>
При удалении первого элемента в линейном двунаправленном списке, также как и при вставке нужно изменять указатель head, а при удалении последующих надо менять указатели предыдущих.
<!-- #endregion -->

```python
class Node:
    def __init__(self, data, next = None, prev = None):
        self.data = data
        self.next = next
        self.prev = prev

class Doubly_Linked_List:
    def __init__(self):
        self.size = 0
        self.head = None
        self.tail = None

    def __str__(self):
        if self.head == None:
            text = "list is empty: " + str(self.size) + " " + str(self.head)
        else:
            text = "list size = " + str(self.size) + "\nhead is = " + str(self.head.data) + "\nlist: "
            temp = self.head
            while temp:
                text += str(temp.data) + " "
                temp = temp.next
        return text

    def push_back(self, data):
        item = Node(data)
        if self.head == None:
            self.head = item
            self.tail = item
            item.prev = None
            item.next = None
        else:
            temp = self.tail
            temp.next = item
            item.next = None
            item.prev = temp
            self.tail = item
        self.size += 1
    
    def push_front(self, data):
        item = Node(data)
        if self.head == None:
            self.head = item
            self.tail = item
            item.prev = None
            item.next = None
        else:
            temp = self.head
            temp.prev = item
            item.prev = None
            item.next = temp
            self.head = item
        self.size += 1

    def insert(self, index, data):
        if not(index.isdigit()):
            return "ErRoR"
        index = int(index)
        if index < 0:
            index += self.size
        if index < 0 or index > self.size:
            return "ErRoR"
        elif self.head == None or index == self.size:
            self.push_back(data)
        elif index == 0:
            self.push_front(data)
        else:
            item = Node(data)
            temp = self.head
            count = 0
            while (count < index - 1):
                temp = temp.next
                count += 1
            curr = temp.next
            temp.next = item
            item.prev = temp
            item.next = curr
            curr.prev = item
            self.size += 1

    def insert_before(self, item, data):
        if self.head == None:
            return "loser"
        index = self.find_item(item)
        if index == "ErRoR":
            return "ErRoR"
        self.insert(str(index), data)
        return "Ok"

    def insert_after(self, item, data):
        if self.head == None:
            return "loser"
        index = self.find_item(item)
        if index == "ErRoR":
            return "ErRoR"
        self.insert(str(index + 1), data)
        return "Ok"

    def find_item(self, data): #поиск элемента по значению
        temp = self.head
        index = 0
        while (temp != None and temp.data != data):
            index += 1
            temp = temp.next
        if temp == None:
            return "ErRoR"
        else:
            return index

    def find_index(self, index): #поиск элемента по индексу
        if not(index.isdigit()):
            return "ErRoR"
        index = int(index)
        if index < 0:
            index += self.size
        if index > self.size - 1 or index < 0:
            return "ErRoR"
        temp = self.head
        count = 0
        while (count < index):
            temp = temp.next
            count += 1
        return temp.data

    def pop_front(self):
        if self.head == None:
            return "ErRoR"
        else:
            item = self.head
            self.head = item.next
            self.head.prev = None
            self.size -= 1
            return item.data

    def pop_back(self):
        if self.head == None:
            return "ErRoR"
        else:
            item = self.tail
            self.tail = item.prev
            self.tail.next = None
            self.size -= 1
            return item.data

    def pop(self, index):
        if not(index.isdigit()):
            return "ErRoR"
        index = int(index)
        if index < 0:
            index += self.size
        if index < 0 or index > self.size - 1:
            return "ErRoR"
        elif self.head == None or index == self.size - 1:
            return self.pop_back()
        elif index == 0:
            return self.pop_front()
        else:
            temp = self.head
            count = 0
            while (count < index - 1):
                temp = temp.next
                count += 1
            item = temp.next
            temp.next = item.next
            item.next.prev = temp
            self.size -= 1
            return item.data

    def pop_before(self, item):
        if self.head == None:
            return "loser"
        index = self.find_item(item)
        if index == "ErRoR":
            return "ErRoR"
        elif index == 0:
            return "first"
        return self.pop(str(index - 1))

    def pop_after(self, item):
        if self.head == None:
            return "loser"
        index = self.find_item(item)
        if index == "ErRoR":
            return "ErRoR"
        elif index == self.size - 1:
            return "last"
        return self.pop(str(index + 1))

    def remove(self, index, length):
        if (not index.isdigit()) or (not length.isdigit()):
            return "ErRoR"
        index = int(index)
        length = int(length)
        if index + length < 0 or index + length - 1 > self.size - 1:
            return "ErRoR"
        elif self.head == None:
            return "empty"
        else:
            index = str(index)
            for i in range(0, length):
                temp = self.pop(index)

    def reverse(self):
        if self.head == None:
            return "ErRoR"
        previous = self.head
        current = previous.next
        head = self.head
        tail = self.tail
        while (current != None):
            next = current.next
            current.next = previous
            previous.prev = current
            previous = current
            current = next
        self.head = tail
        self.head.prev = None
        self.tail = head
        self.tail.next = None

    def clear(self):
        if self.head == None:
            return "list is already empty"
        temp = self.head
        while temp != None:
            temp.data = None
            temp = temp.next
        self.size = 0
        self.head = None

    def no_dublicates(self):
        set_of_dublicates = set()
        temp = self.head
        while temp != None:
            if self.count(temp.data) > 1:
                set_of_dublicates.add(temp.data)
            temp = temp.next
        for j in set_of_dublicates:
            count = self.count(j)
            for i in range(1, count):
                deleted = self.pop(str(self.find_item(j)))
        return self

    # Мне было скучно
    def count(self, item): #Подсчет количества элементов с заданным значением
        if self.head == None:
            return "ErRoR"
        else:
            count = 0
            temp = self.head
            while temp != None:
                if temp.data == item:
                    count += 1
                temp = temp.next
            if count == 0:
                return "ErRoR 404"
            else:
                return count

    def sort(self): #Сортировка списка
        if self.head == None:
            return "NoNo"
        else:
            sorted = []
            temp = self.head
            while temp != None:
                sorted += [temp.data]
                temp = temp.next
            sorted.sort()
            self.clear()
            for i in sorted:
                self.push_back(i)
        return self

    def is_digit(self):
        if self.head == None:
            return "empty"
        temp = self.head
        count_not_digits = 0
        while temp != None:
            if not ((temp.data[1::].isdigit() and temp.data[0] == '-') or temp.data.isdigit()):
                count_not_digits += 1
            temp = temp.next
        if count_not_digits > 0:
            return False
        else:
            return True

    #Индивидуальное задание 1-17
    def only_odd_numbers(self):
        if self.is_digit():
            temp = self.head
            while temp != None:
                if int(temp.data) % 2 == 0:
                    index = self.find_item(temp.data)
                    deleted = self.pop(str(index))
                temp = temp.next
            return self
        else:
            return "ErRoR"
    

    #Индивидуальное задание 2-17
    def more_than_sum(self):
        if self.is_digit():
            count = 0
            sum = 0
            temp = self.head
            while temp != None:
                sum += int(temp.data)
                temp = temp.next
            temp = self.head
            while temp != None:
                if int(temp.data) > sum:
                    count += 1
                temp = temp.next
            if count > 0:
                return count
            else:
                return "NoNo"
        else:
            return "ErRoR"
    

# Взаимодействие с пользователем
x = input("Добро пожаловать!\nЕсли вы хотите вывести набор команд: введите Menu\nЕсли вы хотите посмотреть список: введите Show\nЕсли вы хотите добавить элементы в список: введите Add\nЕсли вы хотите удалить элементы из списка: введите Remove\nЕсли вы хотите найти элемент в списке: введите Find Value\nЕсли вы хотите вывести определенный элемент из списка: введите Find Index\nЕсли вы хотите развернуть список: введите Reverse\nЕсли вы хотите очистить список: введите Clear\nЕсли вы хотите узнать количество вхождений некоторого элемента: введите Count\nЕсли вы хотите отсортировать список: введите Sort\nЕсли вы хотите проверить состоит ли список только из численных элементов: введите Is Digit\nЕсли вы хотите удалить из списка все четные элеметы (только для списков с численными элементами): введите Only Odd Numbers\nЕсли вы хотите посчитать количество элементов в списке, которые больше его суммы (только для списков с численными элементами): введите More Than Sum\nЕсли вы хотите закончить: введите Stop\n")
mylist = Doubly_Linked_List()
while (True):
    x = x.lower()
    match x:
        case "menu":
            print("Если вы хотите вывести набор команд: введите Menu\nЕсли вы хотите посмотреть список: введите Show\nЕсли вы хотите добавить элементы в список: введите Add\nЕсли вы хотите удалить элементы из списка: введите Remove\nЕсли вы хотите найти элемент в списке: введите Find Value\nЕсли вы хотите вывести определенный элемент из списка: введите Find Index\nЕсли вы хотите развернуть список: введите Reverse\nЕсли вы хотите очистить список: введите Clear\nЕсли вы хотите узнать количество вхождений некоторого элемента: введите Count\nЕсли вы хотите отсортировать список: введите Sort\nnЕсли вы хотите проверить состоит ли список только из численных элементов: введите Is Digit\nЕсли вы хотите удалить из списка все четные элеметы (только для списков с численными элементами): введите Only Odd Numbers\nЕсли вы хотите посчитать количество элементов в списке, которые больше его суммы (только для списков с численными элементами): введите More Than Sum\nЕсли вы хотите закончить: введите Stop")
        case "show":
            print(mylist)
        case "add":
            message = input("Если вы хотите линейно заполнить список: введите Fill, если добавить один элемент по индексу: введите Add, если добавить элемент перед каким-то другим: введите Before, если после - After\n")
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
                        print("Если вдруг вы устанете заполнять список и захотите прервать процесс: введите ~I'm LoSeR~")
                        count_elements = 0
                        length = int(length)
                        flag = True
                        for i in range(0, length):
                            if not flag:
                                break
                            item = input("Введите элемент: ")
                            if item == "~I'm LoSeR~":
                                while True:
                                    exit = input("Если вы хотите закончить заполнение списка: введите Break, если добавить элемент ~I'm LoSeR~: введите Add\n")
                                    if not exit.isalpha():
                                        print("YOU LOSER")
                                        print("Надо было ввести команду :З")
                                        print("Попробуйте еще раз")
                                    else:
                                        exit = exit.lower() 
                                        if exit == "break":
                                            print("Элементы успешно добавились, процесс прерван")
                                            flag = False
                                            break
                                        elif exit == "add":
                                            result = mylist.push_back(item)
                                            count_elements += 1
                                            break
                                        else:
                                            print("YOU LOSER")
                                            print("Надо было ввести команду :З")
                                            print("Попробуйте еще раз")
                            else:
                                mylist.push_back(item)
                                count_elements += 1
                        if count_elements == length:
                            print("Список успешно заполнен")
                elif message == "add":
                    index = input("Введите индекс: ")
                    item = input("Введите элемент: ")
                    if mylist.insert(index, item) == "ErRoR":
                        print("YOU LOSER")
                        print("Не вводите некорректный индекс :З")
                    else:
                        print("Вы добавили элемент", item, "по индексу", index)
                elif message == "before":
                    item = input("Введите элемент, перед которым хотите вставить данные: ")
                    data = input("Введите данные, которые хотите вставить: ")
                    result = mylist.insert_before(item, data)
                    if result == "ErRoR":
                        print("YOU LOSER")
                        print("Такого элемента не существует :З")
                    elif result == "loser":
                        print("YOU LOSER")
                        print("Перед каким элементом в пустом списке вы собрались что-то вставлять (｡· v ·｡)?")
                    else:
                        print("Вы добавили элемент", data, "перед элементом", item)
                elif message == "after":
                    item = input("Введите элемент, после которого хотите вставить данные: ")
                    data = input("Введите данные, которые хотите вставить: ")
                    result = mylist.insert_after(item, data)
                    if result == "ErRoR":
                        print("YOU LOSER")
                        print("Такого элемента не существует :З")
                    elif result == "loser":
                        print("YOU LOSER")
                        print("После какого элемента в пустом списке вы собрались что-то вставлять (｡· v ·｡)?")
                    else:
                        print("Вы добавили элемент", data, "после элемента", item)
                else:
                    print("YOU LOSER")
                    print("Вы ввели неправильную команду :З")
        case "remove":
            message = input("Если вы хотите удалить несколько элементов: введите Remove, если один: введите Pop, если удалить элемент перед каким-то другим: введите Before, если после - After")
            if not message.isalpha():
                print("YOU LOSER")
                print("Надо было ввести команду :З")
            else:
                message = message.lower()
                if message == "remove":
                    index = input("Введите индекс, с которого начинать удаление элементов: ")
                    length = input("Введите количество элементов для удаления: ")
                    result = mylist.remove(index, length)
                    if result == "ErRoR":
                        print("YOU LOSER")
                        print("В следующий раз стоит вводить корректный индекс и длину :З")
                    elif result == "empty":
                        print("А что вы собрались удалять в пустом списке (｡· v ·｡)?")
                    else:
                        print("Вы удалили", length, "элементов, начиная с индекса", index)
                elif message == "pop":
                    index = input("Введите индекс: ")
                    result = mylist.pop(index)
                    if result == "ErRoR":
                        print("YOU LOSER")
                        print("Не вводите некорректный индекс :З")
                    else:
                        print("Вы удалили элемент", result)
                elif message == "before":
                    item = input("Введите элемент, перед которым хотите удалить данные: ")
                    result = mylist.pop_before(item)
                    if result == "ErRoR":
                        print("YOU LOSER")
                        print("Такого элемента не существует :З")
                    elif result == "first":
                        print("YOU LOSER")
                        print("Перед первым элементом ничегошеньки нет :З")
                    elif result == "loser":
                        print("YOU LOSER")
                        print("Перед каким элементом в пустом списке вы собрались что-то удалять (｡· v ·｡)?")
                    else:
                        print("Вы удалили элемент", result)
                elif message == "after":
                    item = input("Введите элемент, после которого хотите удалить данные: ")
                    result = mylist.pop_after(item)
                    if result == "ErRoR":
                        print("YOU LOSER")
                        print("Такого элемента не существует :З")
                    elif result == "last":
                        print("YOU LOSER")
                        print("После последнего элемента ничегошеньки нет :З")
                    elif result == "loser":
                        print("YOU LOSER")
                        print("После какого элемента в пустом списке вы собрались что-то удалять (｡· v ·｡)?")
                    else:
                        print("Вы удалили элемент", result)
                else:
                        print("YOU LOSER")
                        print("Вы ввели неправильную команду :З")
        case "find value":
            value = input("Введите элемент: ")
            result = mylist.find_item(value)
            if result == "ErRoR":
                print("YOU LOSER")
                print("Не ищите элемент, которого нет в списке :З")
            else:
                print("Элемент", value, "находится в списке под индексом", result)
        case "find index":
            index = input("Введите индекс: ")
            result = mylist.find_index(index)
            if result == "ErRoR":
                print("YOU LOSER")
                print("Не вводите некорректный индекс :З")
            else:
                print("Под индексом", index, "в списке находится элемент", result)
        case "reverse":
            if mylist.reverse() == "ErRoR":
                print("YOU LOSER")
                print("Не пытайтесь развернуть пустой список :З")
            else:
                print("Вы развернули список")
        case "clear":
            if mylist.clear() == "list is already empty":
                print("YOU LOSER")
                print("Не стоит пытаться очистить пустой список :З")
            else:
                print("Вы очистили список, его элементы больше не доступны :(")
        case "count":
            item = input("Введите элемент, количество вхождений которого хотите узнать: ")
            result = mylist.count(item)
            if result == "ErRoR":
                print("Что вы собрались искать в пустом списке (｡· v ·｡)?")
            elif result == "ErRoR 404":
                print("ErRoR 404")
            else:
                print("Элемент", item, "встретился в списке", result, "раз")
        case "sort":
            result = mylist.sort()
            if result == "NoNo":
                print("YOU LOSER")
                print("Не надо пытаться отсортировать пустой список :З")
            else:
                print(result)
        case "is digit":
            result = mylist.is_digit()
            if result == "empty":
                print("В пустом списке нет ни чисел ни чего-либо еще :З")
            elif result:
                print("Список состоит только из чисел")
            else:
                print("В списке присутствуют не только численные элементы")
        case "only odd numbers":
            result = mylist.only_odd_numbers()
            if result == "ErRoR":
                print("YOU LOSER")
                print("Как оказалось, список состоял не только из численных элементов (｡· v ·｡)")
            else:
                print("Теперь в списке только нечетные элементы")
        case "more than sum":
            result = mylist.more_than_sum()
            if result == "ErRoR":
                print("YOU LOSER")
                print("Как оказалось, список состоял не только из численных элементов (｡· v ·｡)")
            elif result == "NoNo":
                print("В списке не оказалось элементов, которые больше суммы списка")
            else:
                print("В списке", result, "элементов, которые больше суммы списка")
        case "stop":
            break
        case "no dublicates":
            print(mylist.no_dublicates())
    x = input("Введите еще команду: ")
```

```python

```

```python

```
