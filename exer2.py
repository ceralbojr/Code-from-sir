def getAve(sum, n):
    return sum / n

students = []
n = input('Enter no of students: ')
i = 0

while i < int(n):
    name = input(f'Enter student number {i + 1}: ')
    grade1 = input('Enter G1: ')
    grade2 = input('Enter G2: ')
    grade3 = input('Enter G3: ')
    grade4 = input('Enter G4: ')
    sum = int(grade1) + int(grade2) + int(grade3) + int(grade4)
    record = f'{name} - {grade1} {grade2} {grade3} {grade4} - {getAve(sum, 4)}'
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