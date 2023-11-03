from time import sleep


class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None

    def __str__(self) -> str:
        return str(self.val)


class CircularList():
    def __init__(self, node=Node):
        self.head = None

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

    def popValue(self, reach):
        curr = self.head
        index = 0
        while curr.next.val != reach:
            curr = curr.next
            index += 1
            if index > len(self):
                raise RuntimeError("List doest have node with value {reach}")
        curr.next = curr.next.next

    def popAfterValue(self, reach):
        curr = self.head
        index = 0
        while curr.val != reach:
            curr = curr.next
            index += 1
            if index > len(self):
                raise RuntimeError("List doest have node with value {reach}")
        curr.next = curr.next.next

    def popBeforeValue(self, reach):
        curr = self.head
        index = 0
        while curr.next.next.val != reach:
            curr = curr.next
            index += 1
            if index > len(self):
                raise RuntimeError("List doest have node with value {reach}")
        curr.next = curr.next.next

    def __str__(self) -> str:
        res = "-> "
        if self.head is None:
            return "Emty list"

        cur = self.head
        for i in range(len(self) - 1):
            res += str(cur.val) + " -> "
            cur = cur.next
        res += str(cur.val) + " ->"
        return res

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

    def pop_back(self):
        if self.head is None:
            raise IndexError("Cannot pop_back empty list!")
        curr = self.head
        while curr.next.next != self.head:
            curr = curr.next
        curr.next = curr.next.next

    def pop_front(self):
        if self.head is None:
            raise IndexError("Cannot pop_front empty list!")

        curr = self.head
        while curr.next != self.head:
            curr = curr.next
        self.head = self.head.next
        curr.next = self.head

    def clear(self):
        self.head = None

    def index(self, val):
        curr = self.head
        for i in range(len(self)):
            if curr.val == val:
                return i
            curr = curr.next
        raise RuntimeError(f"{val} is not in List")


def task1(list: CircularList) -> CircularList:
    if lst.head is None:
        raise TypeError("List is empty!")

    result = CircularList()
    for i in range(len(lst)):
        curr = lst.head
        sum = 0
        for j in range(i):
            sum += curr.val
            curr = curr.next
        result.push_back(sum)
    return result


def task2(list: CircularList) -> (CircularList, CircularList):
    odd = CircularList()
    even = CircularList()
    curr = list.head
    for i in range(len(list)):
        if curr.val % 2 == 0:
            even.push_back(curr.val)
        else:
            odd.push_back(curr.val)
        curr = curr.next
    return odd, even


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
