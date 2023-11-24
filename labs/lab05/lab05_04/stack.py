class Node:
    def __init__(self, data):
        self.data = data
        self.nextid = None

class LinkedListStack:
    def __init__(self):
        self.top = None

    def is_empty(self):
        if self.top is None:
            return True
        return False

    def push(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.top = new_node
        else:
            new_node.nextid = self.top
            self.top = new_node

    def pop(self):
        if self.is_empty():
            return print('Стек пуст')
        else:
            self.top = self.top.nextid

    def print(self):
        copy_top = self.top
        while not copy_top.nextid.is_empty:
            print(copy_top.data)
            copy_top = copy_top.nextid

    def get_top(self):
        if self.is_empty():
            return None
        return self.top.data

    def clear(self):
        while not self.top.nextid.is_empty:
            self.top = self.top.nextid


def task1(bracket_str):
    new_stack = LinkedListStack()
    open_brackets = ['[','(','{']
    close_brackets = [']',')','}']
    if len(bracket_str) % 2 != 0:
        return 'wrong string'
    for i in range(len(bracket_str)):
        if bracket_str[i] in open_brackets:
            new_stack.push(bracket_str[i])
        else:
            if bracket_str[i] == close_brackets[0]:
                if open_brackets[0] == new_stack.get_top():
                    new_stack.pop()
                else:
                    return 'wrong string'
            elif bracket_str[i] == close_brackets[1]:
                if open_brackets[1] == new_stack.get_top():
                    new_stack.pop()
                else:
                    return 'wrong string'
            elif bracket_str[i] == close_brackets[2]:
                if open_brackets[2] == new_stack.get_top():
                    new_stack.pop()
                else:
                    return 'wrong string'
            else:
                return 'wrong string'
    return 'Good string'

def task2(polish_str):
    new_stack = LinkedListStack()
    for i in range(len(polish_str)):
        if polish_str[i].isdigit():
            new_stack.push(int(polish_str[i]))
        elif polish_str[i] == '+':
            tmp = new_stack.top.data + new_stack.top.nextid.data
            new_stack.pop()
            new_stack.pop()
            new_stack.push(tmp)
        elif polish_str[i] == '-':
            tmp = new_stack.top.data - new_stack.top.nextid.data
            new_stack.pop()
            new_stack.pop()
            new_stack.push(tmp)
        elif polish_str[i] == '/':
            tmp = new_stack.top.data / new_stack.top.nextid.data
            new_stack.pop()
            new_stack.pop()
            new_stack.push(tmp)
        elif polish_str[i] == '*':
            tmp = new_stack.top.data * new_stack.top.nextid.data
            new_stack.pop()
            new_stack.pop()
            new_stack.push(tmp)
    return new_stack.get_top()






