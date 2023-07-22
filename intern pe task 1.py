#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tkinter as tk
from tkinter import messagebox


# In[2]:


board = [' ' for _ in range(9)]


# In[3]:


def display_board():
    for i in range(9):
        buttons[i]['text'] = board[i]


# In[4]:


def check_win(player):
    win_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]               # Diagonals
    ]
    for combination in win_combinations:
        if all(board[i] == player for i in combination):
            return True
    return False


# In[5]:


def button_click(position):
    global current_player
    if board[position] == ' ':
        board[position] = current_player
        buttons[position]['text'] = current_player

        if check_win(current_player):
            messagebox.showinfo('Game Over', 'Player ' + current_player + ' wins!')
            reset_game()
        elif ' ' not in board:
            messagebox.showinfo('Game Over', "It's a tie!")
            reset_game()
        else:
            current_player = 'O' if current_player == 'X' else 'X'
    else:
        messagebox.showwarning('Invalid Move', 'That position is already taken. Try again.')


# In[6]:


root = tk.Tk()
root.title('Tic-Tac-Toe')

buttons = []
for i in range(9):
    button = tk.Button(root, text=' ', font=('Arial', 20), width=6, height=3,
                       command=lambda pos=i: button_click(pos))
    button.grid(row=i // 3, column=i % 3)
    buttons.append(button)




# In[7]:


# Start the game
current_player = 'X'
display_board()


# In[8]:


# Run the GUI event loop
root.mainloop()


# In[ ]:




