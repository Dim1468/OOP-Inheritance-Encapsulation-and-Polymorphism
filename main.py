class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

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

    def add_course(self, course):
        self.courses_taught.append(course)

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_reviewed = []

    def add_course(self, course):
        self.courses_reviewed.append(course)

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

print(best_student.grades)
print(cool_lecturer.courses_taught)
print(cool_reviewer.courses_reviewed)