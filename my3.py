class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lt(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer)  and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer. grade_st:
                 lecturer.grade_st[course] += [grade]
            else:
                 lecturer.grade_st[course] = [grade]
        else:
            return 'Ошибка'

    def calc_average(self):
        self.average_grade = round(sum(sum(self.grades.values(),[])) / len(sum(self.grades.values(),[])), 1)
        return self.average_grade

    def __str__(self):
        return (f'Имя: {self.name}\n'
        f'Фамилия: { self.surname}\n'
        f'Средняя оценка за домашнее задание: {self.calc_average()}\n'
        f'Курсы в процессе изучения: {", ".join( self.courses_in_progress)}\n'
        f'Завершенные курсы: {", ".join(self.finished_courses)}\n')

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Невозможно сравнить')
            return
        return self.average_grade < other.average_grade

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grade_st = {}

    def lt_average(self):
        self.av_gr_lt = round(sum(sum(self.grade_st.values(),[])) / len(sum(self.grade_st.values(),[])), 1)
        return self.av_gr_lt

    def __str__(self):
        text = f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции: {self.lt_average()}'
        return text

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Невозможно сравнить')
            return
        return self.av_gr_lt < other.av_gr_lt

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                 student.grades[course] += [grade]
            else:
                 student.grades[course] = [grade]
        else:
             return 'Ошибка'

    def __str__(self):
        text = f'Имя: {self.name} \nФамилия: {self.surname}'
        return text


some_lecturer = Lecturer('Some', 'Buddy')
some1_lecturer = Lecturer('John', 'Wick')
some_lecturer.courses_attached += ['Python']
some1_lecturer.courses_attached += ['Python', 'Git']

some_student = Student('Ruoy', 'Eman', 'your_gender')
some1_student = Student('Ivan', 'Kein', 'man')
some_student.courses_in_progress += ['Python','Git']
some_student.finished_courses += ['Введение в программирование']
some1_student.courses_in_progress += ['Python']
some1_student.finished_courses += ['Введение в программирование']

some_student.rate_lt(some_lecturer, 'Python', 9)
some_student.rate_lt(some1_lecturer, 'Python', 10)
some_student.rate_lt(some1_lecturer, 'Python', 8)
some1_student.rate_lt(some_lecturer, 'Python', 10)
some1_student.rate_lt(some1_lecturer, 'Python', 7)

some_reviewer = Reviewer('Some', 'Buddy')
some_reviewer.courses_attached += ['Python']
some1_reviewer = Reviewer('Sergey', 'Ivanov')
some1_reviewer.courses_attached += ['Python', 'Git']

some_reviewer.rate_hw(some_student, 'Python', 9)
some_reviewer.rate_hw(some1_student, 'Python', 8)
some_reviewer.rate_hw(some1_student, 'Python', 10)
some1_reviewer.rate_hw(some_student, 'Python', 8)
some1_reviewer.rate_hw(some1_student, 'Python', 10)

some_student.calc_average()
some1_student.calc_average()
print(some_student < some1_student)
print(some_student)
print(some1_student)

some_lecturer.lt_average()
some1_lecturer.lt_average()
print(some_lecturer < some1_lecturer)
print(some_lecturer)
print(some1_lecturer)

print(some_reviewer)
print(some1_reviewer)


student_lt =[some_student, some1_student]
def mid_grade_st(student_lt, course):
    sum = 0
    count = 0
    for person in student_lt:
        for a in person.grades[course]:
            sum += a
            count += 1
            return sum/count

lecturer_lt =[some_lecturer, some1_lecturer]
def mid_grade_lt(lecturer_lt, course):
    sum = 0
    count = 0
    for person in lecturer_lt:
        for a in person.grade_st[course]:
            sum += a
            count += 1
            return sum/count

print( mid_grade_st(student_lt, 'Python'))
print(mid_grade_lt(lecturer_lt, 'Python'))
