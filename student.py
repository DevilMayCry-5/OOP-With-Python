class Student:
    school = 'Marina International School'

    def __init__(self, name, age, grade):
        self.student_name = name
        self.student_age = age
        self.student_grade = grade

    def details(self):
        '''gets details of student'''
        return f'Name: {self.student_name:>6} \nAge: {self.student_age:>4} \nClass: {self.student_grade}\n'