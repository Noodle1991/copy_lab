class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


def is_valid_number(value):
    try:
        float(value)
        return True
    except ValueError:
        return False


class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def push_front(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.length += 1

    def pop_front(self):
        if not self.head:
            raise IndexError("List is empty")
        data = self.head.value
        self.head = self.head.next
        self.length -= 1
        return data

    def push_back(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self.length += 1

    def pop_back(self):
        if not self.head:
            raise IndexError("List is empty")
        if not self.head.next:
            data = self.head.value
            self.head = None
            self.length -= 1
            return data
        current = self.head
        while current.next.next:
            current = current.next
        data = current.next.value
        current.next = None
        self.length -= 1
        return data

    def at(self, index):
        if index < 0:
            index += self.length
        if index < 0 or index >= self.length:
            raise IndexError("Index out of range")
        current = self.head
        for _ in range(index):
            current = current.next
        return current.value

    def push(self, data, index):
        if index == 0:
            self.push_front(data)
        elif index == self.length:
            self.push_back(data)
        elif 0 < index < self.length:
            new_node = Node(data)
            current = self.head
            for _ in range(index - 1):
                current = current.next
            new_node.next = current.next
            current.next = new_node
            self.length += 1
        else:
            raise IndexError("Index out of range")

    def pop(self, index):
        if index == 0:
            return self.pop_front()
        elif index == self.length - 1:
            return self.pop_back()
        elif 0 < index < self.length - 1:
            current = self.head
            for _ in range(index - 1):
                current = current.next
            data = current.next.value
            current.next = current.next.next
            self.length -= 1
            return data
        else:
            raise IndexError("Index out of range")

    def clear(self):
        while self.head:
            temp = self.head
            self.head = self.head.next
            del temp
        self.length = 0

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
        current = self.head
        print("Список:")
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("Пусто")

    def __iter__(self):
        current = self.head
        while current:
            yield current.value
            current = current.next

    def validate_list(self):
        current = self.head
        while current:
            if not is_valid_number(current.value):
                return False
            current = current.next
        return True

    def count_unique_elements(self):
        if not self.validate_list():
            print("Проверьте список. Не все элементы являются действительными числами.")
            return 0

        unique_count = 0
        current = self.head
        prev_value = None

        while current:
            if current.value != prev_value:
                unique_count += 1
                prev_value = current.value
            current = current.next

        return unique_count

    def remove_every_third(self):
        current = self.head
        count = 0
        prev = None

        while current:
            count += 1
            if count % 3 == 0:
                prev.next = current.next
                del current
                current = prev.next
            else:
                prev = current
                current = current.next

def main():
    linked_list = LinkedList()

    while True:
        print("\nМеню:")
        print("1. Инициализировать пустой список")
        print("2. Вставить в начало")
        print("3. Вставить в конец")
        print("4. Вставить на определенную позицию")
        print("5. Удалить из начала")
        print("6. Удалить из конца")
        print("7. Удалить из определенной позиции")
        print("8. Перевернуть список")
        print("9. Показать список")
        print("10 Определить количество различных элементов списка действительных чисел")
        print("11 Удалить из него каждый третий элемент")
        print("12 Выйти")
        choice = input("Введите ваш выбор: ")

        if choice == "1":
            linked_list = LinkedList()
            print("Список инициализирован как пустой.")
        elif choice == "2":
            data = input("Введите данные для вставки в начало: ")
            linked_list.push_front(data)
        elif choice == "3":
            data = input("Введите данные для вставки в конец: ")
            linked_list.push_back(data)
        elif choice == "4":
            data = input("Введите данные для вставки: ")
            index = int(input("Введите позицию для вставки: "))
            try:
                linked_list.push(data, index)
            except IndexError as e:
                print(e)
        elif choice == "5":
            try:
                linked_list.pop_front()
            except IndexError as e:
                print(e)
        elif choice == "6":
            try:
                linked_list.pop_back()
            except IndexError as e:
                print(e)
        elif choice == "7":
            index = int(input("Введите позицию для удаления: "))
            try:
                linked_list.pop(index)
            except IndexError as e:
                print(e)
        elif choice == "8":
            linked_list.reverse()
            print("Список перевернут.")
        elif choice == "9":
            linked_list.display()
        elif choice == "12":
            break
        elif choice == '10':
            if linked_list.validate_list():
                unique_count = linked_list.count_unique_elements()
                print(f"Количество различных элементов в списке: {unique_count}")
            else:
                print("Проверьте список. Не все элементы являются действительными числами.")

        elif choice == "11":
            linked_list.remove_every_third()
            print("Каждый третий элемент удален из списка.")

        else:
            print("Неверный выбор. Пожалуйста, попробуйте еще раз.")


if __name__ == "__main__":
    main()

