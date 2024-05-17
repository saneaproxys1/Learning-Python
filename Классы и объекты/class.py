#Задача 1: Создание класса с методами и атрибутами
# Класс Circle для представления круга
class Circle:
    def __init__(self, radius, color):
        self.radius = radius
        self.color = color
    
    def area(self):
        return 3.14 * self.radius**2
    
    def circumference(self):
        return 2 * 3.14 * self.radius
    
# Создаем объекты класса Circle
circle1 = Circle(5, "red")
circle2 = Circle(3, "blue")
# Выводим информацию о кругах
print(f"Круг 1: Радиус {circle1.radius}, Цвет {circle1.color}, Площадь {circle1.area()}, Длина окружности {circle1.circumference()}")
print(f"Круг 2: Радиус {circle2.radius}, Цвет {circle2.color}, Площадь {circle2.area()}, Длина окружности {circle2.circumference()}")

#Задача 2: Наследование и использование методов родительского класса
# Класс Shape для представления фигуры
class Shape:
    def __init__(self, color):
        self.color = color
    
    def info(self):
        return f"Это фигура цвета {self.color}"

# Класс Rectangle, наследующийся от Shape
class Rectangle(Shape):
    def __init__(self, color, width, height):
        super().__init__(color)
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

# Создаем объект класса Rectangle
rectangle = Rectangle("green", 10, 5)

# Выводим информацию о прямоугольнике
print(rectangle.info())
print(f"Ширина: {rectangle.width}, Высота: {rectangle.height}, Площадь: {rectangle.area()}")

#Задача 3: Использование статического метода в классе
# Класс MathOperations с статическим методом для вычисления факториала
class MathOperations:
    @staticmethod
    def factorial(n):
        if n == 0:
            return 1
        else:
            return n * MathOperations.factorial(n - 1)

# Используем статический метод для вычисления факториала
num = 5
print(f"Факториал числа {num}: {MathOperations.factorial(num)}")

#Задача 4: Использование свойств для защиты данных
# Класс Person с использованием свойств
class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age
    
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, value):
        if value >= 0:
            self._age = value
        else:
            raise ValueError("Возраст должен быть положительным числом")

# Создаем объект класса Person
person = Person("Alice", 30)

# Изменяем возраст с помощью свойства age
person.age = 25
print(f"{person._name} возраст {person.age}")

# Попытка установить отрицательный возраст приведет к ошибке
try:
    person.age = -5
except ValueError as e:
    print(f"Ошибка: {e}")

#Задача 5: Использование методов класса для создания и обработки объектов
# Класс Student с использованием методов класса
class Student:
    total_students = 0  # переменная класса для хранения общего числа студентов
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.total_students += 1  # увеличиваем счетчик при создании нового студента
    
    @classmethod
    def count_students(cls):
        return cls.total_students

# Создаем несколько студентов
student1 = Student("Bob", 20)
student2 = Student("Alice", 22)
student3 = Student("Eve", 21)

# Выводим общее количество студентов
print(f"Общее количество студентов: {Student.count_students()}")
