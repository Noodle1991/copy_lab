from doublylinkedlist import DoublyLinkedList
my_list = DoublyLinkedList()
print("Выберите действие:")
print("1. Добавить элемент")
print("2. Вывести список")
print("3. Перевернуть список")
print("4. Удалить элемент с конца")
print("5. Удалить элемент с начала")
print("6. Удалить элемент после значения")
print(
    "7. Удалить элемент перед значением")
print("8. по списку L строит два новых списка: L1 – из положительных элементов и L2 – из отрицательных элементов списка L.")
print("9. Продублировать все простые числа")
print("10. Выйти.")
while True:
    choice = input("Введите номер действия: ")

    if choice == '1':
        data = int(input("Введите элемент для добавления: "))
        my_list.push_back(data)
        print("Элемент добавлен в список.")
    elif choice == '2':
        print("Содержимое списка:")
        my_list.print_linkedlist()
    elif choice == '3':
        print("Перевернутый список:")
        my_list.reverse_list()
        my_list.print_linkedlist()
    elif choice == '4':
        my_list.pop_back()
    elif choice == '5':
        my_list.pop_front()
    elif choice == '6':
        index = int(input("Введите индекс: "))
        my_list.pop(index)
    elif choice == '7':
        index = int(input("Введите индекс: "))
        my_list.pop_before(index)
    elif choice == '8':
        my_list.listsplit()
    elif choice == '9':
        print("Простые числа:")
        my_list.simplenum()
    elif choice == '10':
        break