students_list = []
for number in range(1, 6):
    student = {
        'name': input("Nome do Estudante " + str(number) + ": "),
        'grade': input("Nota do Estudante " + str(number) + ": ")
    }
    students_list.append(student)
print(students_list)
max_grade = 0
max_name = ""
for student in students_list:
    if float(student['grade']) > max_grade:
        max_grade = float(student['grade'])
        max_name = student['name']
print("Estudante com a maior nota:\nNome: " + max_name + "\nNota: " + str(max_grade))
