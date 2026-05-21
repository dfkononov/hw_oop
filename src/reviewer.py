from src.mentor import Mentor
from src.student import Student

class Reviewer(Mentor):
    """
    Класс, описывающий проверяющего (рецензента).
    Наследует общие атрибуты от Mentor.
    Специализируется на проверке домашних заданий студентов.
    """

    def __init__(self, name: str, surname: str):
        """
        Инициализирует нового проверяющего.

        Args:
            name (str): Имя проверяющего.
            surname (str): Фамилия проверяющего.
        """
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        """
        Ставит оценку студенту за домашнее задание по курсу.

        Оценка ставится только если:
        1. Объект является экземпляром класса Student.
        2. Курс закреплен за данным проверяющим.
        3. Студент изучает данный курс в данный момент.

        Args:
            student (Student): Объект студента, которому ставится оценка.
            course (str): Название курса.
            grade (int | float): Оценка за домашнее задание.

        Returns:
            str: Возвращает строку 'Ошибка', если условия для выставления оценки не выполнены.
                 Возвращает None, если оценка успешно выставлена.
        """
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        """
        Возвращает строковое представление проверяющего для вывода на экран.

        Формат:
            Имя: {Имя}
            Фамилия: {Фамилия}

        Returns:
            str: Отформатированная строка с именем и фамилией.
        """
        return f"Имя: {self.name}\nФамилия: {self.surname}"