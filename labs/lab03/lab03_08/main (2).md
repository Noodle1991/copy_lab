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

## Линейные двунаправленные списки (Doubly linked list)

<!-- #region -->
### Цель работы

изучение структуры данных «линейные двунаправленные списки», а также основных операций над ними.

<!-- #endregion -->

### Задания на лабораторную работу


**1.** Реализовать программу, выполняющую стандартный набор операций с линейным двунаправленным списком:
 - вставка элемента в начало списка;
```
    def push_front(self, data):
        newnode = Node(data)
        if self.head is None:
            self.head = newnode
            self.tail = newnode
        else:
            newnode.next = self.head
            self.head.prev = newnode
            self.head = newnode
        self.length += 1
```
 - вставка элемента в середину списка перед указанным значением;
```angular2html
    def push_before(self, data, value):
        newnode = Node(data)
        current = self.head
        while current:
            if current.data == value:
                newnode.prev = current.prev
                newnode.next = current
                if current.prev:
                    current.prev.next = newnode
                else:
                    self.head = newnode
                current.prev = newnode
                self.length += 1
                return
            current = current.next
        print("Элемент не найден.")
```
 - вставка элемента в середину списка после указанного значения;
```angular2html
    def push_after(self, data, value):
        newnode = Node(data)
        current = self.head
        while current:
            if current.data == value:
                newnode.prev = current
                newnode.next = current.next
                if current.next:
                    current.next.prev = newnode
                else:
                    self.tail = newnode
                current.next = newnode
                self.length += 1
                return
            current = current.next
        print("Элемент не найден")
```
 - вставка элемента в конец списка;
```angular2html
    def push_back(self, data):
        newnode = Node(data)
        if self.tail is None:
            self.head = newnode
            self.tail = newnode
        else:
            newnode.prev = self.tail
            self.tail.next = newnode
            self.tail = newnode
        self.length += 1
```
 - удаление элемента в начале списка;
```angular2html
    def pop_front(self):
        if self.head is None:
            return None
        data = self.head.data
        self.head = self.head.next
        if self.head:
            self.head.prev = None
        else:
            self.tail = None
        self.length -= 1
        return data
```
 - Удаление элемента, стоящего перед указанным значением списка;
```angular2html
    def pop_before(self, value):
        current = self.head
        while current:
            if current.data == value:
                if current.prev:
                    data = current.prev.data
                    if current.prev.prev:
                        current.prev = current.prev.prev
                        current.prev.next = current
                    else:
                        self.head = current
                        current.prev = None
                    self.length -= 1
                    return data
                else:
                    print("Перед элементом искомого элемента нет")
                    return None
            current = current.next
        print("Элемент не найден.")
```
 - Удаление элемента, стоящего после указанного значением списка;
```angular2html
    def pop_after(self, value):
        current = self.head
        while current:
            if current.data == value:
                if current.next:
                    data = current.next.data
                    if current.next.next:
                        current.next = current.next.next
                        current.next.prev = current
                    else:
                        self.tail = current
                        current.next = None
                    self.length -= 1
                    return data
                else:
                    print("После элемента искомого элемента нет")
                    return None
            current = current.next
        print("Элемент не найден.")
```
 - удаление определенного элемента в списке;
```angular2html
    def delete(self, data):
        current = self.head
        while current:
            if current.data == data:
                if current == self.head:
                    self.head = current.next
                    if self.head:
                        self.head.prev = None
                    else:
                        self.tail = None
                elif current == self.tail:
                    self.tail = current.prev
                    self.tail.next = None
                else:
                    current.prev.next = current.next
                    current.next.prev = current.prev
                self.length -= 1
                return True
            current = current.next
        return False
```
 - удаление элемента в конце списка;
```angular2html
    def pop_back(self):
        if self.tail is None:
            return None
        data = self.tail.data
        self.tail = self.tail.prev
        if self.tail:
            self.tail.next = None
        else:
            self.head = None
        self.length -= 1
        return data
```
 - очистка списка;
```angular2html
    def clear(self):
        self.head = None
        self.tail = None
        self.length = 0
```
 - поиск элемента списка по его значяению;
```angular2html
    def at(self, value):
        current = self.head
        index = 0
        while current:
            if current.data == value:
                return index
            current = current.next
            index += 1
        return -1
```
 - реверс списка (переворачивание списка задом на перед).
```angular2html
    def reverse(self):
        if not self.head or not self.head.next:
            return
        current = self.head
        while current:
            temp = current.prev
            current.prev = current.next
            current.next = temp
            current = current.prev
        self.tail = self.head
        self.head = temp.prev
```

Требования:
 - список должен быть реализован в виде класса;
 - каждая операция должна быть реализована как метод класса;
 - добавлению/удалению должна предшествовать проверка возможности выполнения этих операций;



### Индивидуальные задания

**Задание 1.**
8. Пусть имеется список действительных чисел $a_1 → a_2 → \ldots  → a_n$. Сформировать новый список $b_1 → b_2 → \ldots → b_n$ такой же размерности по следующему правилу: элемент $b_k$ равен сумме элементов исходного списка с номерами от 1 до k.
```angular2html
    def sum_list(self):
        current = self.head
        total_sum = 0
        while current:
            total_sum += current.data
            current.data = total_sum
            current = current.next
```

**Задание 2.**

8. Вычислите среднее геометрическое элементов непустого списка.
```angular2html
def find_geometric_mean(head):
    product = 1
    count = 0
    current = self.head
    while current:
        product *= current.data
        count += 1
        current = current.next
    geometric_mean = product ** (1 / count)
    return geometric_mean
```

### Контрольные вопросы

1. Что такое динамическая структура данных?
Динамические структуры данных – это структуры данных, память под которые выделяется и освобождается программистом по мере необходимости. Динамические структуры данных в процессе существования в памяти могут изменять не только число составляю-щих их элементов, но и характер связей между элементами.
2. Что такое список? - Список — это упорядоченный набор элементов, каждый из которых имеет свой номер, или индекс, позволяющий быстро получить к нему доступ.
3. Какие виды списков существуют? - Списки бывают следующих видов:

Маркированный. Перед элементом списка идет маркер.
Нумерованный. Перед элементом списка идет номер.
Список определений. Перед определением идет термин.
Вложенный список.
Многоуровневый. Список состоит из нескольких уровней. может быть маркированным. нумерованным и комбинированным
4. Какие основные операции выполняются над списком? - Основными операциями над списками являются: · переход к очередному элементу списка; · добавление в список нового элемента; · поиск заданного элемента; · удаление элемента из списка. Выполнение этих операций основывается на использовании и изменении указателей. В отличие от очередей и стеков, элемент в список может быть добавлен в любое место.
5. Особенности выполнения операции вставки первого и не первого элемента в двунаправленный список. - Алгоритм вставки элемента: (после k-ого) первые k элементов остаются без изменений все элементы, начиная с k-ого сдвигаются на 1 позицию назад на место (k+1)-ого элемента записываем новый элемент. Массив из n элементов, в который вставляется k элементов необходимо определять как массив, имеющий размер n+k. Вставка перед элементом отличается только тем, что сдвигаются все элементы.
6. Особенности выполнения операции удаления первого и не первого элемента. - Если удаляется первый элемент в списке, то сначала переместить указатель начала списка на следующий элемент. Если в непустом списке удаляется не первый элемент (второй, третий и т.д., последний), то переместить указатель на позицию, следующую перед удаляемым элементом и сместить указатель предыдущего элемента в обход удаляемого элемента
<!-- #endregion -->
