
def pure_mc(pos, N=200):
    # all moves from starting position
    my_side = pos["to_move"]
    initial_moves = moves(pos)
    # win counters per move
    win_counts = dict((move, 0) for move in initial_moves)

    for move in initial_moves:
        for i in range(N):
            # make random moves until the game is over
            res = simulate(pos, move, my_side)
            if res == WIN:
                win_counts[move] += 1
            elif res == DRAW:
                win_counts[move] += 0.5

    # find the move with the highest number of wins, return it

def play_game(pos, player_side = "X"):
    playing = True
    while playing:
        if pos["to_move"] == player_side:
            # print the position
            dump_pos(pos)
            movestr = input("Your move? ")
            # convert user input into the move format you are using internally
            move = parse_move(movestr)
        else:
            move = pure_mc(pos)

        pos = make_move(pos, move)
        # check after each move
        if is_over(pos):
            playing = False

play_game(starting_pos)
