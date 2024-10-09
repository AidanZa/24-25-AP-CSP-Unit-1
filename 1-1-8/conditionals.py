
status = True
grades = [67, 95, 88, 42, 99, 77]
global choice
def show_grades():
    for grade in grades:
        print(grade)

def add_grades():
    new_grade = int(input("Enter your new grade: "))
    grades.append(new_grade)
    print("You added the grade " + str(new_grade) + " to your list")

def show_menu():
    print("Welcome to my grading system.")
    print("Press 1 to view grades")
    print("Press 2 to add grades")
    print("Press 3 to remove grades")
    print("Press 4 to convert to letter grades")
    print("Press 5 to exit the program")
    choice = int(input("Enter your choice: "))

def remove_grades():
    print("The following are your grades.  If you wish to simply delete the last one, enter -1")
    for grade in grades:
        print(grade)
    delete_grade = int(input("Which index would you like to delete?"))
    if delete_grade == -1:
        print("You deleted the grade: " + str(grades.pop()))
    else:
        print("You deleted the grade: " + str(grades.pop(delete_grade)))

def sperate_grades():
    print("You will be completing this part separately")

def finished():
    print("Thank you for using our program.  Have a great day!")
    status = False

while(status):
    show_menu()
    choice = int(input("Enter your choice: "))
    if choice == 1:
        show_grades()
    elif choice ==2:
        add_grades()
    elif choice ==3:
        remove_grades()
    elif choice ==4:
        sperate_grades()
    elif choice ==5:
        finished()
    else:
        print("Please read the menu carefully and select a valid option.")