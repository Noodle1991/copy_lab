from stack import LinkedListStack, task1, task2

my_stack = LinkedListStack()

print("Выберите действие:")
print("1. Добавить элемент")
print("2. Вывести стек")
print("3. Удалить элемент стека")
print("4. Очистить стек")
print("5. Проверить своевременность закрытия скобок")
print("6. Вычислениe значения выражения, представленного в обратной польской записи")
print("7. Выйти.")
while True:
    choice = input("Введите номер действия: ")

    if choice == '1':
        data = int(input("Введите элемент для добавления: "))
        my_stack.push(data)
        print("Элемент добавлен в список.")
    elif choice == '2':
        print('Ваш стек:')
        my_stack.print()
    elif choice == '3':
        my_stack.pop()
        print('Элемент был удален')
    elif choice == '4':
        print('Стек очищен')
    elif choice == '5':
            bracket_str = input('Введите строчку без пробелов ')
            print(task1(bracket_str))
    elif choice == '6':
        polish_str = input('Введите строчку без пробелов')
        print(task2(polish_str))
    elif choice == '7':
        break
