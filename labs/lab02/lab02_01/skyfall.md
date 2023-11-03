---
jupyter:
  jupytext:
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.3'
      jupytext_version: 1.15.1
  kernelspec:
    display_name: Python 3 (ipykernel)
    language: python
    name: python3
---

<h1>Акиньшин Никита Андреевич 1 Вариант </h1>



---

<!-- #region jp-MarkdownHeadingCollapsed=true -->
<h2>Структура Node для однонаправленного списка</h2>
<!-- #endregion -->

```python
class Node:

    def __init__(self, data, next=None):
        self.data = data
        self.next = next
        self.size = 0

    def getData(self):
        return self.data

    def setData(self, data):
        self.data = data

    def getNextNode(self):
        return self.next

    def setNextNode(self, node):
        self.next = node

```

<!-- #region jp-MarkdownHeadingCollapsed=true -->
<h2>Вставка элемента в линейный однонаправленный список (в начало, середину, конец)</h2>
<!-- #endregion -->

```python
    def push_back(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            self.size += 1

    def push_front(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    def insert_at_middle(self, data):
        if self.head is None:
            self.add(data)
        else:
            middle_index = self.size // 2
            current_node = self.head
            for _ in range(middle_index - 1):
                current_node = current_node.next
            new_node = Node(data)
            new_node.next = current_node.next
            current_node.next = new_node
            self.size += 1
```

<!-- #region jp-MarkdownHeadingCollapsed=true -->
<h2>Просмотр линейного однонаправленного списка</h2>
<!-- #endregion -->

```python
    def printLL(self):
        curr = self.head
        while curr:
            print(curr.data)
            curr = curr.getNextNode()
```

<!-- #region jp-MarkdownHeadingCollapsed=true -->
<h2>Поиск элемента в линейном однонаправленном списке(по индексу и по значению)</h2>
<!-- #endregion -->

```python
    def findNode(self, value):
        curr = self.head
        while curr:
            if curr.getData() == value:
                return True
            else:
                curr = curr.getNextNode()
        return False

    def at(self, index):
        if index < 0 and index >= self.size:
            raise Exception("Недопустимый индекс")
        current = self.head
        count = 0
        while count < index:
            current = current.next
            count += 1
        return current



```

<!-- #region jp-MarkdownHeadingCollapsed=true -->
<h2>Удаление элемента из линейного однонаправленного списка (из начала, середины, конца)</h2>
<!-- #endregion -->

```python
 def pop_front(self):
        if not self.head:
            print("Список пуст")
            return None
        value = self.head.data
        self.head = self.head.next
        self.size -= 1
        return value

 def pop_back(self):
        if not self.head:
            print("Список пуст")
            return None
        value = self.head.data
        if not self.head.next:
            self.head = None
            return None
        current_node = self.head
        while current_node.next.next:
            current_node = current_node.next
        current_node.next = None
        self.size -= 1
        return value

 def pop(self, index):
        if index == 0:
            return self.pop_front()
        elif index == self.size - 1:
            return self.pop_back()
        elif index < 0 or index >= self.size:
            print('wrong index')

        else:
            tmp_node = self.head
            for i in range(index - 1):
                tmp_node = tmp_node.next
                remote_node = tmp_node.next
            value = remote_node.data
            tmp_node.next_ = remote_node.next
            self.size -= 1
            return value
```

<!-- #region jp-MarkdownHeadingCollapsed=true -->
<h2>Реверс списка (переворачивание списка задом на перед)</h2>
<!-- #endregion -->

```python
    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev
```

---


<h2>2. Реализовать приложение, для работы со списком, которое реализует следующий набор действий:

а) инициализация пустого линейного однонаправленного списка;

б) организация диалогового цикла с пользователем;</h2>


<code>my_list = LinkedList()<code>

```python
while True:
    print("Выберите действие:")
    print("1. Добавить элемент")
    print("2. Вывести список")
    print("3. Выйти")
    print("4. Перевернуть список")
    print("5. Удалить элемент с конца")
    print("6. Удалить элемент с начала")
    print("7. Удалить элемент по индексу")
    print("8. Найти количество максимального элементов списка действительных чисел")
    print("9. Продублировать все простые числа")

    choice = input("Введите номер действия: ")

    if choice == '1':
        data = int(input("Введите элемент для добавления: "))
        my_list.push_back(data)
        print("Элемент добавлен в список.")
    elif choice == '2':
        print("Содержимое списка:")
        my_list.printLL()
    elif choice == '3':
        print("Выход из программы.")
        break
    elif choice == '4':
        print("Перевернутый список:")
        my_list.reverse()
        my_list.printLL()
    elif choice == '5':
        my_list.pop_back()
    elif choice == '6':
        my_list.pop_front()
    elif choice == '7':
        index = int(input("Введите индекс: "))
        my_list.pop(index)
    elif choice == '8':
        print(" Количество максимальных элементов = ", my_list.count_max_elements())
    elif choice == '9':
        my_list.duplicate_primes()
        my_list.printLL()

    else:
        print("Неверный выбор. Попробуйте еще раз.")
```

<!-- #region jp-MarkdownHeadingCollapsed=true -->
<h2>3 Реализовать индивидуальное задание</h2>
<!-- #endregion -->

---


<ul>
 <li>Найти количество максимальных элементов списка действительных чисел.</li> 
 <li>Дан список целых чисел. Продублировать в нем все простые числа.</li>
</ul>


```python
    def count_max_elements(self):
        if not self.head:
            return 0

        current = self.head
        max_value = current.data
        count = 1

        while current.next:
            current = current.next
            if current.data == max_value:
                count += 1
            elif current.data > max_value:
                max_value = current.data
                count = 1  # Начинаем считать снова, если найден более большой элемент

        return count


```

```python
    def is_prime(self, num: int):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def duplicate_primes(self):
        current = self.head
        while current:
            if self.is_prime(current.data):
                new_node = Node(current.data)
                new_node.next = current.next
                current.next = new_node
                current = current.next.next
            else:
                current = current.next
```

---


<!-- #region jp-MarkdownHeadingCollapsed=true -->
<h2>Ответы на контрольные вопросы</h2>

<!-- #endregion -->

<h4>1.Динамическая структура данных - это структура данных, которая позволяет изменять свой размер в процессе выполнения программы.</h4></li>
</ol>


<h4>2. Список - это упорядоченная коллекция элементов, которая может быть изменена.</h4>



<h4>3. Наиболее распространенные виды списков:
   - Однонаправленный список (Singly Linked List)
   - Двунаправленный список (Doubly Linked List)
   - Кольцевой список (Circular Linked List)
   - Список на массиве (Array-based List)</h4>


<h4>4. Основные операции над списком:
   - Добавление элемента (в начало, в конец, по индексу)
   - Удаление элемента (из начала, из конца, по индексу)
   - Поиск элемента (по значению, по индексу)</h4>


<h4>5. Операция вставки первого элемента выполняется за константное время O(1), так как просто меняется ссылка на новый элемент.
   Операция вставки не первого элемента требует поиска места вставки и изменения ссылок на предыдущий и следующий элементы,
   поэтому время выполнения зависит от размера списка и обычно составляет O(n), где n - количество элементов в списке.</h4>


<h4>6. Операция удаления первого элемента выполняется за константное время O(1), так как просто меняется ссылка на следующий элемент.
   Операция удаления не первого элемента также требует поиска места удаления и изменения ссылок на предыдущий и следующий элементы,
   поэтому время выполнения составляет O(n), где n - количество элементов в списке.</h4>

```python

```
