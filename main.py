class Board:
    def __init__(self):
        self.board = [['n', 'n', 'n'],
                      ['n', 'n', 'n'],
                      ['n', 'n', 'n']]

    def check_victory(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] and self.board[i][0] != "n":
                return True

        for i in range(3):
            if self.board[0][i] == self.board[1][i] == self.board[2][i] and self.board[0][i] != "n":
                return True

        if self.board[0][0] == self.board[1][1] == self.board[2][2] and self.board[0][0] != "n":
            return True

        if self.board[2][2] == self.board[1][1] == self.board[0][0] and self.board[2][2] != "n":
            return True

        else:
            return False

    def set_piece(self, x, y, character):
        x = int(x)
        y = int(y)
        character = str(character)

        self.board[y][x] = character

        print("foi")

    def reset_board(self):
        self.board = [['n', 'n', 'n'],
                      ['n', 'n', 'n'],
                      ['n', 'n', 'n']]

    def print_board(self):
        print("-" * 10 + f"JOGO DA VELHA" + "-" * 10 + "\n")

        print(" " * 13 + "-" * 7)
        print(" " * 13 + f"|{self.board[0][0]}|{self.board[0][1]}|{self.board[0][2]}|")
        print(" " * 13 + "-" * 7)
        print(" " * 13 + f"|{self.board[1][0]}|{self.board[1][1]}|{self.board[1][2]}|")
        print(" " * 13 + "-" * 7)
        print(" " * 13 + f"|{self.board[2][0]}|{self.board[2][1]}|{self.board[2][2]}|")
        print(" " * 13 + "-" * 7)
        print("\n")
        print("-" * 10 + f"JOGO DA VELHA" + "-" * 10)
        print("\n")


def game():
    board = Board()
    current_player = 'x'

    while True:
        print("Escolha uma peça:")
        board.print_board()
        y = int(input("Y: "))
        x = int(input("X: "))
        if current_player == 'x':
            if board.board[y][x] != "n" or "o":
                board.set_piece(x=x, y=y, character='x')
                current_player = 'O'
            else:
                print("Espaço Usado")

        else:
            if board.board[y][x] != "n" or "x":
                board.set_piece(x=x, y=y, character='o')
                current_player = 'X'
            else:
                print("Espaço Usado")


        if board.check_victory():
            print("-" * 10 + f"JOGO DA VELHA" + "-" * 10 + "\n")
            print("\n")
            print(" " * 7 + f"JOGADOR > {current_player} GANHOU\n")
            print("\n")
            print("-" * 10 + f"JOGO DA VELHA" + "-" * 10 + "\n")
            break




game()
