#Script to play TIC-TAC-TOE game
import sys
import subprocess as sb

def clear_screen():
    return sb.call('clear', shell=True)

def print_board():
    print(" {} | {} | {}".format(boardCells[7],
                                 boardCells[8],
                                 boardCells[9]))
    print("-----------")
    print(" {} | {} | {}".format(boardCells[4],
                                 boardCells[5],
                                 boardCells[6]))
    print("-----------")
    print(" {} | {} | {}".format(boardCells[1],
                                 boardCells[2],
                                 boardCells[3]))


def pick_symbol():
    print("Welcome to the classic Tic-Tac-Toe game !!!")
    print("Rules:\nTwo player Game.\nCan choose between X or O only.")
    print("Use the number pad to fill the Tic-Tac-Toe blocks")
    print("7|8|9")
    print("-----")
    print("4|5|6")
    print("-----")
    print("1|2|3")

    player1 = input("\nPlayer#1 pick symbol [X or O]: ").upper()
    player2 = ''
    if player1 == 'X':
        player2 = 'O'
    elif player1 != 'X' and player1 != 'O':
        print("Choose between X or O only !!!")
        print("Rules are rules, folks...")
        print("Exiting out of game")
        sys.exit(1)
    else:
        player2 = 'X'
    print("\nPlayers have choosen their symbol of play")
    print("\nPlayer#1: {}, Player#2: {}".format(player1,player2))
    print("Let's begin the game !\n")
    return player1, player2

def is_win():
    for winner in ['X','O']:
        if (boardCells[1] == boardCells[2] == boardCells[3] == winner or
            boardCells[4] == boardCells[5] == boardCells[6] == winner or
            boardCells[7] == boardCells[8] == boardCells[9] == winner or
            boardCells[1] == boardCells[4] == boardCells[7] == winner or
            boardCells[2] == boardCells[5] == boardCells[8] == winner or
            boardCells[3] == boardCells[6] == boardCells[9] == winner or
            boardCells[1] == boardCells[5] == boardCells[9] == winner or
            boardCells[3] == boardCells[5] == boardCells[7] == winner):
            return winner
    return False


def publish_result(player):
    if player == 'X' or player == 'O':
        clear_screen()
        print_board()
        print("{} wins the game !!!".format(player))
        sys.exit(0)
    else:
        clear_screen()
        print_board()
        print("Oh-Oh we have tie game -__-")
        sys.exit(0)


def update_board(board_spot, player):
    if boardCells[board_spot] == ' ':
        boardCells[board_spot] = player
    else:
        print("-__- This spot is alredy filled, pick another -__-")


def the_game():
    player1, player2 = pick_symbol()
    while not is_win():
        for turn in range(1,10):
            if turn%2 != 0 and turn in range(1,10):
                spot = int(input("Player#1, your turn to choose: "))
                update_board(spot, player1)
                if is_win() == 'X' or is_win() == 'O':
                    publish_result(is_win())
            else:
                spot = int(input("Player#2, your turn to choose: "))
                update_board(spot, player2)
                if is_win() == 'X' or is_win() == 'O':
                    publish_result(is_win())
            clear_screen()
            print_board()
        publish_result('tie')


if __name__ == '__main__':
    boardCells = [' '] * 10
    the_game()
