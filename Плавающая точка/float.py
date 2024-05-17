#Задача 1: Округление числа до двух знаков после запятой
number = float(input("Введите число с плавающей точкой: "))
rounded_number = round(number, 2)
print("Округленное число:", rounded_number)

#Задача 2: Вычисление площади круга
radius = float(input("Введите радиус круга: "))
pi = 3.14159
area = pi * radius ** 2
print("Площадь круга:", area)

#Задача 3: Перевод температуры из Цельсия в Фаренгейты
celsius = float(input("Введите температуру в градусах Цельсия: "))
fahrenheit = celsius * 9/5 + 32
print("Температура в градусах Фаренгейта:", fahrenheit)

#Задача 4: Арифметическая операция
number1 = float(input("Введите первое число: "))
number2 = float(input("Введите второе число: "))
operator = input("Введите оператор (+, -, *, /): ")
result = eval(f"{number1} {operator} {number2}")
print("Результат:", result)

#Задача 5: Среднее значение
number1 = float(input("Введите первое число: "))
number2 = float(input("Введите второе число: "))
number3 = float(input("Введите третье число: "))
average = (number1 + number2 + number3) / 3
print("Среднее значение:", average)

#Задача 6: Проверка числа на положительность, отрицательность или ноль
number = float(input("Введите число с плавающей точкой: "))
if number > 0:
    print("Число положительное.")
elif number < 0:
    print("Число отрицательное.")
else:
    print("Число равно нулю.")
    
#Задача 7: Сравнение двух чисел
number1 = float(input("Введите первое число: "))
number2 = float(input("Введите второе число: "))
if number1 > number2:
    print("Большее число:", number1)
elif number2 > number1:
    print("Большее число:", number2)
else:
    print("Оба числа равны.")
    
#Задача 8: Проверка на попадание в диапазон
number = float(input("Введите число с плавающей точкой: "))
if 0 <= number <= 1:
    print("Число находится в диапазоне от 0 до 1.")
else:
    print("Число не находится в диапазоне от 0 до 1.")
    
#Задача 9: Сравнение трех чисел
number1 = float(input("Введите первое число: "))
number2 = float(input("Введите второе число: "))
number3 = float(input("Введите третье число: "))
if number1 <= number2 and number1 <= number3:
    print("Наименьшее число:", number1)
elif number2 <= number1 and number2 <= number3:
    print("Наименьшее число:", number2)
else:
    print("Наименьшее число:", number3)
    
#Задача 10: Проверка делимости на число с плавающей точкой
number1 = float(input("Введите первое число: "))
number2 = float(input("Введите второе число: "))
if number2 == 0:
    print("Деление на ноль невозможно.")
elif number1 % number2 == 0:
    print("Первое число делится на второе без остатка.")
else:
    print("Первое число не делится на второе без остатка.")
    
#Задача 11: Вывод чисел с плавающей точкой до заданного предела
limit = float(input("Введите предел (число с плавающей точкой): "))
current = 0.0
while current <= limit:
    print(current)
    current += 0.5
    
#Задача 12: Вычисление среднего арифметического
count = 0
total = 0.0
number = float(input("Введите число с плавающей точкой (отрицательное для завершения): "))
while number >= 0:
    total += number
    count += 1
    number = float(input("Введите следующее число: "))

if count > 0:
    average = total / count
    print("Среднее арифметическое введенных чисел:", average)
else:
    print("Не было введено ни одного числа.")
    
#Задача 13: Таблица умножения для числа с плавающей точкой
number = float(input("Введите число с плавающей точкой: "))
i = 1
while i <= 10:
    print(f"{number} * {i} = {number * i}")
    i += 1
    
#Задача 14: Проверка точности вычислений
epsilon = float(input("Введите точность (ε): "))
e_approx = 1.0
factorial = 1
term = 1.0
n = 1
while abs(term) > epsilon:
    factorial *= n
    term = 1.0 / factorial
    e_approx += term
    n += 1
print(f"Значение числа e с точностью {epsilon}:", e_approx)
