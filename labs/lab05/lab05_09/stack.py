class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            print("Стек пуст")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            print("Стек пуст")

    def size(self):
        return len(self.items)

    def clear(self):
        self.items = []

    def display(self):
        if self.is_empty():
            print("Стек пуст.")
        else:
            print("Вершина")
            for item in self.items[::-1]:
                print(item)
            print("Дно")


def brackets_balance(text):
    stack = Stack()
    brackets = {'(': ')', '[': ']', '{': '}'}
    errors = False

    for char in text:
        if char in '([{':
            stack.push(char)
        elif char in ')]}':
            if stack.is_empty():
                errors = True
                break
            if brackets[stack.peek()] == char:
                stack.pop()
            else:
                errors = True
                break

    if errors or not stack.is_empty():
        print("Несбалансированные скобки")
    else:
        print("Скобки сбалансированы")


def postfix_culculation(expression):
    stack = Stack()
    operators = "+-*/"

    for item in expression:
        if item.isdigit():
            stack.push(int(item))
        elif item in operators:
            operand2 = stack.pop()
            operand1 = stack.pop()
            if item == "+":
                result = operand1 + operand2
            elif item == "-":
                result = operand1 - operand2
            elif item == "*":
                result = operand1 * operand2
            elif item == "/":
                result = operand1 / operand2

            stack.push(result)

    if stack.is_empty():
        print("Invalid postfix expression")
    return stack.pop()


stack = Stack()

while True:
    print("Выберите действие:")
    print("1. Добавить элемент в стек")
    print("2. Удалить элемент из стека")
    print("3. Просмотреть вершину стека")
    print("4. Проверить стек на пустоту")
    print("5. Получить размер стека")
    print("6. Очистить стек")
    print("7. Проверить баланс скобок")
    print("8. Вычислить выражение в постфиксной нотации")
    print("9. Вывести стек")
    print("10. Выйти")

    choice = input("Введите номер выбранного действия: ")

    if choice == "1":
        item = input("Введите элемент, который нужно добавить в стек: ")
        stack.push(item)
        print("Элемент успешно добавлен в стек.")

    elif choice == "2":
        if not stack.is_empty():
            removed_item = stack.pop()
            print(f"Удален элемент из стека: {removed_item}")
        else:
            print("Стек пуст. Невозможно удалить элемент.")

    elif choice == "3":
        if not stack.is_empty():
            top_item = stack.peek()
            print(f"Вершина стека: {top_item}")
        else:
            print("Стек пуст. Вершина не доступна.")

    elif choice == "4":
        if stack.is_empty():
            print("Стек пуст.")
        else:
            print("Стек не пуст.")

    elif choice == "5":
        size = stack.size()
        print(f"Размер стека: {size}")

    elif choice == "6":
        stack.clear()
        print("Стек очищен.")

    elif choice == "7":
        text = input("Введите текст для проверки баланса скобок: ")
        brackets_balance(text)

    elif choice == "8":
        expression = input("Введите выражение в постфиксной нотации: ")
        result = postfix_culculation(expression)
        print(f"Результат вычисления: {result}")

    elif choice == "9":
        stack.display()

    elif choice == "10":
        print("Выход из программы.")
        break

    else:
        print("Некорректный выбор. Пожалуйста, выберите действие из списка.")
