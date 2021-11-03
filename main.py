import student

std_1 = student.Student('Foday', 25, 'Form 7')
std_2 = student.Student('Sireh', 20, 'Form 5')
std_3 = student.Student('Fatou', 17, 'Form 3')

students = [std_1, std_2, std_3]

fout = open('student_details.txt', 'w')

for stud in students:
    fout.write(f'{stud.details()}================ \n')
    print(stud.details())


fout.close()