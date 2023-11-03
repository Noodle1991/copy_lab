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
<h3> Лабораторная работа №5 <br> <br>
    «Стек (Stack)» </h3>
<br>
<h4> Цель работы: </h4>
Изучение структуры данных «Стек», а также основных операций над ним.
<br>
<br>
<h4> Постановка задачи: </h4>

1. Написать собственную реализацию стека в виде класса. Приэтом каждая его операция должна быть реализована как метод класса и добавлению/удалению элемента должна предшествовать проверка возможности выполнения этих операций.
2. Реализовать программу, выполняющую стандартный набор операций над стеком:
    * запись элемента в стек;
    * просмотр стека;
    * удаление элемента из стека;
    * проверка стека на пустоту;
    * очистка стека;
    * чтение вершины стека.
3. Реализовать приложение, для работы со стеком, которое реализует следующий набор действий:
    * инициализация пустого стека;
    * организация диалогового цикла с пользователем;
<br>
<br>
<h4> Code Listing: </h4>

```python
class Node: 
    def __init__(self, data, next = None)

class Stack:
    def __init__(self) #инициализация стека

    def __str__(self) #вывод стека

    def is_empty(self) #проверка стека на пустоту

    def push_front(self, data) #запись элемента в стек
    
    def pop_front(self) #удаление элемента из стека

    def top(self) #чтение вершины стека
    
    def clear(self) #очистка стека
    
    #additions
    def remove(self, length) #удаление нескольких верхних элементов стека
    
    def find_item(self, data) #поиск элемента по значению
    
    def reverse(self) #поворот стека задом наперед
    
#individuals
def closing_brackets(string) #программа, проверяющая своевременность закрытия скобок

def postfix_entry(string) #программа вычисления значения выражения, представленного в постфиксной записи

#Взаимодействие с пользователем
x = input("...")
while (x):
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
        
        case "remove":
            ///код

        case "get top":
            ///код

        case "clear":
            ///код
        
        case "is item":
            ///код

        case "reverse":
            ///код
        
        case "stop":
            ///код
    ///код
```
<br>
<h4> Выводы </h4>
В ходе лабораторной работы была изучена структура данных «стек», написана собственнаяя реализация стека в виде класса таким образом, что каждая его операция является методом класса. Реализована программа, выполняющая стандартный набор операций со стеком и приложение, которое осуществляет диалоговый цикл с пользователем.
<br>
<br>
<h4> Ответы на контрольные вопросы </h4>

1. *Что такое динамическая структура данных?* <br>
Динамические структуры данных – это структуры данных, память под которые выделяется и освобождается по мере необходимости в процессе выполнения программы, а не в момент ее запуска. Динамические структуры данных в процессе существования в памяти могут изменять не только число составляющих их элементов, но и характер связей между элементами. <br>
2. *Что такое стек?* <br>
Стек — это специальный тип списка, в котором все операции вставки и удаления выполняются только на одном конце, называемом вершиной (top). <br>
3. *Особенности выполнения операций со стеком.*<br>
В любой момент времени можно получить доступ только к верхнему элементу стека.<br>
4. *Основные операции со стеком.*<br>
    * запись элемента в стек<br>
    * просмотр стека<br>
    * удаление элемента из стека<br>
    * проверка стека на пустоту<br>
    * очистка стека<br>
    * чтение вершины стека<br>
<!-- #endregion -->

