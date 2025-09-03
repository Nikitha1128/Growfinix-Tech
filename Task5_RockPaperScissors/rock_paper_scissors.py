import tkinter as tk
import random

def play(choice):
    options = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(options)
    
    if choice == computer_choice:
        result.set(f"Both chose {choice}. It's a Tie!")
    elif (choice == "Rock" and computer_choice == "Scissors") or \
         (choice == "Paper" and computer_choice == "Rock") or \
         (choice == "Scissors" and computer_choice == "Paper"):
        result.set(f"You chose {choice}, Computer chose {computer_choice}. You Win! 🎉")
    else:
        result.set(f"You chose {choice}, Computer chose {computer_choice}. You Lose! 😢")

def reset():
    result.set("Choose Rock, Paper, or Scissors to play!")

# Tkinter GUI setup
root = tk.Tk()
root.title("Rock Paper Scissors Game")
root.geometry("400x300")

tk.Label(root, text="Rock Paper Scissors", font=("Arial", 16, "bold")).pack(pady=10)

result = tk.StringVar()
result.set("Choose Rock, Paper, or Scissors to play!")

tk.Label(root, textvariable=result, wraplength=350, font=("Arial", 12)).pack(pady=20)

frame = tk.Frame(root)
frame.pack()

tk.Button(frame, text="Rock", width=10, command=lambda: play("Rock")).grid(row=0, column=0, padx=10)
tk.Button(frame, text="Paper", width=10, command=lambda: play("Paper")).grid(row=0, column=1, padx=10)
tk.Button(frame, text="Scissors", width=10, command=lambda: play("Scissors")).grid(row=0, column=2, padx=10)

tk.Button(root, text="Reset", width=15, command=reset).pack(pady=15)

root.mainloop()
