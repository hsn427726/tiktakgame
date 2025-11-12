import tkinter as tk

def button_click(index):
    if buttons[index]["text"] == "":
        buttons[index]["text"] = current_player
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

# Label to show current player
label = tk.Label(root, text=f"Player {current_player}'s turn", font=("normal", 16))
label.grid(row=3, column=0, columnspan=3)

# Start main loop
root.mainloop()
