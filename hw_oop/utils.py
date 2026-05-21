from lecturer import Lecturer
from student import Student

def avg_grade_all_lecturers(lecturers_list, course):
    """
    Считает среднюю оценку всех лекторов за конкретный курс.
    """
    total_sum = 0
    grades_count = 0

    for lecturer in lecturers_list:
        if isinstance(lecturer, Lecturer) and course in lecturer.grades:
            total_sum += sum(lecturer.grades[course])
            grades_count += len(lecturer.grades[course])

    if grades_count == 0:
        return 0.0

    return total_sum / grades_count


def avg_grade_all_students(students_list, course):
    """
    Считает среднюю оценку всех студентов за конкретный курс.
    """
    total_sum = 0
    grades_count = 0

    for student in students_list:
        if isinstance(student, Student) and course in student.grades:
            total_sum += sum(student.grades[course])
            grades_count += len(student.grades[course])

    if grades_count == 0:
        return 0.0

    return total_sum / grades_count