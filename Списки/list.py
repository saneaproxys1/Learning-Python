#Задача 1: Вывод элементов списка
numbers = [1, 2, 3, 4, 5]
print("Элементы списка:", numbers)

#Задача 2: Добавление элемента в список
my_list = []
my_list.append(1)
my_list.append(2)
my_list.append(3)
print("Список после добавления элементов:", my_list)

#Задача 3: Доступ к элементу по индексу
fruits = ['apple', 'banana', 'cherry']
print("Первый элемент списка:", fruits[0])
print("Второй элемент списка:", fruits[1])
print("Третий элемент списка:", fruits[2])

#Задача 4: Изменение элемента списка
numbers = [1, 2, 3, 4, 5]
print("Исходный список:", numbers)
numbers[2] = 10
print("Список после изменения элемента:", numbers)

#Задача 5: Удаление элемента из списка
colors = ['red', 'green', 'blue']
print("Исходный список:", colors)
removed_color = colors.pop(1)  # Удаляем второй элемент (индекс 1)
print("Список после удаления элемента:", colors)
print("Удаленный элемент:", removed_color)

#Задача 6: Поиск элемента в списке
numbers = [1, 2, 3, 4, 5]
search_number = int(input("Введите число для поиска: "))
if search_number in numbers:
    print(f"Число {search_number} найдено в списке.")
else:
    print(f"Число {search_number} не найдено в списке.")
    
#Задача 7: Подсчет элементов в списке
my_list = [10, 20, 30, 40, 50]
if len(my_list) > 0:
    print(f"Количество элементов в списке: {len(my_list)}")
else:
    print("Список пуст.")
    
#Задача 8: Проверка на четность элементов списка
numbers = [2, 4, 6, 7, 8]
all_even = all(num % 2 == 0 for num in numbers)
if all_even:
    print("Все элементы списка четные.")
else:
    print("В списке есть хотя бы один нечетный элемент.")
    
#Задача 9: Проверка на упорядоченность списка
numbers = [1, 3, 5, 7, 6]
if numbers == sorted(numbers):
    print("Список упорядочен по возрастанию.")
elif numbers == sorted(numbers, reverse=True):
    print("Список упорядочен по убыванию.")
else:
    print("Список не упорядочен.")
    
#Задача 10: Проверка наличия дубликатов в списке
my_list = [1, 2, 3, 3, 4, 5]
has_duplicates = len(my_list) != len(set(my_list))
if has_duplicates:
    print("В списке есть повторяющиеся элементы.")
else:
    print("В списке нет повторяющихся элементов.")
    
#Задача 11: Вывод элементов списка с использованием цикла
numbers = [1, 2, 3, 4, 5]
print("Элементы списка:")
for num in numbers:
    print(num)
    
#Задача 12: Сумма элементов списка с использованием цикла
numbers = [1, 2, 3, 4, 5]
sum_numbers = 0
for num in numbers:
    sum_numbers += num
print("Сумма элементов списка:", sum_numbers)

#Задача 13: Поиск наименьшего элемента в списке с использованием цикла
numbers = [5, 2, 9, 1, 7]
min_number = numbers[0]
for num in numbers:
    if num < min_number:
        min_number = num
print("Наименьший элемент списка:", min_number)

#Задача 14: Удаление элементов из списка с использованием цикла
numbers = [8, 12, 4, 15, 6, 20]
print("Исходный список:", numbers)
filtered_numbers = []
for num in numbers:
    if num >= 10:
        filtered_numbers.append(num)
print("Список после удаления элементов меньше 10:", filtered_numbers)

#Задача 15: Поиск элемента по условию с использованием цикла
numbers = [5, 9, 12, 7, 18, 25]
has_multiple_of_3 = False
for num in numbers:
    if num % 3 == 0:
        has_multiple_of_3 = True
        break
if has_multiple_of_3:
    print("В списке есть элементы, кратные 3.")
else:
    print("В списке нет элементов, кратных 3.")
