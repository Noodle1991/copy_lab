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
<h3>Отчет</h3>
<h3>Лабораторная работа #3 
Линейные двунаправленные списки (Doubly linked list)
</h3>
<h4>Цель работы</h4>
<h5>изучение структуры данных «линейные двунаправленные списки», а также основных операций над ними.</h5>
 <h5>Реализовать программу, выполняющую стандартный набор операций с линейным двунаправленным списком:</h5>


**1.** Реализовать программу, выполняющую стандартный набор операций с линейным двунаправленным списком:
 - вставка элемента в начало списка;
 - вставка элемента в середину списка перед указанным значением;
 - вставка элемента в середину списка после указанного значения;
 - вставка элемента в конец списка;
 - удаление элемента в начале списка;
 - Удаление элемента, стоящего перед указанным значением списка;
 - Удаление элемента, стоящего после указанного значением списка;
 - удаление определенного элемента в списке;
 - удаление элемента в конце списка;
 - очистка списка;
 - поиск элемента списка по его значяению;
 - реверс списка (переворачивание списка задо на перед).
 

<h4>Требования: </h4>
 - список должен быть реализован в виде класса;
 - каждая операция должна быть реализована как метод класса;
 - добавлению/удалению должна предшествовать проверка возможности выполнения этих операций;

**2.** Реализовать приложение, для работы со списком, которое реализует следующий набор действий:
 
 а) инициализация пустого линейного однонаправленного списка;
 
 б) организация диалогового цикла с пользователем;

 **3** Реализовать индивидуальное задание.


