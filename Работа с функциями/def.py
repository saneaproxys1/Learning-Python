#Задача 1: Вычисление площади прямоугольника
# Функция для вычисления площади прямоугольника
def calculate_rectangle_area(length, width):
    area = length * width
    return area
# Пример использования функции
length = float(input("Введите длину прямоугольника: "))
width = float(input("Введите ширину прямоугольника: "))
print(f"Площадь прямоугольника с длиной {length} и шириной {width} равна {calculate_rectangle_area(length, width)}")

#Задача 2: Проверка на простое число
# Функция для проверки простого числа
def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True
# Пример использования функции
num = int(input("Введите число для проверки: "))
if is_prime(num):
    print(f"{num} - простое число.")
else:
    print(f"{num} - не простое число.")
    
#Задача 3: Генерация списка чисел Фибоначчи
# Функция для генерации чисел Фибоначчи
def fibonacci_list(n):
    fib_list = [0, 1]
    while fib_list[-1] + fib_list[-2] < n:
        fib_list.append(fib_list[-1] + fib_list[-2])
    return fib_list
# Пример использования функции
limit = int(input("Введите верхнюю границу для чисел Фибоначчи: "))
print(f"Числа Фибоначчи до {limit}: {fibonacci_list(limit)}")

#Задача 4: Поиск среднего значения списка чисел
# Функция для вычисления среднего значения списка
def average(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)
# Пример использования функции
nums = [float(x) for x in input("Введите числа через пробел: ").split()]
print(f"Среднее значение чисел {nums}: {average(nums)}")

#Задача 5: Проверка на палиндром
# Функция для проверки палиндрома
def is_palindrome(s):
    s = s.lower().replace(" ", "")  # Приводим к нижнему регистру и убираем пробелы
    return s == s[::-1]
# Пример использования функции
string = input("Введите строку для проверки на палиндром: ")
if is_palindrome(string):
    print(f"Строка '{string}' является палиндромом.")
else:
    print(f"Строка '{string}' не является палиндромом.")
