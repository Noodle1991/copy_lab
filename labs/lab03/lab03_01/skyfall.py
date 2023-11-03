class Node:

    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.next: Node = next
        self.prev: Node = prev


    def getData(self):
        return self.data

    def setData(self, data):
        self.data = data

    def getNextNode(self):
        return self.next

    def setNextNode(self, node):
        self.next = node

    def getPrevNode(self):
        return self.prev

    def setPrevNode(self, node):
        self.prev = node


class LinkedList:
    def __init__(self):
        self.head: Node = None
        self.tail: Node = None
        self.size = 0

    def is_empty(self):
        return self.head is None

    def push_front(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            self.size += 1

    def insert_before_value(self, value, data):
        new_node = Node(data)
        if self.is_empty():
            print("Список пуст")
            return
        current = self.head
        while current:
            if current.data == value:
                if current == self.head:
                    self.head.prev = new_node
                    new_node.next = self.head
                    self.head = new_node
                else:
                    new_node.prev = current.prev
                    new_node.next = current
                    current.prev.next = new_node
                    current.prev = new_node
                return
            current = current.next
            self.size += 1
        print("Значение", value, "не найдено")

    def push_after_value(self, value, data):
        new_node = Node(data)
        if self.is_empty():
            print("Список пуст")
            return
        current = self.head
        while current:
            if current.data == value:
                if current == self.tail:
                    new_node.prev = self.tail
                    self.tail.next = new_node
                    self.tail = new_node
                else:
                    new_node.prev = current
                    new_node.next = current.next
                    current.next.prev = new_node
                    current.next = new_node
                return
            current = current.next
            self.size += 1
        print("Значение", value, "не найдено")

    def Push_back(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

    def Pop_front(self):
        if self.is_empty():
            print("Список пуст")
            return
        if self.head.next is None:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None

    def Pop_before_value(self, value):
        if self.is_empty() or self.head.data == value or self.head.next.data == value:
            print("Недостаточно элементов в списке для удаления")
            return
        current = self.head.next
        while current.next:
            if current.data == value:
                current.prev.prev.next = current
                current.prev = current.prev.prev
                return
            current = current.next
            self.size -= 1
        print("Значение", value, "не найдено")

    def Pop_after_value(self, value):
        if self.is_empty() or self.tail.data == value or self.tail.prev.data == value:
            print("Недостаточно элементов в списке для удаления")
            return
        current = self.head
        while current.next:
            if current.data == value:
                current.next.next.prev = current
                current.next = current.next.next
                return
            current = current.next
            self.size -= 1
        print("Значение", value, "не найдено")

    def delete_exact(self, value):
        if self.is_empty():
            print("Список пуст")
            return
        current = self.head
        while current:
            if current.data == value:
                if current == self.head:
                    self.delete_at_beginning()
                elif current == self.tail:
                    self.delete_at_end()
                else:
                    current.prev.next = current.next
                    current.next.prev = current.prev
                return
            current = current.next
            self.size -= 1
        print("Значение", value, "не найдено")

    def Pop_back(self):
        if self.is_empty():
            print("Список пуст")
            return
        if self.tail.prev is None:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            self.size -= 1

    def clear(self):
        self.head = None
        self.tail = None

    def find(self, value):
        if self.is_empty():
            print("Список пуст")
            return None
        current = self.head
        while current:
            if current.data == value:
                return current
            current = current.next
        print("Значение", value, "не найдено")
        return None

    def reverse(self):
        if self.is_empty():
            print("Список пуст")
            return
        current = self.head
        while current:
            current.prev, current.next = current.next, current.prev
            current = current.prev
        self.head, self.tail = self.tail, self.head

    # индивидуальное задание

    def remove_duplicates(self):
        current = self.head
        while current:
            exact = current.next
            while exact and current.data == exact.data:
                if exact.next:
                    exact.next.prev = current
                current.next = exact.next
                exact = exact.next
                self.size -= 1
            current = current.next

    def average(self):
        if self.is_empty():
            return None
        else:
            current = self.head
            count = 0
            total_sum = 0
            while current:
                count += 1
                total_sum += current.data
                current = current.next
            average = total_sum / count
            return average



my_list = LinkedList()

print("Выберите действие:")
print("1. Добавить элемент")
print("2. Вывести список")
print("3. Перевернуть список")
print("4. Удалить элемент с конца")
print("5. Удалить элемент с начала")
print("6. Удалить элемент после значения")
print(
    "7. Удалить дубликаты.")
print("8. Вычислите среднее арифметическое элементов непустого списка")
print("9. Выйти.")
while True:
    choice = input("Введите номер действия: ")

    if choice == '1':
        data = int(input("Введите элемент для добавления: "))
        my_list.Push_back(data)
        print("Элемент добавлен в список.")
    elif choice == '2':
        print("Содержимое списка:")
        my_list.print_list()
    elif choice == '3':
        print("Перевернутый список:")
        my_list.reverse()
        my_list.print_list()
    elif choice == '4':
        my_list.Pop_back()
    elif choice == '5':
        my_list.Pop_front()
    elif choice == '6':
        index = int(input("Введите индекс: "))
        my_list.Pop_after_value(index)
    elif choice == '7':

        my_list.remove_duplicates()
        my_list.print_list()
    elif choice == '8':
        my_list.average()
        print(my_list.average())
    elif choice == '9':
        break

