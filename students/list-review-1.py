students = []
n = int(input("Kiritmoqchi talabalar soni: "))
for i in range(n):
    print(f"{i+1}-talaba ma'lumotlari: ")
    name = input("Ismni kiriting: ")
    surname=  input("Familiyani kiriting: ")
    yil = input("Tug'ilgan sanani kiriting: ")
    student = {}
    student["name"]=name
    student["surname"]=surname
    student["yil"] = yil
    students.append(student)
for student in students:
    print(f"Ism: {student['name']}, "
          f"Familiya: {student['surname']}, "
          f"Tug'ilgan yil: {student['yil']}")