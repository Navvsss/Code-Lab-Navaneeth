import random
import tkinter as tk
from tkinter import messagebox, simpledialog

class MathQuizApp:
    def __init__(self, master):
        self.master = master
        master.title("Math Quiz")

        master.configure(bg='lightblue')
        self.score = 0
        self.difficulty = 0
        self.current_question = 0
        self.correct_answer = 0

        self.label = tk.Label(master, text="WELCOME TO THE MATH QUIZ!", bg='lightblue', fg='black', font=("Arial", 14))
        self.label.pack(pady=10)

        self.start_button = tk.Button(master, text="START", command=self.start_quiz, bg='green', fg='white')
        self.start_button.pack(pady=10)

        self.quit_button = tk.Button(master, text="END", command=master.quit, bg='red', fg='white')
        self.quit_button.pack(pady=10)

    def display_menu(self):
        menu = "DIFFICULTY LEVEL\n1. Easy\n2. Moderate\n3. Advanced"
        self.difficulty = simpledialog.askinteger("Select Difficulty", menu)
        
        if self.difficulty not in [1, 2, 3]:
            messagebox.showerror("Error", "Invalid difficulty level. Please select 1, 2, or 3.")
            return self.display_menu() 
        
        self.start_questions()

    def generate_question(self):
        num1 = self.random_int()
        num2 = self.random_int()
        operation = self.decide_operation()

        if operation == '+':
            self.correct_answer = num1 + num2
        elif operation == '-':
            self.correct_answer = num1 - num2

        return f"{num1} {operation} {num2} = ?"

    def random_int(self):
        if self.difficulty == 1:
            return random.randint(0, 9)
        elif self.difficulty == 2:
            return random.randint(10, 99)
        else:
            return random.randint(100, 999)

    def decide_operation(self):
        return random.choice(['+', '-'])

    def start_quiz(self):
        self.score = 0
        self.current_question = 0
        self.display_menu()

    def start_questions(self):
        if self.current_question < 10:
            question = self.generate_question()
            try:
                user_answer = simpledialog.askinteger("Question", question)
                self.check_answer(user_answer)
            except TypeError:
                messagebox.showinfo("Info", "You cancelled the quiz.")
        else:
            self.end_quiz()

    def check_answer(self, user_answer):
        if user_answer is None:
            messagebox.showinfo("Info", "Question skipped.")
        elif user_answer == self.correct_answer:
            self.score += 10
            messagebox.showinfo("Correct!", f"Correct! You've earned 10 points.\nCurrent Score: {self.score}")
        else:
            messagebox.showinfo("Incorrect", f"Incorrect. The correct answer was {self.correct_answer}.\nKeep trying!")

        self.current_question += 1
        self.start_questions()

    def end_quiz(self):
        messagebox.showinfo("Quiz Finished", f"Your final score is {self.score} out of 100.\n" + self.get_grade())
        if messagebox.askyesno("Play Again?", "Would you like to play again?"):
            self.start_quiz()
        else:
            messagebox.showinfo("Goodbye", "Thanks for playing!")

    def get_grade(self):
        if self.score >= 90:
            return "Grade: A+"
        elif self.score >= 80:
            return "Grade: A"
        elif self.score >= 70:
            return "Grade: B"
        elif self.score >= 60:
            return "Grade: C"
        elif self.score >= 50:
            return "Grade: D"
        else:
            return "Grade: F"

if __name__ == "__main__":
    root = tk.Tk()
    quiz_app = MathQuizApp(root)
    root.mainloop()
