from students import Student

def menu():
    while True:
        print("\n============ Student Management System ==========")
        print("1. Add Student") 
        print("2. Upadate marks")
        print("3. Show All Students")
        print("4. Exit")

        choice = int(input("Enter your option(1-4):"))
        if choice==1:
            Student.add_student()
        elif choice==2:
            Student.update_marks() 
        elif choice ==3:
            Student.show_all_students()
        elif choice ==41:
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")
            Student.show_all_students()
        
if __name__ == "__main__":
    menu()   