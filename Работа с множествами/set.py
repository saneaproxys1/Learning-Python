#Задача 1: Создание множества и вывод элементов
# Создаем множество с несколькими элементами
my_set = {1, 2, 3, 4, 5}
# Выводим элементы множества
print(my_set)

#Задача 2: Объединение двух множеств
# Создаем два множества
set1 = {1, 2, 3}
set2 = {3, 4, 5}
# Объединяем множества
union_set = set1.union(set2)
print(f"Объединенное множество: {union_set}")

#Задача 3: Пересечение двух множеств
# Создаем два множества
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5}
# Находим пересечение множеств
intersection_set = set1.intersection(set2)
print(f"Пересечение множеств: {intersection_set}")

#Задача 4: Разность между двумя множествами
# Создаем два множества
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5}
# Находим разность между множествами
difference_set = set1.difference(set2)
print(f"Разность между множествами (set1 - set2): {difference_set}")

#Задача 5: Проверка наличия элемента в множестве
# Создаем множество с данными
my_set = {10, 20, 30, 40, 50}
# Запрашиваем у пользователя элемент для проверки
search_item = int(input("Введите элемент для проверки: "))
# Проверяем наличие элемента в множестве
if search_item in my_set:
    print(f"Элемент {search_item} найден в множестве.")
else:
    print(f"Элемент {search_item} не найден в множестве.")
    
#Задача 6: Фильтрация элементов множества по условию
# Создаем множество с числами
my_set = {15, 30, 25, 10, 35}
# Задаем пороговое значение для фильтрации
threshold = 20
# Фильтруем множество
filtered_set = {item for item in my_set if item > threshold}
print(f"Элементы множества больше {threshold}: {filtered_set}")

#Задача 7: Проверка на непересечение двух множеств
# Создаем два множества
set1 = {1, 2, 3, 4}
set2 = {5, 6, 7}
# Проверяем на непересечение множеств
if set1.isdisjoint(set2):
    print("Множества не имеют общих элементов.")
else:
    print("Множества имеют общие элементы.")
    
#Задача 8: Проверка включения одного множества в другое
# Создаем два множества
set1 = {1, 2, 3}
set2 = {1, 2, 3, 4, 5}
# Проверяем, включено ли set1 в set2
if set1.issubset(set2):
    print("Множество set1 включено в множество set2.")
else:
    print("Множество set1 не включено в множество set2.")
    
#Задача 9: Обновление множества по условию
# Создаем исходное множество и множество для обновления
original_set = {10, 20, 30}
update_set = {15, 25, 35}
# Задаем пороговое значение для добавления элементов
threshold = 20
# Обновляем множество, добавляя элементы из update_set больше threshold
original_set.update(item for item in update_set if item > threshold)
print(f"Обновленное множество: {original_set}")

#Задача 10: Вывод элементов множества с использованием цикла
# Создаем множество с данными
my_set = {10, 20, 30, 40, 50}
# Выводим каждый элемент множества
for item in my_set:
    print(item)
    
#Задача 11: Суммирование элементов множества с использованием цикла
# Создаем множество с числами
my_set = {15, 30, 25, 10, 35}
# Вычисляем сумму элементов множества
total_sum = 0
for item in my_set:
    total_sum += item
print(f"Сумма элементов множества: {total_sum}")

#Задача 12: Поиск минимального значения в множестве с использованием цикла
# Создаем множество с числами
my_set = {15, 30, 25, 10, 35}
# Находим минимальное значение в множестве
min_value = min(my_set)
print(f"Минимальное значение в множестве: {min_value}")

#Задача 13: Фильтрация элементов множества с использованием цикла
# Создаем множество с числами
my_set = {15, 30, 25, 10, 35}
# Задаем пороговое значение для фильтрации
threshold = 20
# Фильтруем множество
filtered_set = set()
for item in my_set:
    if item > threshold:
        filtered_set.add(item)
print(f"Элементы множества больше {threshold}: {filtered_set}")

#Задача 14: Объединение двух множеств с использованием цикла
# Создаем два множества с числами
set1 = {1, 2, 3}
set2 = {3, 4, 5}
# Объединяем множества с помощью цикла
union_set = set1.copy()
for item in set2:
    union_set.add(item)
print(f"Объединенное множество: {union_set}")
