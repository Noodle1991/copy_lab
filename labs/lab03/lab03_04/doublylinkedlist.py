class Node:

    def __init__(self, data):
        self.nextid = None
        self.previousid = None
        self.data = data


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def push_front(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.nextid = self.head
            self.head.previousid = new_node
            self.head = new_node

    def pop_front(self):
        if self.head is None:
            return
        else:
            self.head = self.head.nextid

    def push_back(self, data):
        new_node = Node(data)
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.previousid = self.tail
            self.tail.nextid = new_node
            self.tail = new_node

    def pop_back(self):
        if self.tail is None:
            return
        else:
            self.tail = self.tail.previousid

    def print_linkedlist(self): #iterating over a singly linked list
        copy_head = self.head
        while copy_head is not None:
            print(copy_head.data)
            copy_head = copy_head.nextid

    def clear_list(self):
        copy_head = self.head
        while self.head is not None:
            self.head = self.head.nextid

    def linkedlist_size(self):
        copy_head = self.head
        size = 0
        while copy_head is not None:
            size += 1
            copy_head = copy_head.nextid
        return size

    #поиск элемента, удаление+вставка перед и после индекса, удаление определенногоб поиск элемента по значению
    def reverse_list(self):
        copy_head = self.head
        temp = None
        count = 0
        while copy_head is not None:
            temp = copy_head.previousid
            copy_head.previousid = copy_head.nextid
            copy_head.nextid = temp
            copy_head = copy_head.previousid
        if temp is not None:
            self.head = temp.previousid

    def push(self, data, index):
        new_node = Node(data)
        copy_head = self.head
        position = 0
        if position == index:
            self.push_front(data)
        else:
            while copy_head is not None and position + 1 != index:
                position = position + 1
                copy_head = copy_head.nextid

            if copy_head is not None:
                new_node.nextid = copy_head.nextid
                new_node.previousid = copy_head
                copy_head.nextid = new_node
                copy_head.nextid.previousid = new_node
            else:
                print("Index not present")

    def push_before(self, data, index):
        return self.push(data, index-1)

    def pop(self, index):
        if self.head is None:
            return
        copy_head = self.head
        position = 0
        if position == index:
            self.pop_front()
        else:
            while copy_head is not None and position + 1 != index:
                position = position + 1
                copy_head = copy_head.nextid

            if copy_head is not None:
                copy_head.nextid = copy_head.nextid.nextid
                copy_head.nextid.nextid.previousid = copy_head
            else:
                print("Index not present")

    def pop_before(self, index):
        return self.pop(index-1)

    def data_search(self,data):
        copy_head = self.head
        while copy_head is not None and copy_head.data != data:
            if copy_head.data == data:
                print(data + 'is in list')
            copy_head = copy_head.nextid

    def listsplit(self):
        copy_head = self.head
        A = DoublyLinkedList()
        B = DoublyLinkedList()
        while copy_head is not None:
            if copy_head.data >= 0:
                A.push_front(copy_head.data)
            else:
                B.push_front(copy_head.data)
            copy_head = copy_head.nextid
        return A,B

    def simplenum(self):
        copy_head = self.head
        while copy_head is not None:
            flag = False
            for i in range(2, copy_head.data//2 + 1):
                if copy_head.data % i == 0:
                    flag = True
                    break
            if not flag:
                print(copy_head.data)
            copy_head = copy_head.nextid













