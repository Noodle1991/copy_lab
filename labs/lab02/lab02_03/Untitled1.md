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

<h3>Отчет</h3>
<h3>Лабораторная работа #2 <br> <br>
«Линейные однонаправленные списки (Singly Linked Lists)»
</h3>
<h4> Цель работы: </h4>
<h5>Изучение структуры данных «линейные однонаправленные списки, а также основных операций над ними.</h5>.
<b <br>
<h4> Постановка задачи: </h4>

1. Написать собственную реализацию однонаправленного списка в виде класса. Приэтом каждая его операция должна быть реализована как метод класса и добавлению/удалению элемента должна предшествовать проверка возможности выполнения этих операций.
2. Реализовать программу, выполняющую стандартный набор операций с линейным однонаправленным списком:
    * вставка элемента в линейный однонаправленный список (в начало, середину, конец);
    * просмотр линейного однонаправленного списка;
    * поиск элемента в линейном однонаправленном списке;
    * удаление элемента из линейного однонаправленного списка (из начала, середины, конца);
    * реверс списка (переворачивание списка задом на перед).
3. Реализовать приложение, для работы со списком, которое реализует следующий набор действий:
    * инициализация пустого линейного однонаправленного списка;
    * организация диалогового цикла с пользователем
4. Индивидуальное задание
    * Определить, является ли список упорядоченным по возрастанию.
    * Определить, образуют ли элементы списка действительных чисел геометрическую прогрессию.Listing: </h4>br>

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def append(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
    def append_begin(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def append_index(self, data, index):
        if index < 0:
            print("Index out of list")
            return

        if index == 0:
            self.append_begin(data)
            return

        new_node = Node(data)
        current = self.head
        i = 0
        while current:
            if i == index - 1:
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next
            i += 1

        print("Index out of list")

        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next

    def pop_begin(self):
        if not self.is_empty():
            self.head = self.head.next

    def pop(self):
        if not self.is_empty():
            if not self.head.next:
                self.head = None
            else:
                current = self.head
                while current.next.next:
                    current = current.next
                current.next = None

    def pop_index(self, index):
        if index < 0:
            print("Index out of list")
            return

        if index == 0:
            self.pop_begin()
            return

        current = self.head
        i = 0
        while current:
            if i == index - 1 and current.next:
                current.next = current.next.next
                return
            current = current.next
            i += 1

        print("Index out of list")
    def get(self, index):
        if self.is_empty():
            return None

        current = self.head
        i = 0
        while current:
            if i == index:
                return current.data
            current = current.next
            i += 1

        return None

    def reverse(self):
        prev = None
        current = self.head

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        self.head = prev
    def display(self):
        result = "["
        current = self.head
        while current:
            result += str(current.data)
            if current.next:
                result += ", "
            current = current.next
        return result + "]"

    def is_sorted(self):
        current = self.head

        while current and current.next:
            if current.data > current.next.data:
                return False
            current = current.next

        return True

    def is_geometric_progression(self):
        current = self.head

        if current is None:
            return True  # Пустой список считается геометрической прогрессией

        # Находим знаменатель прогрессии
        ratio = current.data / (current.next.data if current.next else current.data)

        while current and current.next:
            if current.data / current.next.data != ratio:
                return False
            current = current.next

        return True
# Пример использования класса LinkedList:
my_list = LinkedList()

# Проверка на пустоту
print(my_list.is_empty())  # True

# Добавление элементов
my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.append_begin(54)
my_list.append_index(777, 2)
# Вывод элементов
print(my_list.display())

# Проверка is_sorted
print(my_list.is_sorted(), "is sorted")

# Проверка на геометрическую прогрессию
print(my_list.is_geometric_progression(), "progression")

# Удаление элемента
my_list.pop()
my_list.pop_begin()
my_list.pop_index(2)
print(my_list.display(), "delet")

# Реверс списка
my_list.reverse()
print(my_list.display())

# Получение элемента по индексу
print(my_list.get(0))

def main():
    my_list = LinkedList()

    while True:
        print("\nМеню:")
        print("1. Добавить элемент в список")
        print("2. Удалить элемент из списка")
        print("3. Отобразить список")
        print("4. Выйти")

        choice = input("Выберите действие: ")

        if choice == '1':
            data = input("Введите элемент для добавления: ")
            my_list.append(data)
            print(f"Элемент '{data}' добавлен в список.")
        elif choice == '2':
            data = input("Введите индекс элемент для удаления: ")
            my_list.pop_index(int(data))
            print(f"Элемент '{data}' удален из списка.")
        elif choice == '3':
            print("Список:")
            print(my_list.display())
        elif choice == '4':
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор. Попробуйте еще раз.")

if __name__ == "__main__":
    main()

```

<br>
<h4> Выводы </h4>
В ходе лабораторной работы была изучена структура данных «линейные однонаправленные 
списки», написана собственнаяя реализация однонаправленного списка в виде класса 
таким образом, что каждая его операция является методом класса. Реализована 
программа, выполняющая стандартный набор операций с линейным однонаправленным 
списком и приложение, которое осуществляет диалоговый цикл с пользователем.
<br>
<br>
<h4> Ответы на контрольные вопросы </h4>

1. *Что такое динамическая структура данных?* <br>
Динамические структуры данных – это структуры данных, память под которые выделяется и освобождается по мере необходимости в процессе выполнения программы, а не в момент ее запуска. Динамические структуры данных в процессе существования в памяти могут изменять не только число составляющих их элементов, но и характер связей между элементами. <br>
2. *Что такое список?* <br>
Список — это упорядоченный набор элементов, каждый из которых имеет свой номер, или индекс, позволяющий быстро получить к нему доступ
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
5. *Особенности выполнения операций вставки первого и не первого элемента.* <br>
В линейном однонаправленном списке при вставке первого элемента надо менять указатель head, а при вставке последующих элементов нужно изменять указатель предыдущего элемента.<br>
6. *Особенности выполнения операций удаления первого и не первого элемента.* <br>
При удалении первого элемента в линейном однонаправленном списке, также как и при вставке нужно изменять указатель head, а при удалении последующих надо менять указатели предыдущих.му доступ.<br>


```python

```
