import tkinter as tk
from tkinter import messagebox
import random

class RockPaperScissorsApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock~Paper~Scissors Game")
        self.user_score = 0
        self.computer_score = 0
        self.create_widgets()

    def create_widgets(self):
    
        self.frame = tk.Frame(self.root, bg="#f0f0f0", padx=20, pady=20)
        self.frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        self.title_label = tk.Label(self.frame, text="ROCK=PAPER=SCISSORS", font=('Roboto', 18, 'bold'), bg="#f0f0f0")
        self.title_label.pack(pady=10)

        self.instructions_label = tk.Label(self.frame, text="Choose Rock, Paper, or Scissors:", font=('Arial', 14), bg="#f0f0f0")
        self.instructions_label.pack(pady=10)

        button_style = {'bg': '#4CAF50', 'fg': 'white', 'font': ('Arial', 12, 'bold'), 'bd': 2, 'relief': 'raised'}
        self.rock_button = tk.Button(self.frame, text="Rock", command=lambda: self.play_game("Rock"), **button_style)
        self.rock_button.pack(fill=tk.X, padx=5, pady=5)

        self.paper_button = tk.Button(self.frame, text="Paper", command=lambda: self.play_game("Paper"), **button_style)
        self.paper_button.pack(fill=tk.X, padx=5, pady=5)

        self.scissors_button = tk.Button(self.frame, text="Scissors", command=lambda: self.play_game("Scissors"), **button_style)
        self.scissors_button.pack(fill=tk.X, padx=5, pady=5)

        self.user_score_label = tk.Label(self.frame, text=f"Your Score: {self.user_score}", font=('Arial', 12), bg="#f0f0f0")
        self.user_score_label.pack(pady=5)

        self.computer_score_label = tk.Label(self.frame, text=f"Computer Score: {self.computer_score}", font=('Arial', 12), bg="#f0f0f0")
        self.computer_score_label.pack(pady=5)

    def play_game(self, user_choice):
        choices = ["Rock", "Paper", "Scissors"]
        computer_choice = random.choice(choices)
        
        result = self.determine_winner(user_choice, computer_choice)
        self.update_scores(result)

        messagebox.showinfo("Result", f"Your choice: {user_choice}\nComputer's choice: {computer_choice}\nResult: {result}")
        self.ask_play_again()

    def determine_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return "It's a Tie!"

        if (user_choice == "Rock" and computer_choice == "Scissors") or \
           (user_choice == "Scissors" and computer_choice == "Paper") or \
           (user_choice == "Paper" and computer_choice == "Rock"):
            return "You Win!"

        return "You Lose!"

    def update_scores(self, result):
        if result == "You Win!":
            self.user_score += 1
        elif result == "You Lose and Try Again!":
            self.computer_score += 1
        
        self.user_score_label.config(text=f"Your Score : {self.user_score}")
        self.computer_score_label.config(text=f"Computer Score : {self.computer_score}")

    def ask_play_again(self):
        play_again = messagebox.askyesno("Play Again?", "Do you want to play another round?")
        if play_again:
            return
        else:
            self.root.quit()

if __name__ == "__main__":
    root = tk.Tk()
    app = RockPaperScissorsApp(root)
    root.mainloop()
