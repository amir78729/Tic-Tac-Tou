cell_status = (".", "O", "X")


def print_game_field():
    print(game_field[0] + " " + game_field[1] + " " + game_field[2])
    print(game_field[3] + " " + game_field[4] + " " + game_field[5])
    print(game_field[6] + " " + game_field[7] + " " + game_field[8])


def new_game_field():
    for i in range(9):
        game_field.append(cell_status[0])


game_field = []
new_game_field()
game_over = False
player_one_turn = True
while not game_over:
    if player_one_turn:
        print("Player O:\nPlease select a home:(a number between 1 and 9)")
        choice = input()
        game_field[int(choice)-1] = cell_status[1]
        print_game_field()
        player_one_turn = not player_one_turn
    else:
        print("Player X:\nPlease select a home:(a number between 1 and 9)")
        choice = input()
        game_field[int(choice)-1] = cell_status[2]
        print_game_field()
        player_one_turn = not player_one_turn
    # now we should check if the game is over or not...

