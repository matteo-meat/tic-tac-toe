class Board:

    def __init__(self):
        self.board = []

    def create_board(self):
        for i in range(3):
            row = []
            for j in range(3):
                row.append("-")
            self.board.append(row)

    def check_rows(self, player):
        win = False
        i = 0
        while i < 3 and not win:
            j = 0
            while j < 3:
                if not self.board[i][j] == player:
                    win = False
                    break
                else:
                    win = True
                    j += 1
            i += 1
        return win

    def check_columns(self, player):
        win = False
        i = 0
        while i < 3 and not win:
            j = 0
            while j < 3:
                if not self.board[j][i] == player:
                    win = False
                    break
                else:
                    win = True
                    j += 1
            i += 1
        return win

    def check_diagonals(self, player):
        win = False
        i = 0
        while i < 3 and not win:
            if not self.board[i][i] == player:
                win = False
            else:
                win = True
            i += 1
        if not win:
            while i >= 0 and not win:
                if not self.board[i][i] == player:
                    win = False
                else:
                    win = True
                i -= 1
        return win

    def check_win(self, player):
        if self.check_rows(player):
            return True
        elif self.check_columns(player):
            return True
        elif self.check_diagonals(player):
            return True
        return False

    def print_board(self):
        for i in range(3):
            print(self.board[i])
