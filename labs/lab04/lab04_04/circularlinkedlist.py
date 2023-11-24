class Node:
    def __init__(self, data):
        self.data = None
        self.nextid = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def push_front(self, data):
        new_node = Node(data)
        copy_head = self.head
        if self.head is None:
            new_node.nextid = new_node
        else:
            while copy_head.nextid != self.head:
                copy_head = copy_head.nextid
            copy_head.nextid = new_node
            new_node.nextid = self.head
        self.head = new_node

    def push_back(self, data):
        new_node = Node(data)
        copy_head = self.head
        if self.head is None:
            new_node.nextid = new_node
        else:
            while copy_head.nextid != self.head:
                copy_head = copy_head.nextid
            copy_head.nextid = new_node
            new_node.nextid = self.head

    def push(self, data, index):
        new_node = Node(data)
        copy_head = self.head
        while copy_head.nextid != self.head:
            if copy_head.data == data:
                new_node.nextid = copy_head.nextid
                copy_head.nextid = new_node
                return
            copy_head = copy_head.nextid

        if copy_head.data == data:
            new_node.nextid = copy_head.nextid
            copy_head.nextid = new_node

    def pop_front(self):
        if self.head.nextid == self.head:
            self.head = None
        else:
            copy_head = self.head
            while copy_head.nextid != self.head:
                copy_head = copy_head.nextid
            copy_head.nextid = self.head.nextid
            self.head = self.head.nextid

    def pop_back(self):
        if self.head.nextid == self.head:
            self.head = None
        else:
            copy_head = self.head
            while copy_head.nextid != self.head:
                copy_head = copy_head.nextid
            copy_head.nextid = self.head

    def pop(self, index): # after value
        copy_head = self.head
        while copy_head.nextid.data != index:
            copy_head = copy_head.nextid
        copy_head.nextid = copy_head.nextid.nextid

    def pop_before(self, index):
        copy_head = self.head
        index = 0
        while copy_head.nextid.nextid.data != index:
            copy_head = copy_head.nextid
        copy_head.nextid = copy_head.nextid.nextid

    def clear_list(self):
        copy_head = self.head
        while self.head.nextid != self.head:
            self.head = self.head.nextid
        self.head = self.head.nextid

    def reverse(self):
        prev = None
        copy_head = self.head
        while True:
            next_node = copy_head.nextid
            copy_head.nextid = prev
            prev = copy_head
            copy_head = next_node
            if copy_head == self.head:
                break

        self.head = prev

    def print_linkedlist(self): #iterating over a singly linked list
        copy_head = self.head
        while copy_head.nextid != self.head and copy_head is not None:
            print(copy_head.data)
            copy_head = copy_head.nextid
        if copy_head == self.head:
            print('...')


    def task1(self):
        copy_head = self.head
        copylist = []
        while copy_head.nextid != self.head:
            copylist.append(copy_head.data)
            copy_head = copy_head.nextid
        return copylist.sort()

def task2(list1,list2):
    copy_head1 = list1.head
    copy_head2 = list2.head
    copylist = []
    while copy_head1.nextid != list1.head:
        copylist.append(copy_head1.data)
        copy_head1 = copy_head1.nextid
    while copy_head2.nextid != list2.head:
        copylist.append(copy_head2.data)
        copy_head2 = copy_head2.nextid
    copylist.sort()
    list3 = CircularLinkedList()
    for i in copylist:
        list3.push_front(copylist[i])






