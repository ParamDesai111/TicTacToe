import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title('Tic Tac Toe')
        
        # Initialize game state
        self.board = [''] * 9
        self.current_player = 'X'
        
        # Create buttons
        self.buttons = [tk.Button(self.root, font='Arial 20', width=5, height=2, command=lambda i=i: self.make_move(i)) for i in range(9)]
        for idx, button in enumerate(self.buttons):
            row = idx // 3
            col = idx % 3
            button.grid(row=row, column=col)
            
        self.update_buttons()

    def update_buttons(self):
        for i in range(9):
            self.buttons[i]['text'] = self.board[i]

    def make_move(self, idx):
        if not self.board[idx] and not self.check_winner():
            self.board[idx] = self.current_player
            if self.check_winner():
                messagebox.showinfo("Game Over", f"{self.current_player} Wins!")
                self.reset_game()
                return
            elif '' not in self.board:
                messagebox.showinfo("Game Over", "It's a Draw!")
                self.reset_game()
                return
            
            # Switch players
            self.current_player = 'O' if self.current_player == 'X' else 'X'
        
        self.update_buttons()

    def check_winner(self):
        win_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
            [0, 4, 8], [2, 4, 6]  # diagonals
        ]
        for combo in win_combinations:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] and self.board[combo[0]] != '':
                return True
        return False

    def reset_game(self):
        play_again = messagebox.askyesno("Play Again?", "Would you like to play again?")
        if play_again:
            for i in range(9):
                self.board[i] = ''
            self.current_player = 'X'
            self.update_buttons()
        else:
            self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