```python
class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

class Stack:
    def __init__(self):
        self.size = 0
        self.top = None
        
    def __str__(self):
        if self.is_empty():
            text = "stack is empty: " + str(self.size) + " " + str(self.top)
        else:
            text = "stack size = " + str(self.size) + "\ntop is = " + str(self.top.data) + "\nstack: "
            temp = self.top
            while temp:
                text += str(temp.data) + " "
                temp = temp.next
        return text
        
    def is_empty(self):
        if self.top == None:
            return True
        else:
            return False
        
    def push_front(self, data):
        item = Node(data)
        if self.is_empty():
            self.top = item
        else:
            item.next = self.top
            self.top = item
        self.size += 1
   
    def pop_front(self):
        if self.is_empty():
            return "ErRoR"
        else:
            item = self.top
            self.top = item.next
            self.size -= 1
            return item.data

    def get_top(self):
        if self.is_empty():
            return "ErRoR"
        else:
            return self.top.data

    def clear(self):
        if self.is_empty():
            return "list is already empty"
        temp = self.top
        while temp != None:
            temp.data = None
            temp = temp.next
        self.size = 0
        self.top = None

    #additions
    def remove(self, length):
        length = int(length)
        if length < 0 or length - 1 > self.size - 1:
            return "ErRoR"
        elif self.is_empty():
            return "empty"
        else:
            for i in range(0, length):
                temp = self.pop_front()
                
    def find_item(self, data): #поиск элемента по значению
        temp = self.top
        while (temp != None and temp.data != data):
            temp = temp.next
        if temp == None:
            return False
        else:
            return True

    def reverse(self):
        if self.is_empty():
            return "ErRoR"
        item = self.top
        previous_item = None
        while (item != None):
            next_item = item.next
            item.next = previous_item
            previous_item = item
            item = next_item
        self.top = previous_item

#individuals
def closing_brackets(string):
    i = 0
    mystack = Stack()
    if len(string)%2 != 0:
        return "wrong string"
    while i < len(string):
        if (string[i] in "([{"):
            mystack.push_front(string[i])
            i+=1
        else:
            match string[i]:
                case ")":
                    if mystack.get_top() == "(":
                        deleted = mystack.pop_front()
                    else:
                        return "wrong string"
                        break
                case "]":
                    if mystack.get_top() == "[":
                        deleted = mystack.pop_front()
                    else:
                        return "wrong string"
                        break
                case "}":
                    if mystack.get_top() == "{":
                        deleted = mystack.pop_front()
                    else:
                        return "wrong string"
                        break
                case _:
                    return "wrong string"
            i+=1
    return True

print(closing_brackets("{{[()]}}"), "True")
print(closing_brackets("{{}}[()]{}{}"), "True")
print(closing_brackets("{}[]()"), "True")
print(closing_brackets("({[()]}}"), "wrong string")
# print(closing_brackets("q{[()]}}"), "wrong string")
# print(closing_brackets("{{[()]}w"), "wrong string")
print(closing_brackets("{{[()]}]"), "wrong string")
print(closing_brackets("{{[(]}}"), "wrong string")

def postfix_entry(string):
    mystack = Stack()
    for i in range(0, len(string)):
        if string[i].isdigit():
            mystack.push_front(string[i])
        else:
            a = int(mystack.pop_front())
            b = int(mystack.pop_front())
            match string[i]:
                case "+":
                    mystack.push_front(a+b)
                case "-":
                    mystack.push_front(a-b)
                case "*":
                    mystack.push_front(a*b)
                case "/":
                    mystack.push_front(a//b)
    return mystack.get_top()

print(postfix_entry("34+2*")) #(3+4)*2
print(postfix_entry("123+4*+")) #1+(2+3)*4

# Взаимодействие с пользователем
x = input("Добро пожаловать!\nЕсли вы хотите вывести набор команд: введите Menu\nЕсли вы хотите посмотреть стек: введите Show\nЕсли вы хотите проверить пустой ли стек: введите Is Empty\nЕсли вы хотите добавить элементы в стек: введите Add\nЕсли вы хотите удалить элементы из стека: введите Remove\nЕсли вы хотите вывести вершину стека:введите Get Top\nЕсли вы хотите очистить стек: введите Clear\nЕсли вы хотите проверить наличие элемента в стеке: введите Is Item\nЕсли вы хотите развернуть стек: введите Reverse\nЕсли вы хотите закончить: введите Stop\n")
mystack = Stack()
while (x):
    x = x.lower()
    match x:
        case "menu":
            print("Если вы хотите вывести набор команд: введите Menu\nЕсли вы хотите посмотреть стек: введите Show\nЕсли вы хотите проверить пустой ли стек: введите Is Empty\nЕсли вы хотите добавить элементы в стек: введите Add\nЕсли вы хотите удалить элементы из стека: введите Remove\nЕсли вы хотите вывести вершину стека:введите Get Top\nЕсли вы хотите очистить стек: введите Clear\nЕсли вы хотите проверить наличие элемента в стеке: введите Is Item\nЕсли вы хотите развернуть стек: введите Reverse\nЕсли вы хотите закончить: введите Stop")
        case "show":
            print(mystack)
        case "is empty":
            if mystack.is_empty():
                print("Стек пустой")
            else:
                print("Стек не пустой")
        case "add":
            message = input("Если вы хотите линейно заполнить стек: введите Fill, если же добавить один элемент: введите Add\n")
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
                        print("Если вдруг вы устанете заполнять стек и захотите прервать процесс: введите ~I'm LoSeR~")
                        count_elements = 0
                        length = int(length)
                        flag = True
                        for i in range(0, length):
                            if not flag:
                                break
                            item = input("Введите элемент: ")
                            if item == "~I'm LoSeR~":
                                while True:
                                    exit = input("Если вы хотите закончить заполнение стека: введите Break, если добавить элемент ~I'm LoSeR~: введите Add\n")
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
                                            result = mystack.push_front(item)
                                            count_elements += 1
                                            break
                                        else:
                                            print("YOU LOSER")
                                            print("Надо было ввести команду :З")
                                            print("Попробуйте еще раз")
                            else:
                                mystack.push_front(item)
                                count_elements += 1
                        if count_elements == length:
                            print("Стек успешно заполнен")
                elif message == "add":
                    item = input("Введите элемент: ")
                    mystack.push_front(item)
                    print("Вы добавили элемент", item)
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
                    length = input("Введите количество элементов для удаления: ")
                    result = mystack.remove(length)
                    if result == "ErRoR":
                        print("YOU LOSER")
                        print("В следующий раз стоит вводить корректное количество элементов для удаления :З")
                    elif result == "empty":
                        print("А что вы собрались удалять в пустом стеке (｡· v ·｡)?")
                    else:
                        print("Вы удалили", length, "элементов")
                elif message == "pop":
                    result = mystack.pop_front()
                    if result == "ErRoR":
                        print("YOU LOSER")
                        print("А что вы собрались удалять в пустом стеке (｡· v ·｡)?")
                    else:
                        print("Вы удалили элемент", result)
                else:
                        print("YOU LOSER")
                        print("Вы ввели неправильную команду :З")
        case "get top":
            result = mystack.get_top()
            if result == "ErRor":
                print("У пустого стека нет вершины :З")
            else:
                print("Вершина стека - элемент", result)
        case "clear":
            if mystack.clear() == "list is already empty":
                print("YOU LOSER")
                print("Не стоит пытаться очистить пустой стек :З")
            else:
                print("Вы очистили стек, его элементы больше не доступны :(")
        case "is item":
            value = input("Введите элемент: ")
            result = mystack.find_item(value)
            if result:
                print("Элемент найден в стеке")
            else:
                print("Элемент не найден в стеке")
        case "reverse":
            if mystack.reverse() == "ErRoR":
                print("YOU LOSER")
                print("Не пытайтесь развернуть пустой стек :З")
            else:
                print("Вы развернули стек")
        case "stop":
            break
    x = input("Введите еще команду: ")

```

```python

```
