import tkinter as tk
import tkinter.messagebox


class TTT:
    def __init__(self):
        self.main_window = tk.Tk()
        self.main_window.title('TicTacToe')

        # counts clicks
        self.counter = 0

        # creates 3d list relating to buttons
        self.TTT_board = [['', '', ''],
                          ['', '', ''],
                          ['', '', '']]

        # 3 buttons are put into a frame, creating a 3x3 ttt board. Buttons put into seperate frame
        self.Row1 = tk.Frame()
        self.Row2 = tk.Frame()
        self.Row3 = tk.Frame()
        self.Button_frame = tk.Frame()

        self.button1_1 = tk.Button(self.Row1, text='', disabledforeground="black", width=2, height=1,
                                   command=lambda: self.button_clicked(self, button=self.button1_1, row=1, col=1))
        self.button1_2 = tk.Button(self.Row1, text='', disabledforeground="black", width=2, height=1,
                                   command=lambda: self.button_clicked(self, button=self.button1_2, row=1, col=2))
        self.button1_3 = tk.Button(self.Row1, text='', disabledforeground="black", width=2, height=1,
                                   command=lambda: self.button_clicked(self, button=self.button1_3, row=1, col=3))
        self.button1_1.pack(side='left', padx=5, pady=5)
        self.button1_2.pack(side='left', padx=5, pady=5)
        self.button1_3.pack(side='left', padx=5, pady=5)

        self.button2_1 = tk.Button(self.Row2, text='', disabledforeground="black", width=2, height=1,
                                   command=lambda: self.button_clicked(self, button=self.button2_1, row=2, col=1))
        self.button2_2 = tk.Button(self.Row2, text='', disabledforeground="black", width=2, height=1,
                                   command=lambda: self.button_clicked(self, button=self.button2_2, row=2, col=2))
        self.button2_3 = tk.Button(self.Row2, text='', disabledforeground="black", width=2, height=1,
                                   command=lambda: self.button_clicked(self, button=self.button2_3, row=2, col=3))
        self.button2_1.pack(side='left', padx=5, pady=5)
        self.button2_2.pack(side='left', padx=5, pady=5)
        self.button2_3.pack(side='left', padx=5, pady=5)

        self.button3_1 = tk.Button(self.Row3, text='', disabledforeground="black", width=2, height=1,
                                   command=lambda: self.button_clicked(self, button=self.button3_1, row=3, col=1))
        self.button3_2 = tk.Button(self.Row3, text='', disabledforeground="black", width=2, height=1,
                                   command=lambda: self.button_clicked(self, button=self.button3_2, row=3, col=2))
        self.button3_3 = tk.Button(self.Row3, text='', disabledforeground="black", width=2, height=1,
                                   command=lambda: self.button_clicked(self, button=self.button3_3, row=3, col=3))
        self.button3_1.pack(side='left', padx=5, pady=5)
        self.button3_2.pack(side='left', padx=5, pady=5)
        self.button3_3.pack(side='left', padx=5, pady=5)

        self.reset_button = tk.Button(self.Button_frame, text='Reset', command=self.reset)
        self.reset_button.pack(pady=5)

        self.Row1.pack()
        self.Row2.pack()
        self.Row3.pack()
        self.Button_frame.pack()
        tk.mainloop()

    def reset(self):
        self.button1_1['text'] = ''
        self.button1_2['text'] = ''
        self.button1_3['text'] = ''
        self.button2_1['text'] = ''
        self.button2_2['text'] = ''
        self.button2_3['text'] = ''
        self.button3_1['text'] = ''
        self.button3_2['text'] = ''
        self.button3_3['text'] = ''

        self.change_button_state(self, state=tk.NORMAL)
        for row in range(0, 3):
            for col in range(0, 3):
                self.TTT_board[row][col] = ''

        self.counter = 0

    def get_counts(self):
        return self.counter

    @staticmethod
    def button_clicked(self, button=None, row=0, col=0):
        counter = self.get_counts()
        row -= 1
        col -= 1

        if counter % 2 == 0:
            button['text'] = 'X'
            self.counter += 1
            button.config(state=tk.DISABLED)
            self.TTT_board[row][col] = 'X'
        else:
            button['text'] = 'O'
            self.counter += 1
            button.config(state=tk.DISABLED)
            self.TTT_board[row][col] = 'O'
        self.check_winner()

    def check_winner(self):
        for row in range(0, 3):
                if self.TTT_board[row][0] == 'X' and self.TTT_board[row][1] == 'X' and self.TTT_board[row][2] == 'X':
                    self.announce_winner('X')
                if self.TTT_board[row][0] == 'O' and self.TTT_board[row][1] == 'O' and self.TTT_board[row][2] == 'O':
                    self.announce_winner('O')
        for col in range(0, 3):
                if self.TTT_board[0][col] == 'X' and self.TTT_board[1][col] == 'X' and self.TTT_board[2][col] == 'X':
                    self.announce_winner('X')
                if self.TTT_board[0][col] == 'O' and self.TTT_board[1][col] == 'O' and self.TTT_board[2][col] == 'O':
                    self.announce_winner('O')

        if self.TTT_board[0][0] == 'X' and self.TTT_board[1][1] == 'X' and self.TTT_board[2][2] == 'X':
            self.announce_winner('X')
        if self.TTT_board[0][0] == 'O' and self.TTT_board[1][1] == 'O' and self.TTT_board[2][2] == 'O':
            self.announce_winner('O')
        if self.TTT_board[0][2] == 'X' and self.TTT_board[1][1] == 'X' and self.TTT_board[2][0] == 'X':
            self.announce_winner('X')
        if self.TTT_board[0][2] == 'O' and self.TTT_board[1][1] == 'O' and self.TTT_board[2][0] == 'O':
            self.announce_winner('O')

    @staticmethod
    def change_button_state(self, state=tk.NORMAL):
            self.button1_1['state'] = state
            self.button1_2['state'] = state
            self.button1_3['state'] = state
            self.button2_1['state'] = state
            self.button2_2['state'] = state
            self.button2_3['state'] = state
            self.button3_1['state'] = state
            self.button3_2['state'] = state
            self.button3_3['state'] = state

    def announce_winner(self, player):
        tk.messagebox.showinfo('Winner', player + ' WINS!!!')
        self.change_button_state(self, state=tk.DISABLED)
        self.reset()


TTTGui = TTT()
