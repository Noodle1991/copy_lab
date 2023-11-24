<h1>Федотов Андрей Владимирович</h1>
<h1>Вариант 15</h1>

---

<h2>Цель работы</h2>

<ul>
    <li>Изучение структуры данных «Стек», а также основных операций над ним.</li>
</ul>

---


<h2>Основное задание</h2>

<h3>Определение класса <code>Stack</code></h3>


```python
class Stack:
    def __init__(self):
        self.__data = []
    def __str__(self) -> str:
        res = ""
        if len(self.__data) == 0:
            return res
        for item in self.__data:
            res += str(item) + "\n"
        return res
```

<h3>Вставка в стек</h3>


```python
def Push(self, val):
        self.__data.insert(0, val)
```

<h3>Просмотр вершины стека</h3>


```python
def Top(self):
    if len(self.__data) == 0:
        raise RuntimeError("Cannot Top empty Stack")
    return self.__data[0]
```

<h3>Удаление вершины стека</h3>


```python
def Pop(self):
    if len(self.__data) == 0:
        raise RuntimeError("Cannot Pop empty Stack")
    item = self.__data.pop(0)
    return item
```

<h3>Проверка на пустоту</h3>


```python
 def IsEmpty(self):
    return len(self.__data) == 0
```

<h3>Приложение для работы со стеком</h3>


```python
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
            task1(string)
            print("String is good")
        case 6:
            eq = input("Введите выражение: ")
            print(task2(eq))
        case 0:
            print(stack)
        case _:
            print("Несуществующая команда!")
```

---

<h2>Дополнительные задания</h2>

<h3>Используя операции со стеком, написать программу, проверяющую своевременность закрытия скобок <code>( ) ,[ ] , { }</code> в строке символов (строка состоит из одних скобок этих типов).</h3>


```python
def task1(str: str):
    stack = Stack()
    opening_brackets = ['(', '[', '{']
    closing_brackets = [')', ']', '}']
    matching_brackets = {
        ')': '(',
        ']': '[',
        '}': '{'
    }
    
    for ch in str:
        if ch in opening_brackets:
            stack.Push(ch)
        elif ch in closing_brackets:
            if stack.IsEmpty() or stack.Top() != matching_brackets[ch]:
                return "Brackets doest not match!"
            else:
                stack.Pop()
    return "String is good!"
```

<h3>Написать программу вычисления значения выражения, представленного в обратной польской записи (в постфиксной записи). Выражение состоит из цифр от 1до 9 и знаков операции.</h3>


```python
def task2(eq: str):
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
        elif ch == '-':
            num1 = st.Pop()
            num2 = st.Pop()
            st.Push(num2 - num1)
        elif ch == '/':
            num1 = st.Pop()
            num2 = st.Pop()
            st.Push(num2 / num1)
    return st.Top()
```
