import tkinter as tk
from tkinter import messagebox

def check_winner():
    global winner
    # Define winning combinations
    for combo in [
        [0,1,2], [3,4,5], [6,7,8],  # rows
        [0,3,6], [1,4,7], [2,5,8],  # columns
        [0,4,8], [2,4,6]            # diagonals
    ]:
        if buttons[combo[0]]["text"] == buttons[combo[1]]["text"] == buttons[combo[2]]["text"] != "":
            # Highlight winning buttons
            for i in combo:
                buttons[i].config(bg="green")
            messagebox.showinfo("Tic-Tac-Toe", f"Player {buttons[combo[0]]['text']} wins!")
            winner = True
            return

    # Check for draw
    if all(button["text"] != "" for button in buttons) and not winner:
        for button in buttons:
            button.config(bg="red")
        messagebox.showinfo("Tic-Tac-Toe", "It's a draw!")
        winner = True

def button_click(index):
    if buttons[index]["text"] == "" and not winner:
        buttons[index]["text"] = current_player
        check_winner()
        if not winner:
            toggle_player()

def toggle_player():
    global current_player
    current_player = "O" if current_player == "X" else "X"
    label.config(text=f"Player {current_player}'s turn")

# Setup main window
root = tk.Tk()
root.title("Tic-Tac-Toe")

# Create buttons
buttons = [tk.Button(root, text="", font=("normal", 25), width=6, height=2, 
                     command=lambda i=i: button_click(i)) for i in range(9)]

# Place buttons in grid
for i, button in enumerate(buttons):
    button.grid(row=i // 3, column=i % 3)

# Initialize game state
current_player = "X"
winner = False

# Label to show current player
label = tk.Label(root, text=f"Player {current_player}'s turn", font=("normal", 16))
label.grid(row=3, column=0, columnspan=3)

# Start main loop
root.mainloop()
