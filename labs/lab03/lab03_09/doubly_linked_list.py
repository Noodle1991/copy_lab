class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def push_front(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1

    def insert_before(self, data, value):
        new_node = Node(data)
        current = self.head
        while current:
            if current.data == value:
                new_node.prev = current.prev
                new_node.next = current
                if current.prev:
                    current.prev.next = new_node
                else:
                    self.head = new_node
                current.prev = new_node
                self.length += 1
                return
            current = current.next
        print(f"Элемент с значением {value} не найден в списке.")

    def insert_after(self, data, value):
        new_node = Node(data)
        current = self.head
        while current:
            if current.data == value:
                new_node.prev = current
                new_node.next = current.next
                if current.next:
                    current.next.prev = new_node
                else:
                    self.tail = new_node
                current.next = new_node
                self.length += 1
                return
            current = current.next
        print(f"Элемент с значением {value} не найден в списке.")

    def push_back(self, data):
        new_node = Node(data)
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

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

    def remove_before(self, value):
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
                    print(f"Нет элемента перед элементом со значением {value}.")
                    return None
            current = current.next
        print(f"Элемент с значением {value} не найден в списке.")

    def remove_after(self, value):
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
                    print(f"Нет элемента после элемента со значением {value}.")
                    return None
            current = current.next
        print(f"Элемент с значением {value} не найден в списке.")

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

    def clear(self):
        self.head = None
        self.tail = None
        self.length = 0

    def find(self, value):
        current = self.head
        index = 0
        while current:
            if current.data == value:
                return index
            current = current.next
            index += 1
        return -1

    def reverse(self):
        current = self.head
        while current:
            current.prev, current.next = current.next, current.prev
            current = current.prev
        self.head, self.tail = self.tail, self.head

    def display(self):
        current = self.head
        while current:
            print(current.data, end=' <-> ')
            current = current.next
        print("None")

    def duplicate_chet_numbers(self):
        current = self.head
        while current:
            if current.data % 2 == 0:
                new_node = Node(current.data)
                new_node.next = current.next
                new_node.prev = current
                if current.next:
                    current.next.prev = new_node
                current.next = new_node
                self.length += 1
                current = new_node.next
            else:
                current = current.next

    def add_sum_after_every_third(self):
        current = self.head
        index = 1
        while current:
            if index % 3 == 0:
                if current.next:
                    sum = current.data + current.prev.data + current.prev.prev.data
                    new_node = Node(sum)
                    new_node.prev = current
                    new_node.next = current.next
                    current.next.prev = new_node
                    current.next = new_node
                    self.length += 1
                    current = new_node.next
                else:
                    break
            else:
                current = current.next
            index += 1


def main():
    lists = []
    current_list = None

    while True:
        print("\nВыберите операцию:")
        print("1. Создать новый список")
        print("2. Выбрать существующий список")
        print("3. Добавить элемент в начало")
        print("4. Добавить элемент в конец")
        print("5. Удалить элемент с начала")
        print("6. Удалить элемент с конца")
        print("7. Реверс списка")
        print("8. Найти элемент")
        print("9. Вывести список")
        print("10. Дублировать четные числа")
        print("11. Добавить сумму после каждого третьего элемента")
        print("12. Удалить элемент перед указанным значением")
        print("13. Удалить элемент после указанного значения")
        print("14. Вставить элемент перед указанным значением")
        print("15. Вставить элемент после указанного значения")
        print("16. Очистить текущий список")
        print("0. Выход")

        choice = input("Введите ваш выбор: ")

        if choice == '1':
            new_list = DoublyList()
            lists.append(new_list)
            current_list = new_list
            print("Создан новый список.")
        elif choice == '2':
            if len(lists) > 0:
                print("Выберите список (0 -", len(lists) - 1, "):")
                for i, l in enumerate(lists):
                    print(i, "-", "Длина:", l.length)
                list_choice = int(input())
                if 0 <= list_choice < len(lists):
                    current_list = lists[list_choice]
                    print("Выбран список с длиной", current_list.length)
                else:
                    print("Неверный выбор списка.")
            else:
                print("Нет созданных списков.")
        elif choice == '3':
            data = int(input("Введите данные: "))
            current_list.push_front(data)
        elif choice == '4':
            data = int(input("Введите данные: "))
            current_list.push_back(data)
        elif choice == '5':
            data = current_list.pop_front()
            print(f"Удаленный элемент: {data}")
        elif choice == '6':
            data = current_list.pop_back()
            print(f"Удаленный элемент: {data}")
        elif choice == '7':
            current_list.reverse()
            print("Список перевернут.")
        elif choice == '8':
            value = int(input("Введите значение для поиска: "))
            index = current_list.find(value)
            if index != -1:
                print(f"Значение {value} найдено по индексу {index}.")
            else:
                print(f"Значение {value} не найдено.")
        elif choice == '9':
            current_list.display()
        elif choice == '10':
            current_list.duplicate_chet_numbers()
            print("Четные числа дублированы.")
        elif choice == '11':
            current_list.add_sum_after_every_third()
            print("Сумма добавлена после каждого третьего элемента.")
        elif choice == '12':
            value = int(input("Введите значение перед которым нужно удалить элемент: "))
            current_list.remove_before(value)
        elif choice == '13':
            value = int(input("Введите значение после которого нужно удалить элемент: "))
            current_list.remove_after(value)
        elif choice == '14':
            value = int(input("Введите значение перед которым нужно вставить элемент: "))
            data = int(input("Введите данные для вставки: "))
            current_list.insert_before(data, value)
        elif choice == '15':
            value = int(input("Введите значение после которого нужно вставить элемент: "))
            data = int(input("Введите данные для вставки: "))
            current_list.insert_after(data, value)
        elif choice == '16':
            current_list.clear()
            print("Список очищен.")
        elif choice == '0':
            break
        else:
            print("Неверный выбор. Пожалуйста, выберите допустимую операцию.")

if __name__ == "__main__":
    main()
