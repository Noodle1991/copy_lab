<h1>Федотов Андрей Владимирович</h1>
<h1>Варинат 15</h1>

---

<h2>Цель работы</h2>

<ul>
    <li>Изучение структуры данных «Циклические однонаправленные списки», а также основных операций над ними.

</li>
</ul>

---

<h2>Общее задание</h2>

<h3>Определение вспомогательного класса <code>Node</code> и <code>CircularList</code></h3>


```python
class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None

    def __str__(self) -> str:
        return str(self.val)


class CircularList():
    def __init__(self, node=Node):
        self.head = None
```

<h3>Переопрелённые базовые методы для класса <code>CircularList</code></h3>


```python
def __len__(self) -> int:
        cur = self.head
        if self.head is None:
            return 0

        if self.head.next is None:
            return 1

        len = 1
        while cur.next != self.head:
            len += 1
            cur = cur.next
        return len
```

<h3>Вставка в начало линейного циклического списка</h3>


```python
def push_front(self, val):
    new_node = Node(val)
    if self.head is None:
        self.head = new_node
        return
    if len(self) == 1:
        new_node.next = self.head
        self.head.next = new_node
        self.head = new_node

    curr_node = self.head
    for i in range(len(self) - 1):
        curr_node = curr_node.next
    curr_node.next = new_node
    new_node.next = self.head
    self.head = new_node
```

<h3>Вставка перед указанным значением</h3>



```python
def insertBeforeValue(self, val, reach):
    new_node = Node(val)
    curr = self.head
    index = 0
    while curr.next.val != reach:
        curr = curr.next
        index += 1
        if index > len(self):
            raise RuntimeError(f"List doest have node with value {reach}")
    next_node = curr.next
    curr.next = new_node
    new_node.next = next_node
```

<h3>Вставка после указанного значения</h3>


```python
 def insertAfterValue(self, val, reach):
    new_node = Node(val)
    curr = self.head
    index = 0
    while curr.val != reach:
        curr = curr.next
        index += 1
        if index > len(self):
            raise RuntimeError(f"List doest have node with value {reach}")
    next_node = curr.next
    curr.next = new_node
    new_node.next = next_node
```

<h3>Вставка элемента в конец списка
</h3>


```python
def push_back(self, val):
    new_node = Node(val)
    if self.head is None:
        self.head = new_node
        return

    if len(self) == 1:
        self.head.next = new_node
        new_node.next = self.head
        return

    curr_node = self.head
    while curr_node.next != self.head:
        curr_node = curr_node.next
    curr_node.next = new_node
    new_node.next = self.head
```

<h3>Удаление первого элемента списка</h3>


```python
  def pop_front(self):
    if self.head is None:
        raise IndexError("Cannot pop_front empty list!")

    curr = self.head
    while curr.next != self.head:
        curr = curr.next
    self.head = self.head.next
    curr.next = self.head
```

<h3>Удаление элемента, стоящего перед указанным значением</h3>


```python
 def popBeforeValue(self, reach):
    curr = self.head
    index = 0
    while curr.next.next.val != reach:
        curr = curr.next
        index += 1
        if index > len(self):
            raise RuntimeError("List doest have node with value {reach}")
    curr.next = curr.next.next
```

<h3>Удаление элемента, стоящего после указанного значения</h3>


```python
def popAfterValue(self, reach):
    curr = self.head
    index = 0
    while curr.val != reach:
        curr = curr.next
        index += 1
        if index > len(self):
            raise RuntimeError("List doest have node with value {reach}")
    curr.next = curr.next.next
```

<h3>Удаление элемента списка по значению</h3>


```python
 def popValue(self, reach):
    curr = self.head
    index = 0
    while curr.next.val != reach:
        curr = curr.next
        index += 1
        if index > len(self):
            raise RuntimeError("List doest have node with value {reach}")
    curr.next = curr.next.next
```

<h3>Очистка списка</h3>


```python
 def clear(self):
    self.head = None
```

<h3>Поиск элемента списка по его значению</h3>


```python
def index(self, val):
    curr = self.head
    for i in range(len(self)):
        if curr.val == val:
            return i
        curr = curr.next
    raise RuntimeError(f"{val} is not in List")
```

<h2>Реверс списка</h2>


```python
def reverse(self):
    if self.head is None:
        raise RuntimeError()
    prev = None
    curr = self.head
    for i in range(len(self)):
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    self.head.next = prev
    self.head = prev
```

<h3>Приложение для работы со списком
</h3>

---


