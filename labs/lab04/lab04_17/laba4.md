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
<h1>ОТЧЕТ </h1>
<h3> Лабораторная работа №4 <br> <br>
    «Циклические однонаправленные списки (Circular Linked List)» </h3>
<br>
<h4> Цель работы: </h4>
Изучение структуры данных «Циклические однонаправленные списки», а также основных операций над ними.
<br>
<br>
<h4> Постановка задачи: </h4>

1. Написать собственную реализацию циклического однонаправленного списка в виде класса. Приэтом каждая его операция должна быть реализована как метод класса и добавлению/удалению элемента должна предшествовать проверка возможности выполнения этих операций.
2. Реализовать программу, выполняющую стандартный набор операций с циклическим однонаправленным списком:
    * вставка элемента в циклический однонаправленный список (в начало, середину, конец);
    * просмотр циклического однонаправленного списка;
    * поиск элемента в циклическом однонаправленном списке;
    * удаление элемента из циклического однонаправленного списка (из начала, середины, конца);
    * реверс списка (переворачивание списка задом на перед).
3. Реализовать приложение, для работы со списком, которое реализует следующий набор действий:
    * инициализация пустого циклического однонаправленного списка;
    * организация диалогового цикла с пользователем;
<br>
<br>
<h4> Code Listing: </h4>

```python
class Node: 
    def __init__(self, data, next = None)

class Circular_Linked_List:
    def __init__(self)

    def __str__(self) #вывод списка

    def push_front(self, data) #вставка элемента в начало списка

    def push_back(self, data) #вставка элемента в конец списка

    def insert(self, index, data) #вставка элемента по индексу

    def find_item(self, data) #поиск элемента по значению
    
    def find_index(self, index) #поиск элемента по индексу
    
    def pop_front(self) #удаление элемента из начала списка
    
    def pop_back(self) #удаление элемента из конца списка
    
    def pop(self, index) #удаление элемента по индексу

    def remove(self, index, length): #удаление нескольких элементов по индексу и количеству
    
    def reverse(self) #поворот списка задом наперед
    
    def clear(self) #очистка списка
    
    #addition
    def count(self, item) #подсчет количества элементов с заданным значением

    def sort(self) #сортировка списка

    def find_neighbours(self, item): #поиск соседних элементов к данному

    #helpers
    def is_digit(self) #провека списка на численные элементы
    
    def find_maximum(self) #поиск максимального элемента в списке

    #individuals
    def inverse_numbers(self): #Индивидуальное задание 1-17: Имеется список целых чисел. Все нечетные числа в нем умножить на 2, все четные разделить на 2.
        
    def delete_maximum(self):#Индивидуальное задание 2-17: Удалить из списка действительных чисел все максимальные элементы

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

        case "find neighbours":
            ///код

        case "is digit":
            ///код
            
        case "inverse numbers":
            ///код
            
        case "find maximum":
            ///код
            
        case "delete maximum":
            ///код
        
        case "stop":
            ///код
    ///код
```
<br>
<h4> Выводы </h4>
В ходе лабораторной работы была изучена структура данных «циклические однонаправленные списки», написана собственнаяя реализация однонаправленного списка в виде класса таким образом, что каждая его операция является методом класса. Реализована программа, выполняющая стандартный набор операций с циклическим однонаправленным списком и приложение, которое осуществляет диалоговый цикл с пользователем.
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
5. *Дать определение циклического списка.* <br>
Циклический (кольцевой) список – это структура данных, представляющая собой последовательность элементов, последний элемент которой содержит указатель на первый элемент списка, а первый (в случае двунаправленного списка) – на последний.<br>
6. *Классификация циклических списков.* <br>
    * Односвязный циклический список: каждый узел ОЦС содержит 1 поле указателя на следующий узел; поле указателя последнего узла содержит адрес первого узла (корня списка) <br>
    * Двусвязный циклический список: каждый узел ДЦС содержит два поля указателей: на следующий и на предыдущий узел; поле указателя на следующий узел последнего узла содержит адрес первого узла (корня списка); поле указателя на предыдущий узел первого узла (корня списка) содержит адрес последнего узла <br>
