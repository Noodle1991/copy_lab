class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularSinglyList:
    def __init__(self):
        self.head = None
        self.length = 0

    def is_empty(self):
        return self.length == 0

    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.is_empty():
            new_node.next = new_node  # Устанавливаем указатель на самого себя
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head
        self.head = new_node
        self.length += 1

    def insert_after_value(self, data, value):
        if self.is_empty():
            print("Список пуст. Невозможно выполнить вставку.")
            return

        new_node = Node(data)
        temp = self.head
        while temp.next != self.head:
            if temp.data == value:
                new_node.next = temp.next
                temp.next = new_node
                self.length += 1
                return
            temp = temp.next

        if temp.data == value:
            new_node.next = temp.next
            temp.next = new_node
            self.length += 1
        else:
            print(f"Элемент со значением {value} не найден в списке.")

    def insert_before_value(self, data, value):
        if self.is_empty():
            print("Список пуст. Невозможно выполнить вставку.")
            return

        new_node = Node(data)
        temp = self.head
        prev = None
        while temp.next != self.head:
            if temp.data == value:
                new_node.next = temp
                if prev:
                    prev.next = new_node
                else:
                    last_node = self.head
                    while last_node.next != self.head:
                        last_node = last_node.next
                    self.head = new_node
                    last_node.next = self.head
                self.length += 1
                return
            prev = temp
            temp = temp.next

        if temp.data == value:
            new_node.next = temp
            if prev:
                prev.next = new_node
            else:
                last_node = self.head
                while last_node.next != self.head:
                    last_node = last_node.next
                self.head = new_node
                last_node.next = self.head
            self.length += 1
        else:
            print(f"Элемент со значением {value} не найден в списке.")

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.is_empty():
            new_node.next = new_node
            self.head = new_node
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head
        self.length += 1

    def delete_at_beginning(self):
        if self.is_empty():
            print("Список пуст. Невозможно выполнить удаление.")
            return

        if self.head.next == self.head:
            self.head = None
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = self.head.next
            self.head = self.head.next
        self.length -= 1

    def delete_before_value(self, value):
        if self.is_empty():
            print("Список пуст. Невозможно выполнить удаление.")
            return

        if self.head.data == value:
            print("Первый элемент не имеет предшественников для удаления.")
            return

        temp = self.head
        prev = None
        prev_to_prev = None
        while temp.next != self.head:
            if temp.data == value:
                if prev_to_prev:
                    prev_to_prev.next = prev
                else:
                    last_node = self.head
                    while last_node.next != self.head:
                        last_node = last_node.next
                    self.head = prev
                    last_node.next = self.head
                self.length -= 1
                return
            prev_to_prev = prev
            prev = temp
            temp = temp.next

        if temp.data == value:
            if prev_to_prev:
                prev_to_prev.next = prev
            else:
                last_node = self.head
                while last_node.next != self.head:
                    last_node = last_node.next
                self.head = prev
                last_node.next = self.head
            self.length -= 1
        else:
            print(f"Элемент со значением {value} не найден в списке.")

    def delete_after_value(self, value):
        if self.is_empty():
            print("Список пуст. Невозможно выполнить удаление.")
            return

        temp = self.head
        while temp.next != self.head:
            if temp.data == value:
                if temp.next == self.head:
                    print(f"Элемент со значением {value} является последним в списке.")
                    return
                temp.next = temp.next.next
                self.length -= 1
                return
            temp = temp.next

        if temp.data == value:
            if temp.next == self.head:
                print(f"Элемент со значением {value} является последним в списке.")
            else:
                temp.next = temp.next.next
            self.length -= 1
        else:
            print(f"Элемент со значением {value} не найден в списке.")

    def delete_element(self, value):
        if self.is_empty():
            print("Список пуст. Невозможно выполнить удаление.")
            return

        if self.head.data == value:
            self.delete_at_beginning()
            return

        temp = self.head
        prev = None
        while temp.next != self.head:
            if temp.data == value:
                prev.next = temp.next
                self.length -= 1
                return
            prev = temp
            temp = temp.next

        if temp.data == value:
            prev.next = temp.next
            self.length -= 1
        else:
            print(f"Элемент со значением {value} не найден в списке.")

    def delete_at_end(self):
        if self.is_empty():
            print("Список пуст. Невозможно выполнить удаление.")
            return

        if self.head.next == self.head:
            self.head = None
        else:
            temp = self.head
            while temp.next.next != self.head:
                temp = temp.next
            temp.next = self.head
        self.length -= 1

    def clear(self):
        self.head = None
        self.length = 0

    def search(self, value):
        index = 0
        flag = False
        current = self.head
        if self.head is None:
            print("Список пуст.")
            return
        while current.next != self.head:
            if str(current.data) == str(value):
                flag = True
                break
            current = current.next
            index += 1
        if flag:
            print(f"index = {index}")
            return
        else:
            return f"Элемент со значением {value} не найден в списке."

    def reverse(self):
        if self.is_empty():
            print("Список пуст. Невозможно выполнить реверс.")
            return

        prev = None
        current = self.head
        while True:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
            if current == self.head:
                break

        self.head = prev

    def display(self):
        if self.is_empty():
            print("Список пуст.")
            return

        temp = self.head
        while True:
            if temp is not None:
                print(temp.data, end=" -> ")
                temp = temp.next
                if temp == self.head:
                    print("...")
                    break
            else:
                break

    def duplicate_chet_numbers(self):
        if self.is_empty():
            print("Список пуст. Невозможно выполнить дублирование.")
            return

        temp = self.head
        count = 0
        l = self.length
        while count < l:  # Проходим не более, чем длина списка
            if temp.data % 2 == 0:
                new_node = Node(temp.data)
                new_node.next = temp.next
                temp.next = new_node
                self.length += 1
                temp = new_node.next
                count += 1
            else:
                temp = temp.next
                count += 1
            print(count, temp.data)


    def filter_and_sort_divisible_by_3(self):
        if self.is_empty():
            print("Список пуст. Невозможно выполнить фильтрацию и сортировку.")
            return

        divisible_by_3 = []
        temp = self.head
        while True:
            if temp.data % 3 == 0:
                divisible_by_3.append(temp.data)
            temp = temp.next
            if temp == self.head:
                break

        divisible_by_3.sort(reverse=True)

        L2 = CircularSinglyList()
        for num in divisible_by_3:
            L2.insert_at_end(num)

        return L2

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
        print("10. Фильтрация и сортировка (деление на 3)")
        print("11. Добавить элемент перед указанным значением")
        print("12. Добавить элемент после указанного значения")
        print("13. Удалить элемент перед указанным значением")
        print("14. Удалить элемент после указанного значения")
        print("15. Дублировать четные числа")
        print("16. Очистить текущий список")
        print("17. Удалить по значению")
        print("0. Выход")

        choice = input("Введите ваш выбор: ")

        if choice == '1':
            new_list = CircularSinglyList()
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
            current_list.insert_at_beginning(data)
        elif choice == '4':
            data = int(input("Введите данные: "))
            current_list.insert_at_end(data)
        elif choice == '5':
            current_list.delete_at_beginning()
        elif choice == '6':
            current_list.delete_at_end()
        elif choice == '7':
            current_list.reverse()
        elif choice == '8':
            value = int(input("Введите значение для поиска: "))
            current_list.search(value)
        elif choice == '9':
            current_list.display()
        elif choice == '10':
            lists.append(current_list.filter_and_sort_divisible_by_3())
        elif choice == '11':
            data = int(input("Введите данные: "))
            value = int(input("Введите значение, перед которым нужно вставить элемент: "))
            current_list.insert_before_value(data, value)
        elif choice == '12':
            data = int(input("Введите данные: "))
            value = int(input("Введите значение, после которого нужно вставить элемент: "))
            current_list.insert_after_value(data, value)
        elif choice == '13':
            value = int(input("Введите значение, перед которым нужно удалить элемент: "))
            current_list.delete_before_value(value)
        elif choice == '14':
            value = int(input("Введите значение, после которого нужно удалить элемент: "))
            current_list.delete_after_value(value)
        elif choice == '15':
            current_list.duplicate_chet_numbers()
            print("Четные числа дублированы.")
        elif choice == '16':
            current_list.clear()
            print("Список очищен.")
        elif choice == '17':
            value = int(input("Введите значение, которое нужно удалить элемент: "))
            current_list.delete_element(value)
        elif choice == '0':
            break
        else:
            print("Неверный выбор. Пожалуйста, выберите допустимую операцию.")

if __name__ == "__main__":
    main()
