import random
import tkinter as tk
from tkinter import messagebox


def load_jokes(file_path):
    with open(file_path, 'r') as file:
        jokes = [line.strip() for line in file if line.strip()]
    return jokes


class JokeApp:
    def __init__(self, root):
        self.root = root
        root.title("Joke Teller")
        root.configure(bg="cyan")  

        self.joke_list = load_jokes('Resources/randomJokes.txt')

        self.label_welcome = tk.Label(
            root,
            text="Welcome! Click 'Get Joke' to start.",
            wraplength=300,
            bg="lightblue",
            font=("Helvetica", 12),
            fg=("black")
        )
        self.label_welcome.pack(pady=10)

        self.button_get_joke = tk.Button(
            root,
            text="Get Joke",
            command=self.show_joke,
            bg="darkviolet",
            fg="white",
            font=("Helvetica", 10, "bold"),
            activebackground="mediumorchid",  
            activeforeground="white"
        )
        self.button_get_joke.pack(pady=10)

        self.button_quit = tk.Button(
            root,
            text="Quit",
            command=root.quit,
            bg="red", 
            fg="white",
            font=("Helvetica", 10, "bold"),
            activebackground="crimson",  
            activeforeground="white"
        )
        self.button_quit.pack(pady=10)

        self.punchline_button = None

    def show_joke(self):
        joke = random.choice(self.joke_list)
        setup, punchline = joke.split('?')

        self.label_welcome.config(text=f"Setup: {setup.strip()}?")

        if self.punchline_button:
            self.punchline_button.destroy()

        self.punchline_button = tk.Button(
            self.root,
            text="Show Punchline",
            command=lambda: self.display_punchline(punchline.strip()),
            bg="#32cd32",
            fg="white",
            font=("Helvetica", 10, "bold"),
            activebackground="#228b22",
            activeforeground="white"
        )
        self.punchline_button.pack(pady=10)

    def display_punchline(self, punchline):
        messagebox.showinfo("Punchline", punchline)


if __name__ == "__main__":
    root = tk.Tk()
    app = JokeApp(root)
    root.mainloop()
