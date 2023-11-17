class Stack:
    def __init__(self):
        self.__data = []

    def Push(self, val):
        self.__data.insert(0, val)

    def Top(self):
        if len(self.__data) == 0:
            raise RuntimeError("Cannot Top empty Stack")
        return self.__data[0]

    def Pop(self):
        if len(self.__data) == 0:
            raise RuntimeError("Cannot Pop empty Stack")
        item = self.__data.pop(0)
        return item

    def IsEmpty(self):
        return len(self.__data) == 0

    def __str__(self) -> str:
        res = ""
        if len(self.__data) == 0:
            return res
        for ch in self.__data:
            res += str(ch) + "\n"
        return res


def equal_brackets(string: str):
    stack = Stack()
    open_brackets = ['(', '[', '{']
    close_brackets = [')', ']', '}']
    match_brackets = {
        ')': '(',
        ']': '[',
        '}': '{'
    }

    for char in string:
        if char in open_brackets:
            stack.Push(char)
        elif char in close_brackets:
            if stack.IsEmpty() or stack.Top() != match_brackets[char]:
                return "Brackets does not correct!"
            else:
                stack.Pop()


def postfix(eq: str):
    st = Stack()
    eq = eq.split()
    for ch in eq:
        if ch.isnumeric():
            st.Push(int(ch))
        elif ch == '+':
            num1 = st.Pop()
            num2 = st.Pop()
            st.Push(num2 + num1)
        elif ch == '*':
            num1 = st.Pop()
            num2 = st.Pop()
            st.Push(num2 * num1)
    return st.Top()


stack = Stack()
print("1 - Вставка в стек",
      "2 - Просмотр верхушки",
      "3 - Удаление верхушки",
      "4 - Проверка на пустоту",
      "5 - Задание 1",
      "6 - Задание 2",
      "0 - Вывод стека",
      sep="\n"
      )
while True:
    command = int(input("Введите команду: "))
    match command:
        case 1:
            val = input("Введите значение: ")
            stack.Push(val)
        case 2:
            print(stack.Top())
        case 3:
            stack.Pop()
        case 4:
            if stack.IsEmpty():
                print("Empty Stack")
            else:
                print(f"Stack in not empty:\n{stack}")
        case 5:
            string = input("Введите строчку: ")
            equal_brackets(string)
            print("String is good")
        case 6:
            eq = input("Введите выражение: ")
            print(postfix(eq))
        case 0:
            print(stack)
        case _:
            print("Несуществующая команда!")
