class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(self, Reviewer):
            if course in self.courses_in_progress and lecturer in lecturer.courses_taught:
                if course in lecturer.grades:
                    lecturer.grades[course].append(grade)
                else:
                    lecturer.grades[course] = [grade]
            else:
                return 'Ошибка'
        else:
            return 'Ошибка'

    def rate_hw(self, mentor, course, grade):
        if isinstance(mentor, Reviewer) and course in self.courses_in_progress and course in mentor.courses_attached:
            if course in self.grades:
                self.grades[course].append(grade)
            else:
                self.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        average_grade = self.get_average_homework_grade()
        in_progress_courses = ", ".join(self.courses_in_progress)
        finished_courses = ", ".join(self.finished_courses)
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {average_grade}\nКурсы в процессе изучения: {in_progress_courses}\nЗавершенные курсы: {finished_courses}"

    def get_average_homework_grade(self):
        total_average_grade = 0
        total_courses = 0
        for course in self.courses_in_progress:
            grades = self.grades.get(course, [])
            if grades:
                average_grade = sum(grades) / len(grades)
                total_average_grade += average_grade
                total_courses += 1
        if total_courses > 0:
            return total_average_grade / total_courses
        else:
            return 0

    def __lt__(self, other):
        return self.get_average_homework_grade() < other.get_average_homework_grade()

    def __gt__(self, other):
        return self.get_average_homework_grade() > other.get_average_homework_grade()

    def __eq__(self, other):
        return self.get_average_homework_grade() == other.get_average_homework_grade()

    def __le__(self, other):
        return self.get_average_homework_grade() <= other.get_average_homework_grade()

    def __ge__(self, other):
        return self.get_average_homework_grade() >= other.get_average_homework_grade()

    def __ne__(self, other):
        return self.get_average_homework_grade() != other.get_average_homework_grade()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course].append(grade)
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_taught = []
        self.grades = {}

    def add_course(self, course):
        self.courses_taught.append(course)

    def __str__(self):
        average_grade = self.get_average_lecture_grade()
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {average_grade}"

    def __lt__(self, other):
        return self.get_average_lecture_grade() < other.get_average_lecture_grade()

    def __gt__(self, other):
        return self.get_average_lecture_grade() > other.get_average_lecture_grade()

    def __eq__(self, other):
        return self.get_average_lecture_grade() == other.get_average_lecture_grade()

    def __le__(self, other):
        return self.get_average_lecture_grade() <= other.get_average_lecture_grade()

    def __ge__(self, other):
        return self.get_average_lecture_grade() >= other.get_average_lecture_grade()

    def __ne__(self, other):
        return self.get_average_lecture_grade() != other.get_average_lecture_grade()

    def get_average_lecture_grade(self):
        total_average_grade = 0
        for course in self.courses_taught:
            grades = self.grades.get(course, [])
            if grades:
                average_grade = sum(grades) / len(grades)
                total_average_grade += average_grade
        return total_average_grade / len(self.courses_taught)


lecturer1 = Lecturer('John', 'Doe')
lecturer1.add_course('Python')
lecturer1.grades['Python'] = [8, 9, 7]

lecturer2 = Lecturer('Jane', 'Smith')
lecturer2.add_course('Python')
lecturer2.grades['Python'] = [9, 9, 10]

if lecturer1 < lecturer2:
    print("Lecturer 1 has a lower average lecture grade than Lecturer 2")
elif lecturer1 > lecturer2:
    print("Lecturer 1 has a higher average lecture grade than Lecturer 2")
else:
    print("Lecturer 1 and Lecturer 2 have the same average lecture grade")






class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_reviewed = []

    def add_course(self, course):
        self.courses_reviewed.append(course)

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress.append('Python')

cool_mentor = Mentor('Some', 'Buddy')
cool_mentor.courses_attached.append('Python')

cool_lecturer = Lecturer('John', 'Doe')
cool_lecturer.courses_attached.append('Python')
cool_lecturer.add_course('Python')

cool_reviewer = Reviewer('Jane', 'Smith')
cool_reviewer.courses_attached.append('Python')
cool_reviewer.add_course('Python')

cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 9)
cool_mentor.rate_hw(best_student, 'Python', 8)

best_student.rate_lecturer(cool_lecturer, 'Python', 9)

print(best_student.grades)
print(cool_lecturer.courses_taught)
print(cool_lecturer.grades)
print(cool_reviewer.courses_reviewed)