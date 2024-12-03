import csv
import tkinter as tk
from tkinter import messagebox, simpledialog

class Student:
    def __init__(self, code, name, marks):
        self.code = code
        self.name = name
        self.coursework = marks[:3]
        self.exam = marks[3]

    def total_coursework(self):
        return sum(self.coursework)

    def overall_percentage(self):
        return (self.total_coursework() + self.exam) / 160 * 100

    def grade(self):
        perc = self.overall_percentage()
        if perc >= 70:
            return 'A'
        elif perc >= 60:
            return 'B'
        elif perc >= 50:
            return 'C'
        elif perc >= 40:
            return 'D'
        else:
            return 'F'

def load_students(file):
    students = []
    with open(file, 'r') as f:
        reader = csv.reader(f)
        next(reader)  # Skip header
        for row in reader:
            code = int(row[0])
            name = row[1]
            marks = list(map(int, row[2:]))
            students.append(Student(code, name, marks))
    return students

class App:
    def __init__(self, root, students):
        self.root = root
        self.students = students
        self.root.title("RECORDS OF STUDENTS")
        self.bg = "lightblue"
        self.root.configure(bg=self.bg)

        self.menu = tk.Frame(root, bg=self.bg)
        self.menu.pack(pady=20)

        # Create buttons
        for text, command in [("SHOW ALL", self.view_all), 
                              ("PREVIEW STUDENT SEPERATE", self.view_student), 
                              ("HIGHEST SCORING", self.top_student), 
                              ("LOWEST SCORING", self.bottom_student)]:
            tk.Button(self.menu, text=text, command=command, bg="white", fg="magenta").pack(side=tk.LEFT, padx=10)

        # Create a frame for Text widget and Scrollbar
        self.frame = tk.Frame(root)
        self.frame.pack(pady=20)

        self.output = tk.Text(self.frame, width=80, height=20, bg=self.bg)
        self.output.pack(side=tk.LEFT)

        self.scroll = tk.Scrollbar(self.frame, command=self.output.yview)
        self.scroll.pack(side=tk.RIGHT, fill=tk.Y)

        self.output.config(yscrollcommand=self.scroll.set)

    def display_student_info(self, student):
        self.output.delete(1.0, tk.END)
        self.output.insert(tk.END, f"NAME: {student.name}\n"
                                    f"STUDENT CODE: {student.code}\n"
                                    f"TOTAL COURSE WORK: {student.total_coursework()}\n"
                                    f"EXAM MARK: {student.exam}\n"
                                    f"OVERALL PERCENTAGE: {student.overall_percentage():.2f}%\n"
                                    f"GRADE: {student.grade()}\n")
        self.update_scrollbar()

    def view_all(self):
        self.output.delete(1.0, tk.END)
        for s in self.students:
            self.output.insert(tk.END, f"NAME: {s.name}\n"
                                        f"STUDENT CODE: {s.code}\n"
                                        f"TOTAL COURSE WORK: {s.total_coursework()}\n"
                                        f"EXAM MARK: {s.exam}\n"
                                        f"OVERALL PERCENTAGE: {s.overall_percentage():.2f}%\n"
                                        f"GRADE: {s.grade()}\n"
                                        f"{'-'*40}\n")  # Separator line between students
        self.update_scrollbar()

    def view_student(self):
        code = simpledialog.askinteger("CODE INPUT", "ENTER THE STUDENT CODE", parent=self.root)
        if code is not None:
            student = next((s for s in self.students if s.code == code), None)
            if student:
                self.display_student_info(student)
            else:
                messagebox.showinfo("ERROR", "STUDENT CODE ENTERED IS WRONG, PLEASE CHECK AND TRY AGAIN.")

    def top_student(self):
        top = max(self.students, key=lambda s: s.total_coursework() + s.exam)
        self.display_student_info(top)

    def bottom_student(self):
        bottom = min(self.students, key=lambda s: s.total_coursework() + s.exam)
        self.display_student_info(bottom)

    def update_scrollbar(self):
        self.output.config(yscrollcommand=self.scroll.set)

if __name__ == "__main__":
        students = load_students('resources/studentMarks.txt')
        root = tk.Tk()
        app = App(root, students)
        root.mainloop()