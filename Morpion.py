import tkinter
from tkinter import messagebox

def on_button_click(row, col):
    global current_player, board

    if not board[row][col]:
        board[row][col] = current_player
        update_button(row, col)

        if check_winner(row, col):
            messagebox.showinfo("Results", f"Player {current_player} wins !")
            restart_game()
        elif check_draw():
            messagebox.showinfo("Results", "It's a draw !'")
            restart_game()
        else:
            toggle_player()

def update_button(row, col):
    button = buttons[row][col]
    button.config(text=current_player, state=tkinter.DISABLED)

def toggle_player():
    global current_player
    current_player = 'O' if current_player == 'X' else 'X'

def check_winner(row,col):
    return check_row(row) or check_column(col) or check_diagonals(row, col)

def check_row(row):
    return all(board[row][i] == current_player for i in range(3))

def check_column(col):
    return all(board[i][col] == current_player for i in range(3))

def check_diagonals(row, col):
    if row == col or row + col == 2:
        return all(board[i][i] == current_player for i in range(3)) or \
            all(board[i][2 - i] == current_player for i in range(3))
    return False

def check_draw():
    return all(board[i][j] for i in range (3) for j in range (3))

def restart_game():
    global current_player, board
    current_player = 'X'
    board = [['' for i in range(3)] for j in range(3)]

    for i in range(3):
        for j in range(3):
            buttons[i][j].config(text="", state=tkinter.NORMAL)

if __name__ == '__main__':
    current_player = 'X'
    board = [['' for _ in range(3)] for _ in range(3)]

    win = tkinter.Tk()
    win.title('Morpion')
    win.geometry('250x325')

    buttons = [[None, None, None] for _ in range(3)]

    for i in range(3):
        frame = tkinter.Frame(win, height=200, width=600)
        for j in range(3):
            button = tkinter.Button(frame, text='', width=10, height=5, command=lambda row=i, col=j: on_button_click(row,col))
            button.pack(side=tkinter.LEFT)
            buttons[i][j] = button
        frame.pack(side=tkinter.TOP)

    frame1 = tkinter.Frame(win, height=200, width=600)
    restart_button = tkinter.Button(frame1, text="Restart Game", command=restart_game)
    restart_button.pack(pady=5, padx=10)

    quit_button = tkinter.Button(frame1, text="Quit", command=win.quit)
    quit_button.pack()

    frame1.pack()

    win.mainloop()