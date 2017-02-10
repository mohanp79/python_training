from statistics import mean as m

admins = {'admin':'admin', 'grader':'grader'}

students = {'Ben':[23,21,12],
            'Jenny': [17,19,25],
            'Jessie': [21,22,24]}



def enterGrades():
    nameToEnter = input('Student Name: ')
    gradeToEnter = input('Grade: ')

    if nameToEnter in students:
        print('Adding Grade...')
        students[nameToEnter] .append(gradeToEnter)
    else:
        print('Student does not exist')
    print(students)

def removeStudent():
    nameToRemove = input('What student to remove?: ')
    if nameToRemove in students:
        print('Removing Student . . .')
    else:
        print('Student does not exist')
    print(students)

def averageGrades():
    for eachStudent in students:
        gradeList = students[eachStudent]
        avgGrade = m(gradeList)

        print(eachStudent, 'has an average grade of:', avgGrade)


def main():
    print("""
    Welcome to Grading System

    [1] - Enter Grades
    [2] - Remove Student
    [3] - Student Average Grades
    [4] - Exit
    """)

    action = input('What would you like to do today? (Enter a number)')

    if action == '1':
        enterGrades()
    elif action == '2':
        removeStudent()
    elif action == '3':
        averageGrades()
    elif action == '4':
        exit()
    else:
        print('Please enter 1 / 2 / 3 / 4')


login = input('Username: ')
password = input('Password: ')

if login in admins:
    if admins[login] == password:
        print('Welcome,', login)
        while True:
            main()
    else:
        print('Invalid password, will detonate in 5 seconds!')
else:
    print('Invalid username, FBI is on your way to get you!')

while True:
    main()