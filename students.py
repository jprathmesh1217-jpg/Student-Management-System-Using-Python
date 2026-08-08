class Student:
    all_students = [] 


    def __init__(self,name,roll_number,marks):
        self.name=name
        self.roll_number = roll_number 
        self.marks = marks 
    def update_marks(self,new_marks):
        self.marks = new_marks
        print(f"Marks updated successfully for {self.name}.")
    def show_details(self):
         print(f"****** Student Details: ******") 
         print(f"Name: {self.name}")
         print(f"Roll Number: {self.roll_number}")
         print(f"Marks: {self.marks}")

    
    @classmethod
    def find_student_by_roll_number(cls,roll_number):
        for student in cls.all_students:
            if student.roll_number == roll_number:
                return student
        return None

    @classmethod
    def add_student(cls):
        name =input("Enter Student Name:")
        roll_number = input("Enter Student Roll Number: ")
        marks = int(input("Enter Student Marks: "))
        student = cls(name,roll_number,marks) 
        cls.all_students.append(student)
        print(f"Student {name} added successfully.")

    @classmethod 
    def update_marks(cls): 
        roll_number = input("Enter Student Roll Number to update marks:  ")
        Student = cls.find_student_by_roll_number(roll_number) 
        if Student:
            new_marks = int(input(f"Enter New Marks: "))
            Student.update_marks(new_marks)
            print(f"Marks for{Student.name} update successfully!")
        else:
            print("Student Not Found.")
    @classmethod
    def show_all_students(cls):
        if not cls.all_students:
            print("No Students Found.")
            return 
        for student in cls.all_students:
            student.show_details()