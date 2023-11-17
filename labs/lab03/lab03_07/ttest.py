class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def push_front(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.head.prev = None
            self.tail.next = None

        else:
            self.head.prev = new_node
            new_node.next = self.head
            new_node.prev = None
            self.head = new_node
        self.length += 1
        return data

    def push_back(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.head.prev = None
            self.tail.next = None
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
            self.tail.next = None
        self.length += 1
        return data

    def push(self, index, data):
        index = int(index)
        if index < 0:
            index += self.length
        if index < 0 or index > self.length:
            raise IndexError("Index out of range")
        elif index == 0:
            return self.push_front(data)
        elif index == self.length:
            return self.push_back(data)
        else:
            new_node = Node(data)
            current = self.head
            for _ in range(index - 1):
                current = current.next
            new_node.next = current.next
            new_node.prev = current
            current.next.prev = new_node
            current.next = new_node
            self.length += 1
            return data

    def push_before(self, value, data):
        if self.head == None:
            return "error"
        index = self.find_value(value)
        if index == "Node is not present in the list":
            return "Node is not present in the list"
        item = self.push(str(index), data)
        return item

    def push_after(self, value, data):
        if self.head == None:
            return "error"
        index = self.find_value(value)
        if index == "Node is not present in the list":
            return "Node is not present in the list"
        item = self.push(str(index + 1), data)
        return item

    def pop_front(self):
        if self.head is None:
            return "Insufficient data"
        old_head = self.head
        data = old_head.data
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = old_head.next
            self.head.prev = None
        old_head = None
        self.length -= 1
        return data

    def pop_back(self):
        if self.head is None:
            return "Insufficient data"
        data = self.tail.data
        old_head = self.tail
        if self.length == 1:
            self.tail = None
            self.head = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        old_head = None
        self.length -= 1
        return data

    def pop(self, index):
        index = int(index)
        if index < 0:
            index += self.length
        if index < 0 or index >= self.length:
            return "Index out of range"
        elif index == 0:
            return self.pop_front()
        elif index == self.length - 1:
            return self.pop_back()
        else:
            node = self.head
            for _ in range(index - 1):
                node = node.next
            new_node = node.next
            node.next = new_node.next
            new_node.next.prev = node
            data = new_node.data
            new_node = None
            self.length -= 1
            return data

    def pop_before(self, value):
        if self.head == None:
            return "error"
        index = self.find_value(value)
        if index == "Node is not present in the list":
            return "Node is not present in the list"
        elif index == self.length:
            return "last"
        return self.pop(str(index - 1))

    def pop_after(self, value):
        if self.head == None:
            return "error"
        index = self.find_value(value)
        if index == "Node is not present in the list":
            return "Node is not present in the list"
        elif index == self.length - 1:
            return "last"
        return self.pop(str(index + 1))

    def pop_value(self, value):
        if self.head == None:
            return "error"
        index = self.find_value(value)
        if index == "Node is not present in the list":
            return "Node is not present in the list"
        index = int(index)
        if index < 0:
            index += self.length
        if index < 0 or index >= self.length:
            return "Index out of range"
        elif index == 0:
            return self.pop_front()
        elif index == self.length - 1:
            return self.pop_back()
        else:
            node = self.head
            for _ in range(index - 1):
                node = node.next
            new_node = node.next
            node.next = new_node.next
            new_node.next.prev = node
            data = new_node.data
            new_node = None
            self.length -= 1
            return data

    def find_index(self, index):
        if index < 0:
            index += self.length
        if index < 0 or index > self.length:
            return "Index out of range"
        current = self.head
        for _ in range(index - 1):
            current = current.next
        return current.data

    def find_value(self, value):
        index = 0
        flag = False
        current = self.head
        if self.head is None:
            print("List is empty")
            return
        while current is not None:
            if current.data == value:
                flag = True
                break
            current = current.next
            index += 1
        if flag:
            return index
        else:
            return "Node is not present in the list"

    def reverse(self):
        current = self.head
        new_node = None
        while current is not None:
            new_node = current.prev
            current.prev = current.next
            current.next = new_node
            current = current.prev
        if new_node is not None:
            self.head = new_node.prev

    def print(self):

        current = self.head
        while current:
            prev_data = current.prev.data if current.prev else None
            next_data = current.next.data if current.next else None
            print("Current node =", current.data, ", Prev node =", prev_data, ", Next node =", next_data)
            current = current.next

    def clear(self):
        current = self.head
        while current is not None:
            new_node = current
            current = current.next
        self.head = None
        self.length = 0

    def remove_duplicates(self):
        current = self.head
        unique_elements = set()
        while current:
            if current.data not in unique_elements:
                unique_elements.add(current.data)
                current = current.next
            else:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next
                if current.next:
                    current.next.prev = current.prev
                temp = current
                current = current.next
                temp = None
                self.length -= 1


#
# l1 = LinkedList()
# l1.print()
#

def print_menu():
    print("1. Добавить элемент в начало")
    print("21. Добавить элемент в начало второго списка")

    print("2. Добавить элемент в конец")
    print("3. Добавить элемент по индексу")
    print("4. Добавить элемент перед заданным значением")
    print("5. Добавить элемент после заданного значения")
    print("6. Удалить элемент из начала")
    print("7. Удалить элемент из конца")
    print("8. Удалить элемент по индексу")
    print("9. Удалить элемент перед заданным значением")
    print("10. Удалить элемент после заданного значения")
    print("11. Удалить элемент по значению")
    print("12. Вывести элемент по индексу")
    print("13. Вывести индекс по значению")
    print("14. Вывести список")
    print("24. Вывести список второго списка")

    print("15. Удалить дубликаты")
    print("16. Объединить два упорядоченных списка")
    print("17. Очистить список")
    print("18. Выйти")


l1 = LinkedList()
l2 = LinkedList()

while True:
    print("\nОпции:")
    print_menu()
    choice = input("Выберите опцию (1-18): ")
    if choice == "1":
        data = input("Введите элемент для добавления в начало: ")
        l1.push_front(data)
    elif choice == "2":
        data = input("Введите элемент для добавления в конец: ")
        l1.push_back(data)
    elif choice == "3":
        index = input("Введите индекс для добавления элемента: ")
        data = input("Введите элемент для добавления по индексу: ")
        l1.push(index, data)
    elif choice == "4":
        value = input("Введите значение перед которым нужно добавить элемент: ")
        data = input("Введите элемент для добавления: ")
        l1.push_before(value, data)
    elif choice == "5":
        value = input("Введите значение после которого нужно добавить элемент: ")
        data = input("Введите элемент для добавления: ")
        l1.push_after(value, data)
    elif choice == "6":
        l1.pop_front()
    elif choice == "7":
        l1.pop_back()
    elif choice == "8":
        index = input("Введите индекс для удаления элемента: ")
        l1.pop(index)
    elif choice == "9":
        value = input("Введите значение перед которым нужно удалить элемент: ")
        l1.pop_before(value)
    elif choice == "10":
        value = input("Введите значение после которого нужно удалить элемент: ")
        l1.pop_after(value)
    elif choice == "11":
        value = input("Введите значение для удаления: ")
        l1.pop_value(value)
    elif choice == "12":
        index = input("Введите индекс для получения элемента: ")
        # print("Элемент по индексу:", l1.find_index(index))
    elif choice == "13":
        value = input("Введите значение для поиска индекса: ")
        print("Индекс элемента:", l1.find_value(value))
    elif choice == "14":
        l1.print()

    elif choice == "15":
        l1.remove_duplicates()
    elif choice == "16":
        if not l2.head:
            print("Второй список пуст. Добавьте элементы во второй список.")
        else:
            list1_values = []
            current1 = l1.head
            while current1:
                value = current1.data
                try:
                    value = int(value)  # Попытка преобразования в число
                except ValueError:
                    pass
                list1_values.append(value)
                current1 = current1.next

            list2_values = []
            current2 = l2.head
            while current2:
                value = current2.data
                try:
                    value = int(value)  # Попытка преобразования в число
                except ValueError:
                    pass
                list2_values.append(value)
                current2 = current2.next

            if all(isinstance(item, int) for item in list1_values) and all(
                    isinstance(item, int) for item in list2_values):
                sorted_list = sorted(list1_values + list2_values)
                merged_list = LinkedList()
                for item in sorted_list:
                    merged_list.push_back(item)
                print("Новый упорядоченный список из элементов первого и второго списка:")
                merged_list.print()
            else:
                print("Один из списков содержит элементы, которые не являются числами.")
    elif choice == "17":
        l1.clear()
        print("Список очищен")
    elif choice == "18":
        break
    elif choice == "21":
        data = input("Введите элемент для добавления в начало второго списка: ")
        l2.push_front(data)
    elif choice == "24":
        l2.print()
    else:
        print("Некорректный выбор. Пожалуйста, выберите снова.")

# Взаимодействие с пользователем
