
import game_functions as gf

def main():
    board = gf.init_game()
    print_board(board)

    while True:
        move = input("Enter move (w/a/s/d): ").lower()
        valid_moves = {'w': gf.move_up, 'a': gf.move_left, 's': gf.move_down, 'd': gf.move_right}

        if move in valid_moves:
            try:
                new_board = valid_moves[move](board)
                if board != new_board:
                    board = new_board
                    board = gf.add_new_two(board)
                    print_board(board)

                    if gf.check_win(board):
                        print("Congratulations! You've reached 2048!")
                        break

                    if gf.check_no_moves(board):
                        print("No more moves available. Game over!")
                        break
                else:
                    print("Move not possible. Try a different direction.")
            except Exception as e:
                print("An error occurred:", e)
        else:
            print("Invalid input. Please enter w, a, s, or d.")

def print_board(board):
    for row in board:
        print(' '.join(str(cell).rjust(4) for cell in row))
    print()

if __name__ == "__main__":
    main()