### Индивидуальные задания
1. Написать функцию, которая по двум линейным спискам L1 и L2 формирует новый список L, состоящий из элементов, входящих в оба списка.
2. Пусть имеется список L. Удалить из него каждый третий элемент.
<!-- #endregion -->

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            new_node.prev = current

    def prepend(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def insert_before(self, value, data):
        if not self.head:
            return
        new_node = Node(data)
        current = self.head
        while current:
            if current.data == value:
                new_node.prev = current.prev
                new_node.next = current
                if current.prev:
                    current.prev.next = new_node
                current.prev = new_node
                if current == self.head:
                    self.head = new_node
                return
            current = current.next

    def insert_after(self, value, data):
        if not self.head:
            return
        new_node = Node(data)
        current = self.head
        while current:
            if current.data == value:
                new_node.prev = current
                new_node.next = current.next
                if current.next:
                    current.next.prev = new_node
                current.next = new_node
                return
            current = current.next

    def delete_front(self):
        if self.head:
            self.head = self.head.next
            if self.head:
                self.head.prev = None

    def delete_before(self, value):
        if not self.head:
            return
        current = self.head
        while current:
            if current.data == value and current.prev:
                current.prev = current.prev.prev
                if current.prev:
                    current.prev.next = current
                return
            current = current.next

    def delete_after(self, value):
        if not self.head:
            return
        current = self.head
        while current:
            if current.data == value and current.next:
                current.next = current.next.next
                if current.next:
                    current.next.prev = current
                return
            current = current.next

    def delete_value(self, value):
        current = self.head
        while current:
            if current.data == value:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next
                if current.next:
                    current.next.prev = current.prev
                return
            current = current.next

    def delete_end(self):
        current = self.head
        while current and current.next:
            current = current.next
        if current:
            if current.prev:
                current.prev.next = None
            else:
                self.head = None

    def clear(self):
        self.head = None

    def search(self, value):
        current = self.head
        while current:
            if current.data == value:
                return True
            current = current.next
        return False

    def reverse(self):
        current = self.head
        while current:
            current.prev, current.next = current.next, current.prev
            if not current.next:
                self.head = current
            current = current.next



    def display(self):
        current = self.head
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")

def intersection(L1, L2):
    result = DoublyLinkedList()

        # Создаем множество для хранения уникальных элементов из L1
    unique_elements = set()

        # Проходим по L1 и добавляем элементы в множество
    current = L1.head
    while current:
        unique_elements.add(current.data)
        current = current.next

        # Проходим по L2 и если элемент есть в множестве unique_elements, добавляем его в результат
    current = L2.head
    while current:
        if current.data in unique_elements:
            result.append(current.data)
        current = current.next

    return result

def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

    # Функция для создания списка L2 из простых чисел из списка L1
def create_prime_list(L1):
    L2 = DoublyLinkedList()
    current = L1.head
    while current:
        if is_prime(current.data):
            L2.append(current.data)
        current = current.next
    return L2
    
L1 = DoublyLinkedList()

L1.append(2)
L1.append(3)
L1.append(4)
L1.append(5)
L1.append(6)

L2 = create_prime_list(L1)

L2.display()

L1 = DoublyLinkedList()
L2 = DoublyLinkedList()

L1.append(1)
L1.append(2)
L1.append(3)

L2.append(2)
L2.append(3)
L2.append(4)

result = intersection(L1, L2)

result.display()

L2 = create_prime_list(L1)


class LinkedListApp:
    def __init__(self):
        self.dlist = DoublyLinkedList()

    def run(self):
        while True:
            print("Выберите действие:")
            print("1. Вставить элемент в начало списка")
            print("2. Вставить элемент перед указанным значением")
            print("3. Вставить элемент после указанного значением")
            print("4. Вставить элемент в конец списка")
            print("5. Удалить элемент в начале списка")
            print("6. Удалить элемент перед указанным значением")
            print("7. Удалить элемент после указанного значением")
            print("8. Удалить элемент по значению")
            print("9. Удалить элемент в конце списка")
            print("10. Очистить список")
            print("11. Поиск элемента по значению")
            print("12. Реверс списка")
            print("13. Вывести список")
            print("0. Выход")

            choice = int(input("Ваш выбор: "))

            if choice == 1:
                data = input("Введите значение: ")
                self.dlist.prepend(data)
            elif choice == 2:
                value = input("Введите значение, перед которым нужно вставить новый элемент: ")
                data = input("Введите значение нового элемента: ")
                self.dlist.insert_before(value, data)
            elif choice == 3:
                value = input("Введите значение, после которого нужно вставить новый элемент: ")
                data = input("Введите значение нового элемента: ")
                self.dlist.insert_after(value, data)
            elif choice == 4:
                data = input("Введите значение: ")
                self.dlist.append(data)
            elif choice == 5:
                self.dlist.delete_front()
            elif choice == 6:
                value = input("Введите значение, перед которым нужно удалить элемент: ")
                self.dlist.delete_before(value)
            elif choice == 7:
                value = input("Введите значение, после которого нужно удалить элемент: ")
                self.dlist.delete_after(value)
            elif choice == 8:
                data = input("Введите значение, которое нужно удалить: ")
                self.dlist.delete_value(data)
            elif choice == 9:
                self.dlist.delete_end()
            elif choice == 10:
                self.dlist.clear()
            elif choice == 11:
                data = input("Введите значение для поиска: ")
                if self.dlist.search(data):
                    print("Значение найдено в списке.")
                else:
                    print("Значение не найдено в списке.")
            elif choice == 12:
                self.dlist.reverse()
            elif choice == 13:
                self.dlist.display()
            elif choice == 0:
                break
            else:
                print("Неправильный выбор. Попробуйте снова.")


if __name__ == "__main__":
    app = LinkedListApp()
    app.run()
```

### Контрольные вопросы

1. Что такое динамическая структура данных?
Динамическая структура данных:
Динамическая структура данных - это структура данных, которая позволяет изменять свой размер во времени, а также эффективно управлять добавлением, удалением и доступом к элементам. Она не имеет фиксированного размера и может автоматически расширяться или сжиматься по мере необходимости. Это позволяет оптимизировать использование памяти и ресурсов при работе с данными.

2. Что такое список?
Список:
Список - это одна из наиболее распространенных динамических структур данных. Список представляет собой упорядоченную коллекцию элементов, где каждый элемент может содержать данные различных типов. Списки могут быть изменяемыми, их размер может изменяться по мере добавления или удаления элементов.

3. Какие виды списков существуют?
Виды списков:
Существует несколько разновидностей списков, включая:
    1. Связанный список (Linked List): Элементы связаны между собой с помощью ссылок, что позволяет эффективно вставлять и удалять элементы, но усложняет доступ к элементам по индексу.
    2. Динамический массив (Dynamic Array): Это массив, который может изменять свой размер по мере необходимости. Это позволяет быстрый доступ к элементам по индексу, но вставка и удаление элементов в середине может быть дорогой операцией.
    3. Связанный список с хвостовой ссылкой (Doubly Linked List): Похож на связанный список, но каждый элемент имеет две ссылки - на следующий и на предыдущий элемент. Это облегчает вставку и удаление элементов в обе стороны.

4. Какие основные операции выполняются над списком?
Основные операции над списком:
Основные операции, которые можно выполнять над списком, включают:
    1. Вставка элемента: Добавление нового элемента в список.
    2. Удаление элемента: Удаление элемента из списка.
    3. Доступ к элементу по индексу: Получение элемента по его порядковому номеру.
    4. Поиск элемента: Поиск элемента по его значению.
    5. Обход списка: Перебор всех элементов списка.
5. Особенности выполнения операции вставки первого и не первого элемента в двунаправленный список.
Особенности вставки и удаления в двунаправленном списке:
В двунаправленном списке (Doubly Linked List) вставка и удаление элементов имеют следующие особенности:

    1. Вставка первого элемента:
       - При вставке первого элемента в пустой список необходимо обновить ссылки на "голову" (head) и "хвост" (tail).
       - В двунаправленном списке это требует изменения только одной ссылки.

    2. Вставка не первого элемента:
       - При вставке элемента в середину списка необходимо обновить ссылки на предыдущий и следующий элементы, чтобы вставляемый элемент указывал на своих соседей, и их соседи указывали на вставляемый элемент.
    
6. Особенности выполнения операции удаления первого и не первого элемента.
Особенности вставки и удаления в двунаправленном списке:
В двунаправленном списке (Doubly Linked List) вставка и удаление элементов имеют следующие особенности:

    1. Вставка первого элемента:
       - При вставке первого элемента в пустой список необходимо обновить ссылки на "голову" (head) и "хвост" (tail).
       - В двунаправленном списке это требует изменения только одной ссылки.

    2. Вставка не первого элемента:
       - При вставке элемента в середину списка необходимо обновить ссылки на предыдущий и следующий элементы, чтобы вставляемый элемент указывал на своих соседей, и их соседи указывали на вставляемый элемент.

    3. Удаление первого элемента:
       - При удалении первого элемента необходимо обновить ссылки на "голову" (head) и предыдущий элемент новой "головы", а также обнулить ссылки на удаленный элемент.

    4. Удаление не первого элемента:
       - При удалении элемента из середины списка необходимо обновить ссылки на предыдущий и следующий элементы, чтобы они указывали друг на друга, обходя удаляемый элемент.о  эа друга, обходя удаляемый элемент.

Двунаправленный список облегчает вставку и удаление элементов в обе стороны, но требует больше памяти для хранения дополнительных ссылок на предыдущий элемент.
