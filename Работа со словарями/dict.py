#Задача 1: Создание и вывод значений словаря
# Создаем словарь с оценками студентов
students = {
    'Alice': 85,
    'Bob': 92,
    'Charlie': 78,
    'David': 88,
    'Emma': 95
}
# Выводим все значения словаря
print(students.values())

#Задача 2: Доступ к элементу словаря по ключу
# Создаем словарь с возрастами людей
ages = {
    'Alice': 25,
    'Bob': 30,
    'Charlie': 35,
    'David': 28,
    'Emma': 27
}
# Выводим возраст человека по запросу пользователя
name = input("Введите имя человека: ")
print(ages.get(name, "Данные отсутствуют"))

#Задача 3: Добавление элемента в словарь
# Создаем пустой словарь
my_dict = {}
# Добавляем элементы в словарь
my_dict['key1'] = 'value1'
my_dict['key2'] = 'value2'
my_dict['key3'] = 'value3'
print(my_dict)

#Задача 4: Удаление элемента из словаря
# Создаем словарь с данными
data = {
    'key1': 'value1',
    'key2': 'value2',
    'key3': 'value3'
}
# Удаляем элемент по ключу 'key2'
data.pop('key2')
print(data)

#Задача 5: Подсчет элементов в словаре
# Создаем словарь с данными
data = {
    'key1': 'value1',
    'key2': 'value2',
    'key3': 'value3'
}
# Выводим количество элементов в словаре
print(len(data))

#Задача 6: Поиск элемента в словаре
# Создаем словарь с данными
students = {
    'Alice': 85,
    'Bob': 92,
    'Charlie': 78,
    'David': 88,
    'Emma': 95
}
# Запрашиваем у пользователя имя для поиска
search_name = input("Введите имя студента для поиска: ")
# Проверяем, есть ли такой студент в словаре
if search_name in students:
    print(f"Оценка студента {search_name}: {students[search_name]}")
else:
    print(f"Студент {search_name} не найден в базе данных.")
    
#Задача 7: Проверка наличия ключа в словаре
# Создаем словарь с данными
inventory = {
    'apple': 10,
    'banana': 5,
    'orange': 8,
    'grape': 3,
    'peach': 6
}
# Запрашиваем у пользователя название продукта для проверки
product_name = input("Введите название продукта для проверки наличия: ")
# Проверяем, есть ли такой продукт в инвентаре
if product_name in inventory:
    print(f"Продукт {product_name} есть в наличии.")
else:
    print(f"Продукт {product_name} отсутствует в наличии.")
    
#Задача 8: Подсчет элементов в словаре по условию
# Создаем словарь с данными (имена и возрасты)
ages = {
    'Alice': 25,
    'Bob': 30,
    'Charlie': 35,
    'David': 28,
    'Emma': 27
}
# Подсчитываем количество людей, чей возраст больше или равен 30
count = sum(1 for name, age in ages.items() if age >= 30)
print(f"Количество людей с возрастом 30 и старше: {count}")

#Задача 9: Фильтрация элементов словаря
# Создаем словарь с данными (имена и оценки)
grades = {
    'Alice': 85,
    'Bob': 92,
    'Charlie': 78,
    'David': 88,
    'Emma': 95
}
# Фильтруем студентов, у которых оценка выше 85
filtered_grades = {name: grade for name, grade in grades.items() if grade > 85}
print("Студенты с оценкой выше 85:")
for name, grade in filtered_grades.items():
    print(f"{name}: {grade}")
    
#Задача 10: Проверка наличия дубликатов в словаре
# Создаем словарь с данными (название товара и его количество)
inventory = {
    'apple': 10,
    'banana': 5,
    'orange': 8,
    'apple': 3,  # дубликат ключа 'apple'
    'peach': 6
}
# Проверяем наличие дубликатов в словаре
has_duplicates = len(inventory) != len(set(inventory))
if has_duplicates:
    print("Есть дублирующиеся ключи в словаре.")
else:
    print("Нет дублирующихся ключей в словаре.")
    
#Задача 11: Вывод ключей и значений словаря
# Создаем словарь с оценками студентов
grades = {
    'Alice': 85,
    'Bob': 92,
    'Charlie': 78,
    'David': 88,
    'Emma': 95
}
# Выводим все ключи и значения словаря
print("Список студентов и их оценок:")
for key, value in grades.items():
    print(f"{key}: {value}")
    
#Задача 12: Суммирование значений словаря
# Создаем словарь с числовыми значениями
numbers = {
    'a': 10,
    'b': 20,
    'c': 30,
    'd': 40,
    'e': 50
}
# Вычисляем сумму всех значений
total_sum = 0
for key, value in numbers.items():
    total_sum += value
print(f"Сумма всех чисел в словаре: {total_sum}")

#Задача 13: Поиск минимального значения в словаре
# Создаем словарь с числовыми значениями
numbers = {
    'a': 15,
    'b': 5,
    'c': 25,
    'd': 10,
    'e': 20
}
# Находим минимальное значение
min_value = None
for key, value in numbers.items():
    if min_value is None or value < min_value:
        min_value = value
print(f"Минимальное значение в словаре: {min_value}")

#Задача 14: Фильтрация словаря по условию
# Создаем словарь с числовыми значениями
numbers = {
    'a': 15,
    'b': 5,
    'c': 25,
    'd': 10,
    'e': 20
}
# Задаем пороговое значение для фильтрации
threshold = 15
# Фильтруем словарь по заданному условию
filtered_dict = {}
for key, value in numbers.items():
    if value > threshold:
        filtered_dict[key] = value
print("Элементы словаря, значения которых больше", threshold)
print(filtered_dict)

#Задача 15: Проверка наличия элементов в словаре по условию
# Создаем словарь с числовыми значениями
numbers = {
    'a': 15,
    'b': 5,
    'c': 25,
    'd': 10,
    'e': 20
}
# Задаем пороговое значение для проверки
threshold = 10
# Проверяем наличие значений меньше заданного
found_less_than_threshold = False
for key, value in numbers.items():
    if value < threshold:
        found_less_than_threshold = True
        break
if found_less_than_threshold:
    print(f"В словаре есть значения меньше {threshold}.")
else:
    print(f"В словаре нет значений меньше {threshold}.")
