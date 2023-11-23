import tkinter as tk
from tkinter import messagebox

# Backend Game Logic
def check_winner(board, player):
    for row in board:
        if all([cell == player for cell in row]):
            return True
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True
    return False

def check_draw(board):
    return all([cell in ['X', 'O'] for row in board for cell in row])

def minimax(board, depth, is_maximizing):
    if check_winner(board, 'X'):
        return -10 + depth
    if check_winner(board, 'O'):
        return 10 - depth
    if check_draw(board):
        return 0

    if is_maximizing:
        max_eval = float('-inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == '':
                    board[i][j] = 'O'
                    eval = minimax(board, depth + 1, False)
                    board[i][j] = ''
                    max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == '':
                    board[i][j] = 'X'
                    eval = minimax(board, depth + 1, True)
                    board[i][j] = ''
                    min_eval = min(min_eval, eval)
        return min_eval

def best_move(board):
    best_score = float('-inf')
    move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == '':
                board[i][j] = 'O'
                score = minimax(board, 0, False)
                board[i][j] = ''
                if score > best_score:
                    best_score = score
                    move = (i, j)
    return move

# GUI using tkinter
class TicTacToeApp:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title('Tic Tac Toe')
        self.board = [['' for _ in range(3)] for _ in range(3)]
        self.buttons = [[tk.Button(self.window, text='', font='Arial 20', width=5, height=2, command=lambda i=i, j=j: self.make_move(i, j)) for j in range(3)] for i in range(3)]

        for i in range(3):
            for j in range(3):
                self.buttons[i][j].grid(row=i, column=j)

    def make_move(self, i, j):
        if not self.board[i][j]:
            self.board[i][j] = 'X'
            self.buttons[i][j]['text'] = 'X'
            if check_winner(self.board, 'X'):
                self.end_game('X Wins!')
                return
            elif check_draw(self.board):
                self.end_game('It\'s a Draw!')
                return
            move = best_move(self.board)
            if move:
                self.board[move[0]][move[1]] = 'O'
                self.buttons[move[0]][move[1]]['text'] = 'O'
                if check_winner(self.board, 'O'):
                    self.end_game('O Wins!')
                elif check_draw(self.board):
                    self.end_game('It\'s a Draw!')

    def end_game(self, message):
        messagebox.showinfo('Game Over', message)
        response = messagebox.askyesno('Play Again', 'Do you want to play again?')
        if response:
            for i in range(3):
                for j in range(3):
                    self.board[i][j] = ''
                    self.buttons[i][j]['text'] = ''
        else:
            self.window.quit()

    def run(self):
        self.window.mainloop()

# Run the app
if __name__ == '__main__':
    app = TicTacToeApp()
    app.run()
