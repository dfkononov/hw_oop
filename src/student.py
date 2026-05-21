class Student:
    """
    Класс, описывающий студента.

    Хранит информацию о студенте, его курсах, оценках и позволяет
    оценивать лекции преподавателей.

    Атрибуты:
        name (str): Имя студента.
        surname (str): Фамилия студента.
        gender (str): Пол студента.
        finished_courses (list): Список завершенных курсов.
        courses_in_progress (list): Список курсов, которые студент изучает сейчас.
        grades (dict): Словарь с оценками за домашние задания.
                      Формат: {'Название курса': [оценка1, оценка2, ...]}.
    """

    def __init__(self, name: str, surname: str, gender: str):
        """
        Инициализирует нового студента.

        Args:
            name (str): Имя студента.
            surname (str): Фамилия студента.
            gender (str): Пол студента.
        """
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecture(self, lecturer, course, grade):
        """
        Ставит оценку лектору за лекцию по конкретному курсу.

        Оценка ставится только если:
        1. Объект является экземпляром класса Lecturer.
        2. Лектор ведет данный курс.
        3. Студент изучает данный курс.

        Args:
            lecturer: Объект класса Lecturer.
            course (str): Название курса.
            grade (int | float): Оценка за лекцию по 10-балльной шкале.

        Returns:
            str: Возвращает 'Ошибка', если условия не выполнены.
            None: Возвращает None, если оценка успешно выставлена.
        """
        from src.lecturer import Lecturer

        is_valid_lecturer = isinstance(lecturer, Lecturer)
        is_valid_course = (course in lecturer.courses_attached and
                           course in self.courses_in_progress)

        if is_valid_lecturer and is_valid_course:
            # Проверяем, есть ли у лектора словарь для оценок
            if not hasattr(lecturer, 'grades'):
                lecturer.grades = {}
            # Добавляем оценку в словарь лектора
            if course in lecturer.grades:
                lecturer.grades[course].append(grade)
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def get_avg_grade(self):
        """
        Вычисляет среднюю оценку студента за все домашние задания по всем курсам.

        Returns:
            float: Среднее арифметическое всех оценок. Возвращает 0, если оценок нет.
        """
        if not self.grades:
            return 0

        # "Распаковываем" все оценки из словаря в один список
        all_grades = [grade for grades in self.grades.values() for grade in grades]

        return sum(all_grades) / len(all_grades)

    def __str__(self):
        """
        Возвращает строковое представление студента с подробной информацией.

        Формат вывода:
            Имя: {Имя}
            Фамилия: {Фамилия}
            Средняя оценка за домашние задания: {Средний балл}
            Курсы в процессе изучения: {Курс1, Курс2}
            Завершенные курсы: {Курс3, Курс4}

        Returns:
            str: Отформатированная строка с данными о студенте.
                 Если список курсов пуст, поле будет пустым.
        """
        avg_grade = self.get_avg_grade()

        courses_in_progress_str = ', '.join(self.courses_in_progress)
        finished_courses_str = ', '.join(self.finished_courses)

        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка за домашние задания: {avg_grade:.1f}\n"
                f"Курсы в процессе изучения: {courses_in_progress_str}\n"
                f"Завершенные курсы: {finished_courses_str}")

    def __gt__(self, other_student):
        """
        Сравнивает текущего студента с другим по средней оценке.
        Позволяет использовать оператор >
        """
        if not isinstance(other_student, Student):
            return 'Ошибка Сравниваемый объект - не студент'

            # Сравниваем средние оценки
        return self.get_avg_grade() > other_student.get_avg_grade()

    def __lt__(self, other_student):
        """
        Сравнивает текущего студента с другим по средней оценке.
        Позволяет использовать оператор <
        """
        if not isinstance(other_student, Student):
            return 'Ошибка Сравниваемый объект - не студент'

        return self.get_avg_grade() < other_student.get_avg_grade()

    def __eq__(self, other_student):
        """
        Проверяет, равны ли средние оценки двух студентов.
        Позволяет использовать оператор ==
        """
        if not isinstance(other_student, Student):
            return 'Ошибка Сравниваемый объект - не студент'

        return self.get_avg_grade() == other_student.get_avg_grade()