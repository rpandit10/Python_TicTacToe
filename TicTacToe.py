import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")

        self.current_player = "X"
        self.board = [" " for _ in range(9)]

        self.buttons = [tk.Button(root, text=" ", font=("normal", 20), width=6, height=2,
                                  command=lambda idx=i: self.make_move(idx)) for i in range(9)]

        for i in range(3):
            for j in range(3):
                self.buttons[i * 3 + j].grid(row=i, column=j)

        self.start_button = tk.Button(root, text="Start New Game", command=self.reset_board)
        self.start_button.grid(row=3, columnspan=3)

        self.winner_label = tk.Label(root, text="", font=("normal", 16))
        self.winner_label.grid(row=4, columnspan=3)

        self.turn_label = tk.Label(root, text=f"Player {self.current_player}'s turn", font=("normal", 12))
        self.turn_label.grid(row=5, columnspan=3)

    def make_move(self, idx):
        if self.board[idx] == " ":
            self.board[idx] = self.current_player
            self.buttons[idx].config(text=self.current_player)
            if self.check_winner():
                self.winner_label.config(text=f"Player {self.current_player} wins!")
                self.disable_buttons()
            elif " " not in self.board:
                self.winner_label.config(text="It's a draw!")
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
                self.turn_label.config(text=f"Player {self.current_player}'s turn")

    def check_winner(self):
        win_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                            (0, 3, 6), (1, 4, 7), (2, 5, 8),
                            (0, 4, 8), (2, 4, 6)]

        for combo in win_combinations:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != " ":
                return True
        return False

    def reset_board(self):
        self.board = [" " for _ in range(9)]
        for button in self.buttons:
            button.config(text=" ")
            button.config(state="active")
        self.current_player = "X"
        self.winner_label.config(text="")
        self.turn_label.config(text=f"Player {self.current_player}'s turn")

    def disable_buttons(self):
        for button in self.buttons:
            button.config(state="disabled")

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()


