import collections

def hill_climbing(pos):
    curr_value = pos.value()
    while True:
        move, new_value = pos.best_move()
        if new_value >= curr_value:
            # no improvement, give up
            return pos, curr_value
        else:
            # position improves, keep searching
            curr_value = new_value
            pos.make_move(move)


class NQPosition:

    def __init__(self, N):
        self.n = N
        self.board = [i for i in range(1, N + 1)]  # represnting positions of queens on each row, starting from 1
        # number is ROW            INDEX if COLUMN

    def value(self):
        h = 0
        unique = set(self.board)
        h += len(self.board) - len(unique)
        for i in range(self.n):
            for j in range(i + 1, self.n):
                if abs(i - j) == abs(self.board[i] - self.board[j]):
                    h += 1
        return h

    def local_value(self, board):
        h = 0
        unique = set(board)
        h += len(board) - len(unique)
        for i in range(self.n):
            for j in range(i + 1, self.n):
                if abs(i - j) == abs(board[i] - board[j]):
                    h += 1
        #TODO идея от каждой королевы провести 8 лучей пока не встретит королеву или край карты
        return h

    def make_move(self, move):
        return
        # actually execute a move (change the board)

    def best_move(self):
        conflicts = int("infinity")
        for i in range(self.n):
            for j in range(i + 1, self.n):
                board = self.board[:]
                board[i], board[j] = board[j], board[i]




        return


pos = NQPosition(4)  # test with the tiny 4x4 board first
print("Initial position value", pos.value())
#best_pos, best_value = hill_climbing(pos)
#print("Final value", best_value)
# if best_value is 0, we solved the problem
