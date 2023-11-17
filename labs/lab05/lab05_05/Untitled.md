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


# Отчет

## Лабораторная работа №5

### Линейный однонаправленный список

### Цель работы:

Изучение структуры данных «Стек», а также основных операций над ним.

### Задачи:

1. Реализовать программу, выполняющую стандартный набор операций с линейным двунаправленным списком:

- стек должен быть реализован в виде класса;
- каждая операция должна быть реализована как метод класса;
- добавлению/удалению должна предшествовать проверка возможности выполнения этих операций;

2. Реализовать приложение, для работы со списком, которое реализует следующий набор действий:

а) инициализация пустого стека;

б) организация диалогового цикла с пользователем;

3 Реализовать индивидуальное задание.

- Реализовать перевод математических выражений из инфиксной в постфиксную форму записи.

### Листинг программного кода с описанием

class Node:
    def __init__(self,data)

class LinkedList:
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
  
    if x=="list" # содержит операции работы над листом
  
        while x!="end" # возвращает в главное меню
  
            if x=="add" # содержит операции добавления элемента
  
                while x!="end" # возвращает в главное меню

            if x=="delete" # содержит команды удаления
  
                while x!="end" # возвращает в главное меню
  
            if x=="clear" # очищает список
  
                while x!="end" # возвращает в главное меню

    if x=="find" # находит элемент в списке
  
        while x!="end" # возвращает в главное меню
 
    if x=="reverse" # переворачивает список
  
        while x!="end" # возвращает в главное меню

    if x=="print" # печатает список
  
        while x!="end" # возвращает в главное меню

### Ответы на контрольные вопросы

1. Что такое динамическая структура данных?

Динамические структуры данных – это структуры данных, память под которые выделяется и освобождается программистом по мере необходимости. Динамические структуры данных в процессе существования в памяти могут изменять не только число составляю-щих их элементов, но и характер связей между элементами.

2. Что такое стек?

Стек — это специальный тип списка, в котором все операции вставки и удаления выполняются только на одном конце, называемом вершиной (top).
Особенности выполнения операций со стеком.

3. Особенности выполнения операций со стеком.

В любой момент времени можно получить доступ только к верхнему элементу стека.

4. Основные операции со стеком.

- запись элемента в стек
- просмотр стека
- удаление элемента из стека
- проверка стека на пустоту
- очистка стека
- чтение вершины стека

```

```python
import sys

class Stack:
    def __init__(self):
        self.top=[]

    def push(self,item):
        self.top.append(item)

    def pop(self):
        if len(self.top)==0:
            return "Stack is empty"
            # raise ValueError('Stack is empty')
        item=self.top.pop()
        # print(item)

    def is_empty(self):
        print(len(self.top)==0)

    def size(self):
        print("Count =",len(self.top))
    
    def print(self):
        print("Stack =",self.top)

    def clear(self):
        self.top.clear()

    def tail(self):
        if len(self.top)==0:
            return "It is empty stack"
        else:
            print(self.top[-1])

    def reverse(self):
        self.top.reverse()

def brackets(string):
    i = 0
    mystack = Stack()
    if len(string)%2 != 0:
        return "wrong string"
    while i < len(string):
        if (string[i] in "([{"):
            mystack.push(string[i])
            i+=1
        else:
            if string[i]== ")":
                if mystack.top[-1] == "(":
                    mystack.pop()
                else:
                    return "wrong string"
                    break
            elif string[i]== "]":
                if mystack.top[-1] == "[":
                    mystack.pop()
                else:
                    return "wrong string"
                    break
            elif string[i]== "}":
                if mystack.top[-1] == "{":
                    mystack.pop()
                else:
                    return "wrong string"
                    break
            else:
                return "wrong string"
            i+=1
    return True

print("~~~~test_brackets~~~~")
print(brackets("{{[()]}}"), "True")
print(brackets("{{}}[()]{}{}"), "True")
print(brackets("{}[]()"), "True")
print(brackets("({[()]}}"), "wrong string")
print(brackets("q{[()]}}"), "wrong string")
print(brackets("{{[()]}w"), "wrong string")
print(brackets("{{[()]}]"), "wrong string")
print(brackets("{{[(]}}"), "wrong string")

