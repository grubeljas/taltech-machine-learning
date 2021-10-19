import copy
import random


class Game:

    def __init__(self):
        self.board = [[0 for _ in range(7)] for _ in range(6)]
        self.play_game()

    def play_game(self, player_side=1):
        playing = True
        comp_side = 2 if player_side == 1 else 1
        symbol = player_side
        print(self)
        while playing:
            if symbol == player_side:
                print("PLAYER'S TURN")
                while playing:
                    movestr = input("Your move? ")
                    try:
                        move = parse(self.board, int(movestr))
                        break
                    except IndexError or ValueError:
                        print("\nInvalid input\n")
                pos = make_move(self.board, move)
                self.board[pos[0]][pos[1]] = symbol
                symbol = comp_side
            else:
                print("COMPUTER'S TURN")
                move = self.pure_mc(comp_side)
                pos = make_move(self.board, move)
                self.board[pos[0]][pos[1]] = symbol
                symbol = player_side

            print(self)
            res = if_win(pos, self.board)
            if res:
                playing = False
                if res == "draw":
                    print(res)
                else:
                    if symbol == player_side:
                        print("winner is computer")
                    else:
                        print("winner is player")

    def pure_mc(self, side, N=200):
        my_side = side
        initial_moves = []
        for i in range(7):
            if self.board[0][i] == 0:
                initial_moves.append(i)

        win_counts = dict((move, 0) for move in initial_moves)
        for move in initial_moves:
            for i in range(N):
                # make random moves until the game is over
                res = simulate(copy.deepcopy(self.board), move, my_side)
                if res == "win":
                    win_counts[move] += 1
                elif res == "draw":
                    win_counts[move] += 0.5
        print(win_counts)

        count = -1
        best_move = None
        for move in win_counts.keys():
            if win_counts[move] > count:
                count = win_counts[move]
                best_move = move
        return best_move

    def __repr__(self):
        sentence = ""
        for row in self.board:
            sentence += "|"
            for symbol in row:
                if symbol == 0:
                    sentence += " "
                elif symbol == 2:
                    sentence += "O"
                else:
                    sentence += "X"
            sentence += "|\n"
        sentence += "|0123456|\n"
        return sentence


def simulate(board, move, comp_side):
    player_side = 2 if comp_side != 2 else 1
    while True:
        for side in [comp_side, player_side]:
            pos = None
            while not pos:
                try:
                    pos = make_move(board, parse(board, move))
                except IndexError:
                    move = random.randint(0, 6)

            board[pos[0]][pos[1]] = side

            move = random.randint(0, 6)

            res = if_win(pos, board)
            if res == "draw":
                return res
            elif res:
                if side == comp_side:
                    return "win"
                else:
                    return "lose"


def parse(board, move):
    if board[0][move] == 0:
        return move
    raise IndexError


def make_move(board, move):
    i = 5
    while True:
        if board[i][move] != 0:
            i -= 1
        else:
            return i, move


def if_win(pos, board):
    symbol = board[pos[0]][pos[1]]
    if 0 not in board[0]:
        return "draw"
    return horizontal_win(pos, symbol, board) or vertical_win(pos, symbol, board) or diagonal_win(pos, symbol, board)


def horizontal_win(move, new_symbol, board):
    for i in range(4):
        if board[move[0]][i] == board[move[0]][i + 1] \
                == board[move[0]][i + 2] == board[move[0]][i + 3] == new_symbol:
            return True
    return False


def vertical_win(move, symbol, board):
    try:
        return board[move[0]][move[1]] == board[move[0] + 1][move[1]] \
               == board[move[0] + 2][move[1]] == board[move[0] + 3][move[1]] == symbol
    except IndexError:
        return False


def diagonal_win(move, new_symbol, board):
    for c in range(4):
        for r in range(3):
            if board[r][c] == board[r + 1][c + 1] == board[r + 2][c + 2] == board[r + 3][c + 3] == new_symbol:
                return True

    for c in range(4):
        for r in range(3, 6):
            if board[r][c] == board[r - 1][c + 1] == board[r - 2][c + 2] == board[r - 3][c + 3] == new_symbol:
                return True

    return False


def main():
    Game()


if __name__ == '__main__':
    main()
