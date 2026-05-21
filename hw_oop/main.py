"""
Точка входа для выполнения домашнего задания по ООП.

Этот скрипт создает объекты классов Student, Lecturer и Reviewer,
моделирует их взаимодействие (выставление оценок) и выводит результаты.

Зависимости:
    Должен находиться в одной папке с файлами:
    - student.py
    - mentor.py
    - lecturer.py
    - reviewer.py
    - utils.py

Как запустить:
    $ python main.py

Результат:
    В консоль будет выведена информация о проверке заданий,
    а также результаты "полевых испытаний" (средние оценки).
"""
from student import Student
from mentor import Mentor
from lecturer import Lecturer
from reviewer import Reviewer
from utils import avg_grade_all_students, avg_grade_all_lecturers

# --- Блок для Задания 4: Полевые испытания ---
# Создаем по 2 экземпляра каждого класса с именами из примеров

# Студенты
student_1 = Student('Алёхина', 'Ольга', 'Ж')
student_2 = Student('Ник', 'Смит', 'М')

# Лекторы
lecturer_1 = Lecturer('Иван', 'Иванов')
lecturer_2 = Lecturer('Стив', 'Морганс')

# Рецензенты (Проверяющие)
reviewer_1 = Reviewer('Пётр', 'Петров')
reviewer_2 = Reviewer('Дэн', 'Милман')

# --- Взаимодействие объектов (вызов методов) ---

# Прикрепляем курсы
student_1.courses_in_progress += ['Python', 'Java']
student_2.courses_in_progress += ['Python', 'Git']

lecturer_1.courses_attached += ['Python']
lecturer_2.courses_attached += ['Git']

reviewer_1.courses_attached += ['Python']
reviewer_2.courses_attached += ['Git']

# Рецензенты ставят оценки студентам (метод rate_hw)
print("--- Оценки от рецензентов ---")
reviewer_1.rate_hw(student_1, 'Python', 10)
reviewer_1.rate_hw(student_1, 'Python', 9)
reviewer_2.rate_hw(student_2, 'Git', 8)
reviewer_2.rate_hw(student_2, 'Python', 7)

print(f"У {student_1.name} оценки: {student_1.grades}")
print(f"У {student_2.name} оценки: {student_2.grades}")
print("-" * 20)

# Студенты ставят оценки лекторам (метод rate_lecture)
print("--- Оценки лекторам от студентов ---")
student_1.rate_lecture(lecturer_1, 'Python', 9)
student_2.rate_lecture(lecturer_2, 'Git', 8)
student_2.rate_lecture(lecturer_1, 'Python', 7)  # Второй студент тоже оценил первого лектора

print(f"У {lecturer_1.name} оценки: {lecturer_1.grades}")
print(f"У {lecturer_2.name} оценки: {lecturer_2.grades}")
print("=" * 40)

# --- Блок для Задания 3: Полиморфизм и магические методы ---

print("--- Вывод информации через __str__ ---")
print(reviewer_1)  # Имя: Пётр ...
print(lecturer_1)  # Имя: Иван ...
print(student_1)  # Имя: Алёхина ...
print("=" * 40)

# --- Блок для Задания 4: Функции подсчета средних оценок ---

# Создаем списки объектов для передачи в функции
all_students = [student_1, student_2]
all_lecturers = [lecturer_1, lecturer_2]

# Считаем среднюю оценку студентов по курсу Python
python_students_avg = avg_grade_all_students(all_students, 'Python')
print(f"Средняя оценка студентов по Python: {python_students_avg:.1f}")

# Считаем среднюю оценку лекторов по курсу Python
python_lecturers_avg = avg_grade_all_lecturers(all_lecturers, 'Python')
print(f"Средняя оценка лекторов по Python: {python_lecturers_avg:.1f}")

print("\n" + "=" * 20 + " ПРОВЕРКА ЗАДАНИЯ №1 И №2 " + "=" * 20)