def postfix(string):
    mystack = Stack()
    for i in range(0, len(string)):
        if string[i].isdigit():
            mystack.push(int(string[i]))
    mystack.reverse()
    for i in range(0, len(string)):
        if string[i].isdigit():
            continue
        else:
            a = int(mystack.top[-1])
            mystack.pop()
            b = int(mystack.top[-1])
            mystack.pop()
            if string[i]== "+":
                mystack.push(a+b)
            elif string[i]== "-":
                mystack.push(a-b)
            elif string[i]== "*":
                mystack.push(a*b)
            elif string[i]== "/":
                mystack.push(a//b)
    return mystack.tail()

print("~~~~test_brackets~~~~")
postfix("34+2*") #(3+4)*2
postfix("23+41*+") #1+(2+3)*4
print("\n")



st=Stack()
# st.print()
# print("~~~~test_push~~~~")
# st.push(4)
# st.push(7)
# st.push(1)
# st.push(0)
# st.push(0)
# st.push("six")
# st.push(5)
# st.push("end")
# st.push("last")
# st.print()
# print("\n")
# print("~~~~test_pop~~~~")
# st.pop()
# st.print()
# st2=Stack()
# print(st2.pop())
# st2.print()
# print("\n")
# print("~~~~test_is_empty~~~~")
# st.print()
# st.is_empty()
# st2=Stack()
# st2.print()
# st2.is_empty()
# print("\n")
# print("~~~~test_size~~~~")
# st.print()
# st.size()
# st2=Stack()
# st2.print()
# st2.size()
# print("\n")
# print("~~~~test_clear~~~~")
# st.print()
# st2=Stack()
# st2.print()
# print("print after clear:")
# st.clear()
# st.print()
# st2.print()
# st2.clear()
# print("end")
# print("\n")
# print("~~~~test_top~~~~")
# st.tail()
# print("\n")
# print("~~~~test_brackets~~~~")
# print(brackets("{{[()]}}"), "True")
# print(brackets("{{}}[()]{}{}"), "True")
# print(brackets("{}[]()"), "True")
# print(brackets("({[()]}}"), "wrong string")
# print(brackets("q{[()]}}"), "wrong string")
# print(brackets("{{[()]}w"), "wrong string")
# print(brackets("{{[()]}]"), "wrong string")
# print(brackets("{{[(]}}"), "wrong string")
# print("\n")
# print("~~~~test_reverse~~~~")
# st.reverse()
# st.print()
# print("\n")
# print("~~~~test_brackets~~~~")
# postfix("34+2*") #(3+4)*2
# postfix("23+41*+") #1+(2+3)*4
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
    print("Введите 'stack', если хотите изменять стек.")
    print("Введите 'empty', если хотите проверить стек на пустоту.")
    print("Введите 'size' чтобы узнать количество элеменов в стеке.")
    print("Введите 'print' для просмотра стек.")
    print("Введите 'stop' для завершения прошраммы.")

print("Пожалуйста введите 'start' чтобы начать.")
x=input()
clear_output()
while x!="start":
    print("Вы ввели неправильную команду. \nПожалуйста введите 'start' чтобы начать.")
    x=input()
    clear_output()
stack1=Stack()
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
    if x=="stack":
        while x!="end":
            print("Введите 'add', чтобы добавить элементы в стек.")
            print("Введите 'delete', если хотите удалить элементы из стека.")
            print("Введите 'clear', если хотите очистить стек.")
            print("Введите 'end', чтобы выйти из этого раздела.")
            x=input()
            clear_output()
            if x=="add":
                while x!="end":
                    print("Введите количество элементов, которое хотите добавить в стек.")
                    count=int(input())
                    for i in range(0,count):
                        print("Введите элемент")
                        element=input()
                        stack1.push(element)
                    print("Элементы добавлены.")
                    print("Введите 'end', чтобы выйти.")
                    x=input()
                    clear_output()
            if x=="delete":
                while x!="end":
                    print("Так ваш стек выглядит сейчас.")
                    stack1.print()
                    print("Введите количество элементов, которое хотите удалить из стека.")
                    count=int(input())
                    for i in range(0,count):
                        stack1.pop()
                    print("Элементы удалены.")
                    print("Теперь ваш стек выглядит так.")
                    stack1.print()
                    print("Введите 'end', чтобы выйти.")
                    x=input()
                    clear_output()
            if x=="clear":
                while x!="end":
                    print("Вы точно хотите очистить стек? Если да введите 'y', иначе 'n'.")
                    ok=input()
                    if ok=="y":
                        stack1.clear()
                        print("Ваш стек очищен.")
                    print("Введите 'end', чтобы выйти.")
                    x=input()
                    clear_output()
    if x=="empty":
        while x!="end":
            stack1.is_empty()
            print("Так выглядит ваш стек")
            stack1.print()
            print("Введите 'end', чтобы выйти.")
            x=input()
            clear_output()
    if x=="size":
        while x!="end":
            stack1.size()
            print("Так выглядит ваш стек.")
            stack1.print()
            print("Введите 'end', чтобы выйти.")
            x=input()
            clear_output()
    if x=="print":
        while x!="end":
            print("Сейчас ваш стек выглядит так.")
            stack1.print()
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

```python

```
