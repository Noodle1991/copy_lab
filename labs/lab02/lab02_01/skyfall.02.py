class Node:

    def __init__(self, data, next=None):
        self.data = data
        self.next = next
        self.size = 0

    # defining getter and setter for data and next
    def getData(self):
        return self.data

    def setData(self, data):
        self.data = data

    def getNextNode(self):
        return self.next

    def setNextNode(self, node):
        self.next = node


class LinkedList:

    def __init__(self, head=None):
        self.head = head
        self.size = 0

    def getSize(self):
        return self.size

    def addNode(self, data):
        node = Node(data, self.head)
        self.head = node
        self.size += 1

    # delete a node from linked list at value
    def removeNode(self, value):
        prev = None
        curr = self.head
        while curr:
            if curr.getData() == value:
                if prev:
                    prev.setNextNode(curr.getNextNode())
                else:
                    self.head = curr.getNextNode()
                return True

            prev = curr
            curr = curr.getNextNode()

        return False

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

    # find a node in the linked list
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

    # print the linked list
    def printLL(self):
        curr = self.head
        while curr:
            print(curr.data)
            curr = curr.getNextNode()

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

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    # 3 individual answer
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

    # 2

    def is_empty(self):
        return self.head is None


my_list = LinkedList()



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
