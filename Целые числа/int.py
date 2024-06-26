#Задача №1
#Какое целое число получим в итоге?
a = 11 * 2 ** 2-13 / 4 + 7;
print (a);
#Сначала по приоритету возводим в степень (2 ** 2). Далее умножаем (11 * 4). Потом делим (13 / 4). Следом вычитаем (44 - 3.25). На последнем этапе применяем сложение (40.75 + 7). Получаем число с плавающей точкой 47.75. Если привести его к типу int, то результат равняется 47.

#Задача №2
#Какие из представленных выражений можно преобразовать в целое десятичное число за одну операцию:
    #А) '123е'; - нельзя
    #Б) '91.4'; - нельзя
    #В) 524.345 ** 435345345311145345; - нельзя (очень длинное число для данных int)
    #Г) '7.1 + 4'; - нельзя
    #Д) '4' - 2; - нельзя
    #Е) '4 - 2'; - нельзя
    #Ж) '42'; - можно
    #З) -12.12; - можно
b = '42';
print (int(b))
c = -12.12;
print (int(c))

#Задача 1: Вывод остатка от деления на 7
number = int(input("Введите целое число: "))
remainder = number % 7
print("Остаток от деления на 7:", remainder)

#Задача 2: Возведение в куб
number = int(input("Введите целое число: "))
cube = number ** 3
print("Куб числа:", cube)

#Задача 3: Сложение трех чисел
a = int(input("Введите первое целое число: "))
b = int(input("Введите второе целое число: "))
c = int(input("Введите третье целое число: "))
sum_result = a + b + c
print("Сумма трех чисел:", sum_result)

#Задача 4: Вычисление разницы между числами
a = int(input("Введите первое целое число: "))
b = int(input("Введите второе целое число: "))
difference = a - b
print("Разница между числами:", difference)

# Задача 5: Умножение двух чисел
a = int(input("Введите первое целое число: "))
b = int(input("Введите второе целое число: "))
product = a * b
print("Произведение двух чисел:", product)

#Задача 6: Проверка на положительное число
number = int(input("Введите целое число: "))
if number > 0:
    print("Число является положительным.")
else:
    print("Число не является положительным.")
    
#Задача 7: Определение наибольшего из двух чисел
a = int(input("Введите первое целое число: "))
b = int(input("Введите второе целое число: "))
if a > b:
    print("Наибольшее число:", a)
else:
    print("Наибольшее число:", b)

#Задача 8: Проверка на кратность 10
number = int(input("Введите целое число: "))
if number % 10 == 0:
    print("Число делится на 10.")
else:
    print("Число не делится на 10.")
    
#Задача 9: Проверка числа на четность
number = int(input("Введите целое число: "))
if number % 2 == 0:
    print("Число является четным.")
else:
    print("Число не является четным.")
    
#Задача 10: Определение знака числа
number = int(input("Введите целое число: "))
if number > 0:
    print("Число положительное.")
elif number < 0:
    print("Число отрицательное.")
else:
    print("Число равно нулю.")
    
#Задача 11: Вывод всех четных чисел до n
n = int(input("Введите целое число: "))
for i in range(1, n + 1):
    if i % 2 == 0:
        print(i)
        
#Задача 12: Сумма чисел от 1 до n
n = int(input("Введите целое число: "))
sum_result = 0
for i in range(1, n + 1):
    sum_result += i
print("Сумма чисел от 1 до", n, ":", sum_result)

#Задача 13: Таблица умножения для числа n
n = int(input("Введите целое число: "))
for i in range(1, 11):
    print(n, "*", i, "=", n * i)

#Задача 14: Факториал числа
n = int(input("Введите целое число: "))
factorial = 1
for i in range(1, n + 1):
    factorial *= i
print("Факториал числа", n, ":", factorial)

#Задача 15: Обратный порядок чисел
n = int(input("Введите целое число: "))
for i in range(n, 0, -1):
    print(i)