```python
lst = CircularList()
print("1 - Вставка в начало",
      "2 - Вставка в конец",
      "3 - Вставка до определённого значения",
      "4 - Вставка после определённого значения",
      "5 - Удаление по значению",
      "6 - Удаление до определённого значения",
      "7 - Удаление после определённого значения",
      "8 - Удаление певрого элемета",
      "9 - удаление последнего элемента",
      "10 - Реверс списка",
      "11 - Поиск индекса по значению",
      "12 - Задание 1",
      "13 - Задание 2",
      "14 - Очистка списка",
      "0 - Вывод списка в поток",
      sep='\n')
while True:
    command = int(input("Введите команду: "))
    match command:
        case 1:
            val = int(input("Введите значение: "))
            lst.push_front(val)
        case 2:
            val = int(input("Введите значение: "))
            lst.push_back(val)
        case 3:
            reach = int(input("Введите значение, до которого нужно вставить элемент: "))
            val = int(input("Введите значение: "))
            lst.insertBeforeValue(val, reach)
        case 4:
            reach = int(input("Введите значение, после которого которого нужно вставить элемент: "))
            val = int(input("Введите значение: "))
            lst.insertAfterValue(val, reach)
        case 5:
            reach = int(input("Введите значение, которое нужно удалить из списка: "))
            lst.popValue(reach)
        case 6:
            reach = int(input("Ввдите значение, до которого нужно удалить элменет"))
            lst.popBeforeValue(reach)
        case 7:
            reach = int(input("Введите значение, после которого нужно удалить элемент"))
            lst.popAfterValue(reach)
        case 8:
            lst.pop_front()
        case 9:
            lst.pop_back()
        case 10:
            lst.reverse()
        case 11:
            val = int(input("Введите значение: "))
            print(lst.index(val))
        case 12:
            print(f"Первоначальный лист:\n{lst}")
            print(f"Получившийся лист:\n{task1(lst)} ")
        case 13:
            odd, even = task2(lst)
            print(f"Cписок нечётных элементов {odd}")
            print(f"Cписок чётных элементов {even}")
        case 14:
            lst.clear()
        case 0:
            print(lst)
            sleep(2)
        case _:
            print("Несуществующая команда!")

```

<h2>Индивидуальное задание</h2>


---

<h3>Написать функцию, которая удаляет из списка элементы, входящие в него только один раз.</h3>


```python
def func1(lstt: CircularList):
    if lstt is None:
        raise Exception()
    val = {}
    cur = lstt.head
    for _ in range(len(lstt)):
        if cur.val in val.keys():
            val[cur.val] += 1
        else:
            val[cur.val] = 1
        cur = cur.next
    cur = lstt.head
    tmp = CircularList()
    for _ in range(len(lstt)):
        if val[cur.val] > 1:
            tmp.push_back(cur.val)
        cur = cur.next
    lstt.clear()
    cur = tmp.head
    for _ in range(len(tmp)):
        lstt.push_back(cur.val)
        cur = cur.next
```

<h3>Написать функцию, которая по двум линейным спискам L1 и L2 формирует новый список L, состоящий из попарных произведений элементов L1 и L2. Длина формируемого списка ограничивается длиной меньшего из списков L1, L2.</h3>


```python
def func2(lst1: CircularList, lst2: CircularList) -> CircularList:
    tmp = CircularList()
    cur_l1 = lst1.head
    cur_l2 = lst1.head
    for _ in range(min(len(lst1), len(lst2))):
        tmp.push_back(cur_l1.val * cur_l2.val)
        cur_l1 = cur_l1.next
        cur_l2 = cur_l2.next
    return tmp
```

---

<h2>Ответы на контрольные вопросы</h2>



1. **Динамическая структура данных** - это структура данных, которая позволяет изменять размер и форму во время выполнения программы. Она может выделять или освобождать память по мере необходимости, что позволяет эффективно управлять данными.

2. **Список** - это структура данных, представляющая собой упорядоченную последовательность элементов, каждый из которых содержит данные и ссылку на следующий элемент (или на предыдущий и следующий элементы в двусвязном списке). Списки позволяют хранить и манипулировать коллекциями данных.

3. Виды списков:
   - **Односвязный список**: каждый элемент содержит ссылку только на следующий элемент в списке.
   - **Двусвязный список**: каждый элемент содержит ссылки на предыдущий и следующий элементы в списке.
   - **Циклический список**: последний элемент списка ссылается на первый элемент, образуя замкнутую петлю.

4. Основные операции над списком:
   - **Вставка**: добавление элемента в список в указанном месте.
   - **Удаление**: удаление элемента из списка.
   - **Поиск**: нахождение элемента в списке по значению или индексу.
   - **Обход**: перебор всех элементов списка для выполнения определенных действий.

5. **Циклический список** - это специальный вид связанного списка, в котором последний элемент списка ссылается на первый элемент, образуя замкнутый цикл. Это означает, что обход списка можно начать с любого его элемента и продолжать доходить до исходного элемента.

6. Классификация циклических списков:
   - **Простой циклический список**: последний элемент ссылается только на первый элемент.
   - **Двусвязный циклический список**: каждый элемент ссылается и на предыдущий, и на следующий элемент. Последний элемент ссылается на первый, и первый - на последний элемент.

7. Основные операции над циклическим списком:
   - **Вставка**: добавление элемента в список.
   - **Удаление**: удаление элемента из списка.
   - **Поиск**: нахождение элемента в списке.
   - **Обход**: перебор всех элементов списка до исходного элемента.
