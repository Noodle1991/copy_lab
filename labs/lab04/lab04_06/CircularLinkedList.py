class CircularLinkedListException(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        if self.message:
            return f'CircularLinkedListException: {self.message}'
        else:
            return 'CircularLinkedListException has been raised'


class Node:
    def __init__(self, data=None, next_node=None):
        self.data_ = data
        self.next_: Node = next_node


class CircularLinkedList:
    def __init__(self):
        self.size_ = 0
        self.head_: Node = None

    def push_front(self, data):
        '''Добавление элемента в начало списка'''

        new_node = Node(data)
        if not self.size_:
            self.head_ = new_node
            new_node.next_ = self.head_
        else:
            new_node.next_ = self.head_
            self.head_ = new_node

            tmp_node = self.head_
            for _ in range(self.size_):
                tmp_node = tmp_node.next_
            tmp_node.next_ = self.head_
        self.size_ += 1

    def insert(self, data, index: int):
        '''Добавление элемента в середину списка по индексу'''

        if index == 0:
            self.push_front(data)
        elif index == self.size_:
            self.push_back(data)
        elif index < 0 or index > self.size_:
            raise CircularLinkedListException('wrong index')
        else:
            new_node = Node(data)
            tmp_node = self.head_
            for _ in range(index - 1):
                tmp_node = tmp_node.next_
            new_node.next_ = tmp_node.next_
            tmp_node.next_ = new_node
            self.size_ += 1

    def insert_after_index(self, data, index: int):
        '''Добавление элемента в середину списка после указанного индекса'''

        self.insert(data, index + 1)

    def push_back(self, data):
        '''Добавление элемента в конец списка'''

        if not self.size_:
            self.push_front(data)
        else:
            tmp_node = self.head_
            for _ in range(self.size_ - 1):
                tmp_node = tmp_node.next_
            tmp_node.next_ = Node(data, self.head_)
            self.size_ += 1

    def pop_front(self):
        '''Удаление элемента из начала списка'''

        if not self.size_:
            raise CircularLinkedListException('list is empty')
        else:
            self.head_ = self.head_.next_
            return self.pop_back()

    def pop(self, index: int):
        '''Удаление элемента из середины списка по индексу'''

        if index == 0:
            return self.pop_front()
        elif index == self.size_ - 1:
            return self.pop_back()
        elif index < 0 or index >= self.size_:
            raise CircularLinkedListException('wrong index')
        else:
            tmp_node = self.head_
            for i in range(index - 1):
                tmp_node = tmp_node.next_
            remote_node = tmp_node.next_
            value = remote_node.data_
            tmp_node.next_ = remote_node.next_
            self.size_ -= 1
            return value

    def pop_after_index(self, index: int):
        '''Удаление элемента из середины списка после указанного индекса'''

        return self.pop(index + 1)

    def remove(self, data):
        '''Удаление элемента по значению'''

        index = self.index(data)
        self.pop(index)

    def pop_back(self):
        '''Удаление элемента из конца списка'''

        if not self.size_:
            raise CircularLinkedListException('list is empty')
        else:
            tmp_node = self.head_
            while not (tmp_node.next_.next_ is self.head_):
                tmp_node = tmp_node.next_
            value = tmp_node.next_.data_
            tmp_node.next_ = self.head_
            self.size_ -= 1
            return value

    def clear(self):
        '''Очистка списка'''

        if self.size_:
            self.head_.next_ = None
            self.head_ = None
            self.size_ = 0

    def index(self, data):
        '''Поиск элемента списка по его значению'''

        if not self.size_:
            raise CircularLinkedListException('list is empty')
        else:
            tmp_node = self.head_
            for count in range(self.size_):
                if tmp_node.data_ == data:
                    return count
                else:
                    tmp_node = tmp_node.next_
            else:
                raise CircularLinkedListException(f'{data} is not in CircularLinkedList')

    def reverse(self):
        '''Реверс списка'''

        if self.size_:
            prev_node = self.head_
            for _ in range(self.size_ - 1):
                prev_node = prev_node.next_

            cur_node = self.head_
            next_node = self.head_
            for _ in range(self.size_):
                next_node = next_node.next_
                cur_node.next_ = prev_node
                prev_node = cur_node
                cur_node = next_node
            self.head_ = prev_node

    def __str__(self):
        text = '['
        if self.size_:
            tmp_node = self.head_
            text += str(tmp_node.data_)
            tmp_node = tmp_node.next_
            while not (tmp_node is self.head_):
                text += ', '
                text += str(tmp_node.data_)
                tmp_node = tmp_node.next_
        text += ']'
        return text

    def __getitem__(self, index):
        if index < 0:
            index += self.size_
        if index < 0 or index >= self.size_:
            raise CircularLinkedListException('wrong index')
        else:
            tmp_node = self.head_
            for i in range(index):
                tmp_node = tmp_node.next_
            return tmp_node.data_

    def prime_numbers(self):
        '''Функция, формирующая новый список, состоящий из элемнтов текущего списка, которые являются простыми числами'''

        new_lst = CircularLinkedList()
        for i in range(self.size_):
            num = self[i]
            count = 0
            for j in range(2, int(num // 2) + 1):
                if num % j == 0:
                    count += 1
            if not count:
                new_lst.push_back(num)
        return new_lst

    def subset(self):
        '''Функция, которая в линейном списке из каждой группы подряд идущих одинаковых элементов оставляет только один'''

        i = 0
        while i < self.size_:
            unique_data = self[i]
            j = i + 1
            if j < self.size_:
                while self[j] == unique_data:
                    self.pop(j)
                    if j >= self.size_:
                        break
            i += 1

        if self[-1] == self[0]:
            self.pop_back()


menu = '''
    Для взаимодействия со списком введите название команды.

    Доступные команды:
    * Вывести меню с командами: "menu"
    * Завершить программу: "exit"
    * Вывести список в чат: "print"
    * Добавить элемент в начало списка: "push_front"
    * Добавить элемент перед указанным индексом: "insert"
    * Добавить элемент после указанного индекса: "shift_insert"
    * Добавить элемент в конец списка: "push_back"
    * Удалить элемент из начала списка: "pop_front"
    * Удалить элемент перед указанным индексом: "pop"
    * Удалить элемент после указанного индекса: "shift_pop"
    * Удалить элемент списка по его значению: "remove"
    * Удалить элемент из конца списка: "pop_back"
    * Очистить список: "clear"
    * Вывести значение по индексу: "item"
    * Вывести индекс элемента по значению: "index"
    * Реверсировать список: "reverse"
    * Сформировать список состоящий только из простых чисел: "prime_numbers"
    * Оставить только один элемент из группы подряд идущих одинаковых элементов: "subset"
    '''

message = input('Для создания списка и начала работы пропишите "Create"\n>>')
if message.lower() == 'create':
    lst = CircularLinkedList()
    print(menu)

    run = True
    while run:
        command = input('Введите команду\n>>')
        correct_index = True
        match command:
            case 'menu':
                print(menu)

            case 'exit':
                stop = input('Вы точно хотите завершить работу программы? Y/N\n>>')
                if stop.lower() == 'y' or stop.lower() == 'yes':
                    run = False

            case 'print':
                print(lst)

            case 'push_front':
                value = input('Введите значение элемента\n>>')
                try:
                    value = float(value)
                except:
                    pass

                lst.push_front(value)
                print(f'Елемент {value} был добавлен в начало списка')

            case 'insert':
                index = input('Введите индекс\n>>')
                value = input('Введите значение элемента\n>>')
                try:
                    index = int(index)
                except:
                    correct_index = False

                if correct_index:
                    try:
                        value = float(value)
                    except:
                        pass
                    lst.insert(value, index)
                    print(f'Елемент {value} был добавлен на {index} позицию списка')

            case 'shift_insert':
                index = input('Введите индекс\n>>')
                value = input('Введите значение элемента\n>>')
                try:
                    index = int(index)
                except:
                    correct_index = False

                if correct_index:
                    try:
                        value = float(value)
                    except:
                        pass
                    lst.insert_after_index(value, index)
                    print(f'Елемент {value} был добавлен на {index + 1} позицию списка')

            case "push_back":
                value = input('Введите значение элемента\n>>')
                try:
                    value = float(value)
                except:
                    pass

                lst.push_back(value)
                print(f'Елемент {value} был добавлен в конец списка')

            case "pop_front":
                value = lst.pop_front()
                print(f'Елемент {value} был удален из начала списка')

            case "pop":
                index = input('Введите индекс\n>>')
                try:
                    index = int(index)
                except:
                    correct_index = False

                if correct_index:
                    value = lst.pop(index)
                    print(f'Елемент {value} был удален на {index} позиции списка')

            case "shift_pop":
                index = input('Введите индекс\n>>')
                try:
                    index = int(index)
                except:
                    correct_index = False

                if correct_index:
                    value = lst.pop_after_index(index)
                    print(f'Елемент {value} был удален на {index + 1} позиции списка')

            case "remove":
                value = input('Введите значение элемента\n>>')
                try:
                    value = float(value)
                except:
                    pass

                lst.remove(value)
                print(f'Елемент {value} был удален из списка')

            case "pop_back":
                value = lst.pop_back()
                print(f'Елемент {value} был удален из конца списка')

            case "clear":
                lst.clear()
                print('Список был очищен!')

            case "item":
                index = input('Введите индекс\n>>')
                try:
                    index = int(index)
                except:
                    correct_index = False

                if correct_index:
                    print(lst[index])

            case "index":
                value = input('Введите значение элемента\n>>')
                try:
                    value = float(value)
                except:
                    pass

                index = lst.index(value)
                print(f'Элемент {value} находится в списке под индексом {index}')

            case "reverse":
                lst.reverse()

            case "prime_numbers":
                lst2 = lst.prime_numbers()
                print('Сформированный список:')
                print(lst2)

            case "subset":
                lst.subset()

            case _:
                print(f'Не существует команды {command}! Попробуйте еще раз.')
                print(menu)

        if not correct_index:
            print('Вы указали некорректное значение индекса! Попробуйте еще раз.')
        print()
print('Завершение работы программы')
