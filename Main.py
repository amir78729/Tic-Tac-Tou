cell_status = (".", "O", "X")


def print_game_field():
    print(game_field[0] + " " + game_field[1] + " " + game_field[2])
    print(game_field[3] + " " + game_field[4] + " " + game_field[5])
    print(game_field[6] + " " + game_field[7] + " " + game_field[8])


def new_game_field():
    for j in range(9):
        game_field[j] = cell_status[0]


def check_if_the_game_is_over():
    if game_field[0] == game_field[1] == game_field[2] != cell_status[0]:
        return True
    elif game_field[0] == game_field[4] == game_field[8] != cell_status[0]:
        return True
    elif game_field[0] == game_field[3] == game_field[6] != cell_status[0]:
        return True
    elif game_field[2] == game_field[5] == game_field[8] != cell_status[0]:
        return True
    elif game_field[6] == game_field[7] == game_field[8] != cell_status[0]:
        return True
    elif game_field[2] == game_field[4] == game_field[6] != cell_status[0]:
        return True
    elif game_field[3] == game_field[4] == game_field[5] != cell_status[0]:
        return True
    elif game_field[1] == game_field[4] == game_field[7] != cell_status[0]:
        return True
    return False


def new_game():
    new_game_field()
    game_over = False
    player_one_turn = True
    while not game_over:
        if player_one_turn:
            print("Player O:\nPlease select a home:(a number between 1 and 9)")
            choice = input()
            game_field[int(choice) - 1] = cell_status[1]
            print_game_field()
            player_one_turn = not player_one_turn
        else:
            print("Player X:\nPlease select a home:(a number between 1 and 9)")
            choice = input()
            game_field[int(choice) - 1] = cell_status[2]
            print_game_field()
            player_one_turn = not player_one_turn
        # now we should check if the game is over or not...
        if check_if_the_game_is_over():
            game_over = True

    if player_one_turn:
        print("X wins!")
    else:
        print("O wins!")


game_field = []
for i in range(9):
    game_field.append(cell_status[0])
continue_playing = True
while continue_playing:
    new_game()
    command = input("Play again?!(Y/N)")
    if command == "y" or command == "Y":
        continue
    elif command == "n" or command == "N":
        continue_playing = False
    else:
        print("WTF")




