from src.mentor import Mentor


class Lecturer(Mentor):
    """
    Класс, описывающий лектора. Наследует атрибуты от Mentor.
    Лектор может получать оценки от студентов за свои лекции.
    """

    def __init__(self, name, surname):
        """
        Инициализация объекта Lecturer.

        Args:
            name (str): Имя лектора.
            surname (str): Фамилия лектора.
        """
        super().__init__(name, surname)
        self.grades = {}

    def get_avg_grade(self):
        """
        Вычисляет среднюю оценку лектора по всем курсам.

        Returns:
            float: Среднее арифметическое всех оценок.
                   Возвращает 0, если оценок нет.
        """
        if not self.grades:
            return 0
        # Собираем все оценки из словаря в один список
        all_grades = [grade for grades in self.grades.values() for grade in grades]
        return sum(all_grades) / len(all_grades)

    def __str__(self):
        """
        Возвращает строковое представление объекта для печати.

        Формат:
            Имя: {Имя}
            Фамилия: {Фамилия}
            Средняя оценка за лекции: {Средний балл}

        Returns:
            str: Отформатированная строка с информацией о лекторе.
        """
        avg_grade = self.get_avg_grade()
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {avg_grade:.1f}"

    def __gt__(self, other):
        """
        Сравнивает текущего лектора с другим по средней оценке за лекции.
        Позволяет использовать оператор '>' (больше).
        """
        if not isinstance(other, Lecturer):
            return 'Ошибка Сравниваемый объект - не лектор'
        return self.get_avg_grade() > other.get_avg_grade()

    def __lt__(self, other):
        """
        Сравнивает текущего лектора с другим по средней оценке за лекции.
        Позволяет использовать оператор '<' (меньше).
        """
        if not isinstance(other, Lecturer):
            return 'Ошибка Сравниваемый объект - не студент'
        return self.get_avg_grade() < other.get_avg_grade()

    def __eq__(self, other):
        """
        Проверяет, равны ли средние оценки двух лекторов.
        Позволяет использовать оператор '==' (равно).
        """
        if not isinstance(other, Lecturer):
            return 'Ошибка Сравниваемый объект - не студент'
        return self.get_avg_grade() == other.get_avg_grade()