7. *Какие основные операции выполняются над циклическим списком?* <br>
<br>
<!-- #endregion -->

```python
class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

class Circular_Linked_List:
    def __init__(self):
        self.size = 0
        self.head = None

    def __str__(self):
        if self.head == None:
            text = "list is empty: " + str(self.size) + " " + str(self.head)
        else:
            text = "list size = " + str(self.size) + "\nhead is = " + str(self.head.data) + "\nlist: " + str(self.head.data) + " "
            temp = self.head.next
            while temp != self.head:
                text += str(temp.data) + " "
                temp = temp.next
        return text

    def print_next(self):
        temp = self.head.next
        last = self.head
        while temp != self.head:
            last = last.next
            temp = temp.next
        print(last.next.data)

    def push_front(self, data):
        item = Node(data)
        if self.head == None:
            self.head = item
            item.next = item
        else:
            item.next = self.head
            temp = self.head.next
            last = self.head
            while temp != self.head:
                last = last.next
                temp = temp.next
            self.head = item
            last.next = item
        self.size += 1

    def push_back(self, data):
        item = Node(data)
        if self.head == None:
            self.push_front(data)
        else:
            temp = self.head.next
            last = self.head
            while temp != self.head:
                last = last.next
                temp = temp.next
            last.next = item
            item.next = self.head
            self.size += 1
        
    def insert(self, index, data):
        if not((index[1::].isdigit() and index[0] == '-') or index.isdigit()):
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
            item.next = curr
            self.size += 1

    def find_item(self, data): #поиск элемента по значению
        temp = self.head
        count_heads = 0
        index = 0
        while (temp.data != data):
            index += 1
            temp = temp.next
            if temp == self.head:
                count_heads += 1
                break
        if count_heads == 1:
            return "ErRoR"
        else:
            return index

    def find_index(self, index): #поиск элемента по индексу
        if not((index[1::].isdigit() and index[0] == '-') or index.isdigit()):
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
        elif self.size == 1:
            item = self.head
            self.size = 0
            self.head = None
            return item.data
        else:
            item = self.head
            temp = self.head.next
            last = self.head
            while temp != self.head:
                last = last.next
                temp = temp.next
            self.head = item.next
            last.next = self.head
            self.size -= 1
            return item.data

    def pop_back(self):
        if self.head == None:
            return "ErRoR"
        elif self.size == 1:
            item = self.head
            self.size = 0
            self.head = None
            return item.data
        else:
            temp = self.head
            while (temp.next.next != self.head):
                temp = temp.next
            item = temp.next 
            temp.next = self.head
            self.size -= 1
            return item.data

    def pop(self, index):
        if not((index[1::].isdigit() and index[0] == '-') or index.isdigit()):
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
            self.size -= 1
            return item.data

    def remove(self, index, length):
        if (not((index[1::].isdigit() and index[0] == '-') or index.isdigit())) or (not length.isdigit()):
            return "ErRoR"
        index = int(index)
        length = int(length)
        if index + length < 0 or index + length - 1 > self.size - 1:
            return "ErRoR"
        elif self.head == None:
            return "empty"
        else:
            for i in range(0, length):
                index = str(index)
                temp = self.pop(index)

    def clear(self):
        if self.head == None:
            return "list is already empty"
        temp = self.head.next
        while temp != self.head:
            temp.data = None
            temp = temp.next
        self.size = 0
        self.head = None

    # Мне было скучно
    def reverse(self):
        if self.head == None:
            return "ErRoR"
        item = self.head
        previous_item = None
        while True:
            next_item = item.next
            item.next = previous_item
            previous_item = item
            item = next_item
            if item == self.head:
                break
        self.head = previous_item
        temp = self.head.next
        last = self.head
        while temp != None:
            last = last.next
            temp = temp.next
        last.next = self.head
        
    def count(self, item): #Подсчет количества элементов с заданным значением
        if self.head == None:
            return "ErRoR"
        else:
            count = 0
            temp = self.head
            while True:
                if temp.data == item:
                    count += 1
                temp = temp.next
                if temp == self.head:
                    break
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
            while True:
                sorted += [temp.data]
                temp = temp.next
                if temp == self.head:
                    break
            sorted.sort()
            self.clear()
            for i in sorted:
                self.push_back(i)
            return self

    def find_neighbours(self, item): #Поиск соседних элементов к данному
        if self.head == None:
            return "ErRoR", "ErRoR"
        else:
            temp = self.head.next
            prev = self.head
            while True:
                prev = prev.next
                temp = temp.next
                if temp == self.head:
                    break
            temp = self.head
            count_heads = 0
            while True:
                if temp.data == item:
                    break
                prev = temp
                temp = temp.next
                if temp == self.head:
                    count_heads += 1
                    break
            if count_heads > 0:
                return "ErRoR 404", "ErRoR 404"
            next = temp.next
            return prev.data, next.data

    #helpers
    def is_digit(self):
        if self.head == None:
            return "ErRoR"
        temp = self.head
        count_not_numbers = 0
        while True:
            if not((temp.data[1::].isdigit() and temp.data[0] == '-') or temp.data.isdigit()):
                count_not_numbers += 1
            temp = temp.next
            if temp == self.head:
                break
        if count_not_numbers > 0:
            return False
        else:
            return True

    def find_maximum(self):
        result = self.is_digit()
        if result == "ErRoR":
            return "empty"
        elif result:
            temp = self.head
            maximum = int(temp.data)
            while True:
                if int(temp.data) > maximum:
                    maximum = int(temp.data)
                temp = temp.next
                if temp == self.head:
                    break
            return maximum
        else:
            return "ErRoR"
            
    #Индивидуальное задание 1-17: Имеется список целых чисел. Удалить из него все четные числа. doubly linked list?????????????????????????????????????????????? 
    #Имеется список целых чисел. Все нечетные числа в нем умножить на 2, все четные разделить на 2.
    def inverse_numbers(self):
        result = self.is_digit()
        if result == "ErRoR":
            return "empty"
        elif result:
            temp = self.head
            while True:
                if int(temp.data) % 2 == 0:
                    temp.data = str(int(temp.data)//2)
                elif int(temp.data) % 2 == 1:
                    temp.data = str(int(temp.data)*2)
                temp = temp.next
                if temp == self.head:
                    break
            return self
        else:
            return "ErRoR"
    
    #Индивидуальное задание 2-17: Удалить из списка действительных чисел все максимальные элементы
    def delete_maximum(self):
        maximum = str(self.find_maximum())
        if maximum == "empty":
            return "empty"
        elif maximum == "ErRoR":
            return "ErRoR"
        else:
            index = self.find_item(maximum)
            while index != "ErRoR":
                deleted = self.pop(str(index))
                index = self.find_item(maximum)
            return "Ok"

# Взаимодействие с пользователем
x = input("Добро пожаловать!\nЕсли вы хотите вывести набор команд: введите Menu\nЕсли вы хотите посмотреть список: введите Show\nЕсли вы хотите добавить элементы в список: введите Add\nЕсли вы хотите удалить элементы из списка: введите Remove\nЕсли вы хотите найти элемент в списке: введите Find Value\nЕсли вы хотите вывести определенный элемент из списка: введите Find Index\nЕсли вы хотите развернуть список: введите Reverse\nЕсли вы хотите очистить список: введите Clear\nЕсли вы хотите узнать количество вхождений некоторого элемента: введите Count\nЕсли вы хотите отсортировать список: введите Sort\nЕсли вы хотите найти соседей элемента: введите Find Neighbours\nЕсли вы хотите проверить состоит ли список только из численных элементов: введите Is Digit\nЕсли вы хотите все нечетные числа в списке умножить на 2, а все четные разделить на 2: введите Inverse Numbers\nЕсли вы хотите узнать значение максимального элемента: введите Find Maximum\nЕсли вы хотите удалить из списка действительных чисел все максимальные элементы: введите Delete Maximum\nЕсли вы хотите закончить: введите Stop\n")
mylist = Circular_Linked_List()
while (x):
    x = x.lower()
    match x:
        case "menu":
            print("Если вы хотите вывести набор команд: введите Menu\nЕсли вы хотите посмотреть список: введите Show\nЕсли вы хотите добавить элементы в список: введите Add\nЕсли вы хотите удалить элементы из списка: введите Remove\nЕсли вы хотите найти элемент в списке: введите Find Value\nЕсли вы хотите вывести определенный элемент из списка: введите Find Index\nЕсли вы хотите развернуть список: введите Reverse\nЕсли вы хотите очистить список: введите Clear\nЕсли вы хотите узнать количество вхождений некоторого элемента: введите Count\nЕсли вы хотите отсортировать список: введите Sort\nЕсли вы хотите найти соседей элемента: введите Find Neighbours\nЕсли вы хотите проверить состоит ли список только из численных элементов: введите Is Digit\nЕсли вы хотите все нечетные числа в списке умножить на 2, а все четные разделить на 2: введите Inverse Numbers\nЕсли вы хотите узнать значение максимального элемента: введите Find Maximum\nЕсли вы хотите удалить из списка действительных чисел все максимальные элементы: введите Delete Maximum\nЕсли вы хотите закончить: введите Stop")
        case "show":
            print(mylist)
            # mylist.print_next()
        case "add":
            message = input("Если вы хотите линейно заполнить список: введите Fill, если же добавить один элемент по индексу: введите Add\n")
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
                else:
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
        case "find neighbours":
            item = input("Введите элемент, соседей которого хотите найти: ")
            prev, next = mylist.find_neighbours(item)
            if prev == "ErRoR":
                print("YOU LOSER")
                print("Что вы собрались искать в пустом списке (｡· v ·｡)?")
            elif prev == "ErRoR 404":
                print("ErRoR 404")
            else:
                print("У элемента ", item, " предыдущий элемент: ", prev, ", а следующий: ", next, sep = "")
        case "is digit":
            result = mylist.is_digit()
            if result == "ErRoR":
                print("YOU LOSER")
                print("Что вы собрались проверять в пустом списке (｡· v ·｡)?")
            elif result:
                print("Список состоит только из чисел")
            else:
                print("В списке присутствуют не только численные элементы")
        case "inverse numbers":
            result = mylist.inverse_numbers()
            if result == "empty":
                print("YOU LOSER")
                print("Что вы собрались делать в пустом списке (｡· v ·｡)?")
            elif result == "ErRoR":
                print("YOU LOSER")
                print("В списке присутствуют не только численные элементы")
            else:
                print("Список успешно преобразован")
        case "find maximum":
            result = mylist.find_maximum()
            if result == "empty":
                print("YOU LOSER")
                print("Что вы собрались искать в пустом списке (｡· v ·｡)?")
            elif result == "ErRoR":
                print("YOU LOSER")
                print("В списке присутствуют не только численные элементы")
            else:
                print("Максимальный элемент в списке:", result)
        case "delete maximum":
            result = mylist.delete_maximum()
            if result == "empty":
                print("YOU LOSER")
                print("Что вы собрались удалять в пустом списке (｡· v ·｡)?")
            elif result == "ErRoR":
                print("YOU LOSER")
                print("В списке присутствуют не только численные элементы")
            else:
                print("Список успешно почищен от всех максимальных элементов")
        case "stop":
            break
    x = input("Введите еще команду: ")

```

```python

```