# Средняя оценка студентов
print(f"Средняя оценка {student_1.name}: {student_1.get_avg_grade():.1f}")
print(f"Средняя оценка {student_2.name}: {student_2.get_avg_grade():.1f}")

print("\n--- Результаты сравнения ---")

# Сравнение 1: Проверка оператора "больше" для студентов
if student_1 > student_2:
    print(f"{student_1.name} {student_1.surname} учится лучше, чем {student_2.name} {student_2.surname}")
elif student_2 > student_1:
    print(f"{student_2.name} {student_2.surname} учится лучше, чем {student_1.name} {student_1.surname}")
else:
    print("У студентов одинаковые средние оценки")

# Сравнение 2: Проверка оператора "меньше" для студентов
if student_1 < student_2:
    print(f"Проверка 'меньше' работает: Оценка {student_1.name} меньше, чем у {student_2.name}")

# Сравнение 3: Проверка на равенство для студентов
if student_1 == student_2:
    print(f"Проверка на равенство: У студентов одинаковые успехи")
else:
    print("Проверка на равенство: Успехи студентов различаются")

# Средняя оценка лекторов

print(f"Средняя оценка {lecturer_1.name}: {lecturer_1.get_avg_grade():.1f}")
print(f"Средняя оценка {lecturer_2.name}: {lecturer_2.get_avg_grade():.1f}")

print("\n--- Результаты сравнения (с использованием операторов) ---")

# Сравнение 1: Проверка оператора 'больше' для лекторов
if lecturer_1 > lecturer_2:
    print(f"Оператор '>' работает: {lecturer_1.name} {lecturer_1.surname} имеет оценку выше, чем {lecturer_2.name} {lecturer_2.surname}")
else:
    print(f"Оператор '>' работает: {lecturer_2.name} {lecturer_2.surname} имеет оценку не ниже, чем у {lecturer_1.name} {lecturer_1.surname}")

# Сравнение 2: Проверка оператора 'меньше' (<) для лекторов
if lecturer_2 < lecturer_1:
    print(f"Оператор '<' работает: Оценка {lecturer_2.name} ниже, чем у {lecturer_1.name}")

# Сравнение 3: Проверка оператора 'равно' (==) для лекторов
# Для наглядности создадим лектора с такой же оценкой, как у второго
print("\n--- Проверка на равенство ---")
lecturer_3 = Lecturer('Пётр', 'Сидоров')
# Копируем оценки от лектора 2, чтобы они были равны
lecturer_3.grades = lecturer_2.grades.copy()

if lecturer_2 == lecturer_3:
    print(f"Оператор '==' работает: У {lecturer_2.name} и {lecturer_3.name} одинаковые средние оценки")
else:
    print("Ошибка: Оператор '==' работает некорректно")

# Проверки задания №1 (Наследование)
print("\n--- Проверка Задания №1 ---")
lecturer_test = Lecturer('Иван', 'Иванов')
reviewer_test = Reviewer('Пётр', 'Петров')
print(isinstance(lecturer_test, Mentor))  # True
print(isinstance(reviewer_test, Mentor))  # True
print(lecturer_test.courses_attached)  # []
print(reviewer_test.courses_attached)  # []

# Проверки задания №2 (Взаимодействие)
print("\n--- Проверка Задания №2 ---")
lecturer_test = Lecturer('Иван', 'Иванов')
reviewer_test = Reviewer('Пётр', 'Петров')
student_test = Student('Алёхина', 'Ольга', 'Ж')

student_test.courses_in_progress += ['Python', 'Java']
lecturer_test.courses_attached += ['Python', 'C++']
reviewer_test.courses_attached += ['Python', 'C++']

print(student_test.rate_lecture(lecturer_test, 'Python', 7))  # None
print(student_test.rate_lecture(lecturer_test, 'Java', 8))  # Ошибка
print(student_test.rate_lecture(lecturer_test, 'С++', 8))  # Ошибка
print(student_test.rate_lecture(reviewer_test, 'Python', 6))  # Ошибка

print(lecturer_test.grades)  # {'Python': [7]}