import math
import os
from colorama import Fore, Style, init
init(autoreset=True)
player_score = 0
ai_score = 0
tie_score = 0

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_board(brd):
    symbols = []
    for i in range(9):
        if brd[i] == "X":
            symbols.append(Fore.RED + "X" + Style.RESET_ALL)
        elif brd[i] == "O":
            symbols.append(Fore.GREEN + "O" + Style.RESET_ALL)
        else:
            symbols.append(str(i + 1))

    print()
    for i in range(0, 9, 3):
        print(f"| {symbols[i]} | {symbols[i+1]} | {symbols[i+2]} |")
    print()

def check_winner(brd, player):
    win_conditions = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ]
    for condition in win_conditions:
        if brd[condition[0]] == brd[condition[1]] == brd[condition[2]] == player:
            return True
    return False

def check_tie(brd):
    return " " not in brd

def player_move(brd):
    while True:
        move = input("Enter your move (1-9): ")
        if not move.isdigit():
            print("Please enter a valid number.")
            continue
        move = int(move) - 1
        if 0 <= move <= 8 and brd[move] == " ":
            brd[move] = "X"
            break
        else:
            print("Invalid move. Try again.")

def ai_move(brd):
    best_score = -math.inf
    best_move = None
    for i in range(9):
        if brd[i] == " ":
            brd[i] = "O"
            score = minimax(brd, 0, False, -math.inf, math.inf)
            brd[i] = " "
            if score > best_score:
                best_score = score
                best_move = i
    brd[best_move] = "O"
def minimax(brd, depth, is_maximizing, alpha, beta):
    if check_winner(brd, "O"):
        return 1
    elif check_winner(brd, "X"):
        return -1
    elif check_tie(brd):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if brd[i] == " ":
                brd[i] = "O"
                score = minimax(brd, depth + 1, False, alpha, beta)
                brd[i] = " "
                best_score = max(score, best_score)
                alpha = max(alpha, score)
                if beta <= alpha:
                    break
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if brd[i] == " ":
                brd[i] = "X"
                score = minimax(brd, depth + 1, True, alpha, beta)
                brd[i] = " "
                best_score = min(score, best_score)
                beta = min(beta, score)
                if beta <= alpha:
                    break
        return best_score

def print_score():
    print(Fore.CYAN + f"\nScore: You - {player_score} | AI - {ai_score} | Ties - {tie_score}\n")

def play_game():
    global player_score, ai_score, tie_score
    print("🎮 Welcome to Tic-Tac-Toe! You are " + Fore.RED + "X" + Style.RESET_ALL + ", AI is " + Fore.GREEN + "O" + Style.RESET_ALL)

    while True:
        board = [" " for _ in range(9)]
        print_board(board)

        while True:
            player_move(board)
            print_board(board)
            if check_winner(board, "X"):
                print("🎉 You win!")
                player_score += 1
                break
            elif check_tie(board):
                print("It's a tie!")
                tie_score += 1
                break

            print("AI is making a move...")
            ai_move(board)
            print_board(board)
            if check_winner(board, "O"):
                print("😔 You lost! AI wins.")
                ai_score += 1
                break
            elif check_tie(board):
                print("It's a tie!")
                tie_score += 1
                break

        print_score()
        again = input("Play again? (y/n): ").lower()
        if again != "y":
            print("Thanks for playing!")
            break
        clear_screen()
if __name__ == "__main__":
    play_game()

