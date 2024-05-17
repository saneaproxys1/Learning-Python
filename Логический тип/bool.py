#Задача 1: Проверка на четность
number = int(input("Введите целое число: "))
is_even = number % 2 == 0
print(f"Число {number} четное: {is_even}")

#Задача 2: Проверка на делимость
numerator = int(input("Введите первое целое число (делимое): "))
denominator = int(input("Введите второе целое число (делитель): "))
is_divisible = numerator % denominator == 0
print(f"Число {numerator} делится на {denominator} без остатка: {is_divisible}")

#Задача 3: Проверка вхождения в диапазон
number = int(input("Введите целое число: "))
is_in_range = 10 <= number <= 100
print(f"Число {number} находится в диапазоне от 10 до 100: {is_in_range}")

#Задача 4: Проверка на простое число
number = int(input("Введите целое число: "))
is_prime = number > 1 and all(number % i != 0 for i in range(2, int(number ** 0.5) + 1))
print(f"Число {number} простое: {is_prime}")

#Задача 5: Проверка на четность
number = int(input("Введите целое число: "))
if number % 2 == 0:
    print(f"Число {number} четное.")
else:
    print(f"Число {number} нечетное.")
    
#Задача 6: Проверка делимости
numerator = int(input("Введите первое целое число (делимое): "))
denominator = int(input("Введите второе целое число (делитель): "))
if denominator != 0 and numerator % denominator == 0:
    print(f"Число {numerator} делится на {denominator} без остатка.")
else:
    print(f"Число {numerator} не делится на {denominator} без остатка или делитель равен нулю.")
    
#Задача 7: Проверка вхождения в диапазон
number = int(input("Введите целое число: "))
if 10 <= number <= 100:
    print(f"Число {number} находится в диапазоне от 10 до 100.")
else:
    print(f"Число {number} не находится в диапазоне от 10 до 100.")
    
#Задача 8: Проверка на простое число
number = int(input("Введите целое число: "))
is_prime = True
if number < 2:
    is_prime = False
else:
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            is_prime = False
            break

if is_prime:
    print(f"Число {number} простое.")
else:
    print(f"Число {number} не является простым.")
