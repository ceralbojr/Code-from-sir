
# print('Hello Python World')

# x = 'Josh'
# no1 = 90
# no2 = 9
# no3 = 10
# sum = no1 + no2 + no3

# if (sum < 100):
#     print('The sum is lesser than 100')
# elif sum > 100:
#     print('Sum is greater than 100')

# # i = 0
# # while i < 10:
# #     if (i == 4):
# #         print(f'The value of i is {i}')
# #     elif (i <= 6):
# #         print('Hello')
# #     else:
# #         print('Hi')

# #     print(i)
# #     i += 1

# # for i in range(10):
# #     if (i == 4):
# #         print(f'The value of i is {i}')
# #     elif (i <= 6):
# #         print('Hello')
# #     else:
# #         print('Hi')

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
    sum = int(grade1) + int(grade2) + int (grade3) + int(grade4)
    record = f'{name} - {grade1} {grade2} {grade3} {grade4} - {getAve(sum,4)}'
    students.append(record)
    
    i += 1

print()
print()

for s in students:
    print(s)

print()

d0 = input('Enter recrod to view: ')
print(students[int(d0) - 1])

print()

d1 = input('Enter recrod to delete: ')
students.pop(int(d1) - 1)

print()

for s in students:
    print(s)

# def add(a,b):
#     return a + b

# def minus(a,b):
#     return a - b

# def times(a,b):
#     return a * b

# def divide(a,b):
#     return a / b

# print('A - Add')
# print('M - Minus')
# print('T - Times')
# print('D - Divide')

# choice = input('Enter your choice: ')
# no1 = input('Enter no1: ')
# no2 = input('Enter no2: ')
# if choice == 'A':
#     print(add(float(no1), float(no2)))
# elif choice == 'M':
#     print(minus(float(no1), float(no2)))
# elif choice == 'T':
#     print(times(float(no1), float(no2)))
# elif choice == 'D':
#     print(divide(float(no1), float(no2)))
# else:
#     print('Error')





