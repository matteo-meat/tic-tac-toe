from board import Board
from random import randint


def swap_player(player):
    if player == "X":
        return "O"
    else:
        return "X"


def process_turn(player, choice):
    board.print_board()
    move(player, choice)
    print("\n\n")
    board.print_board()
    return board.check_win(player)


def move(player, choice):
    if player != choice:
        row, col = randint(0, 2), randint(0, 2)
        while board.board[row][col] != "-":
            row, col = randint(0, 2), randint(0, 2)
        board.make_move(player, row, col)
    else:
        row, col = input("Enter the coordinates for your next move").split()
        while board.board[row][col] != "-":
            row, col = int(input("Spot taken, choose again!").split())
        board.make_move(player, row, col)


def start(choice):
    while choice != "X" and choice != "O":
        choice = input("Hello, you wanna play 'X' or 'O'?").upper()
        if choice != "X" and choice != "O":
            print("Please enter a valid choice")

    if randint(0, 1) == 0:
        curr_player = choice
        print("You are starting!")
    else:
        if choice == "X":
            curr_player = "O"
        else:
            curr_player = "X"
        print("The computer is starting!")

    return curr_player, choice


board = Board()
choice = ""
player, choice = start(choice)
end = False
while not end:
    end = process_turn(player, choice)
    if end:
        print(f"Player {player} won!!!")
    else:
        swap_player(player)
        print()
