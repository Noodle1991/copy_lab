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
        newnode = Node(data)
        if self.head is None:
            self.head = newnode
            self.tail = newnode
        else:
            newnode.next = self.head
            self.head.prev = newnode
            self.head = newnode
        self.length += 1

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


    def at(self, value):
        current = self.head
        index = 0
        while current:
            if current.data == value:
                return index
            current = current.next
            index += 1
        return -1

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

    def display(self):
        current = self.head
        while current:
            print(current.data, end=' <-> ')
            current = current.next
        print("None")
