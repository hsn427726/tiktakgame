import tkinter as tk

# Setup main window
root = tk.Tk()
root.title("Tic-Tac-Toe")

# Create buttons
buttons = [tk.Button(root, text="", font=("normal", 25), width=6, height=2) for _ in range(9)]

# Place buttons in grid
for i, button in enumerate(buttons):
    button.grid(row=i // 3, column=i % 3)

# Start main loop
root.mainloop()
