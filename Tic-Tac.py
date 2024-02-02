import tkinter as tk
import tkinter.messagebox

class TicTacToeGame:
    def __init__(self, root):
        self.root = root
        
        self.root.title("Tic-Tac-Toe")

        self.x_color = "blue"  
        self.o_color = "green" 
        self.win_color = "red" 

        #Buttons
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                
                self.buttons[i][j] = tk.Button(root, text="", font=('normal', 40), width=5, height=2,
                                               command=lambda i=i, j=j: self.on_cell_click(i, j))
                self.buttons[i][j].grid(row=i, column=j)

        
        self.score_x = 0
        self.score_o = 0
        
        self.scoreboard = tk.Label(root, text="X: 0 - O: 0", font=('normal', 20))
        self.scoreboard.grid(row=3, column=0, columnspan=3)

        
        self.player = "X"
        self.game_over = False

    def on_cell_click(self, row, col):
        
        if self.buttons[row][col]['text'] == "" and not self.game_over:
            self.buttons[row][col]['text'] = self.player
            
            self.buttons[row][col]['fg'] = self.x_color if self.player == "X" else self.o_color

          
            if self.check_winner(self.player):
                tkinter.messagebox.showinfo("Tic-Tac-Toe", f"Player {self.player} RBAAA7!")
                self.update_score(self.player)
                self.reset_game()
            elif self.check_draw():
                
                tkinter.messagebox.showinfo("Tic-Tac-Toe", "It's a Draw!")
                self.reset_game()
            else:
                
                self.player = "O" if self.player == "X" else "X"

    def check_winner(self, p):
        
        for i in range(3):
            if self.buttons[i][0]['text'] == self.buttons[i][1]['text'] == self.buttons[i][2]['text'] == p or \
               self.buttons[0][i]['text'] == self.buttons[1][i]['text'] == self.buttons[2][i]['text'] == p:
                # l9ina cells dial rabe7
                self.highlight_winner([(i, j) for j in range(3)])
                return True
        if self.buttons[0][0]['text'] == self.buttons[1][1]['text'] == self.buttons[2][2]['text'] == p or \
           self.buttons[0][2]['text'] == self.buttons[1][1]['text'] == self.buttons[2][0]['text'] == p:
            self.highlight_winner([(i, i) for i in range(3)] if self.buttons[0][0]['text'] == p else [(i, 2-i) for i in range(3)])
            return True
        return False

    def check_draw(self):
        
        for row in self.buttons:
            for button in row:
                if button['text'] == "":
                    return False
        return True

    def reset_game(self):
        
        self.player = "X"
        self.game_over = False
        for row in self.buttons:
            for button in row:
                button['text'] = ""
                button['fg'] = 'black'

    def update_score(self, player):
       
        if player == "X":
            self.score_x += 1
        else:
            self.score_o += 1
        self.scoreboard['text'] = f"X: {self.score_x} - O: {self.score_o}"

    def highlight_winner(self, cells):
        for row, col in cells:
            self.buttons[row][col]['fg'] = self.win_color

root = tk.Tk()
game = TicTacToeGame(root)
root.mainloop()
