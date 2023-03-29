from Person import studentNum1

stud = studentNum1

# def getAve(sum, n):
#     return sum / n

students = []
n = int(input('Enter no of students: '))
i = 0
while i < n:
    stud.id_no = int(input('Enter ID Number: '))
    stud.name = input(f'Enter student number {i + 1}: ')
    stud.grade1 = int(input('Enter G1: '))
    stud.grade2 = int(input('Enter G2: '))
    stud.grade3 = int(input('Enter G3: '))
    stud.grade4 = int(input('Enter G4: '))
    # sum = stud.grade1 + stud.grade2 + stud.grade3 + stud.grade4
    record = f'ID Number: {stud.id_no} | {stud.name} - {stud.grade1} {stud.grade2} {stud.grade3} {stud.grade4} - {stud.getAve(stud)}'
    students.append(record)

    i += 1
print()
print()

for s in students:
    print(s)
print()

d0 = input('Enter record to view: ')
print(students[int(d0) - 1])

print()

d1 = input('Enter record to delete: ')
students.pop(int(d1) - 1)

print()

for s in students:
    print(s)