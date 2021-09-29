import random


def hill_climbing(pos, level=0):
    curr_value = pos.value()
    while True:
        move, new_value = pos.best_move()
        if new_value >= curr_value:
            # no improvement, give up
            if curr_value != 0 and level < 5:
                return hill_climbing(NQPosition(pos.n), level=level+1)
            return pos, curr_value
        else:
            # position improves, keep searching
            curr_value = new_value
            pos.make_move(move)


class NQPosition:

    def __init__(self, N):
        self.n = N
        self.board = [i for i in range(1, N + 1)]  #represnting positions of queens on each row, starting from 1
        # number is ROW            INDEX if COLUMN
        random.shuffle(self.board)
        self.conflicts = self.value()

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
        self.board[move[0]], self.board[move[1]] = self.board[move[1]], self.board[move[0]]
        self.conflicts = self.value()
        return

    def best_move(self):
        conflicts = self.conflicts
        move = (0, 0)
        for i in range(self.n):
            for j in range(i + 1, self.n):
                board = self.board[:]
                board[i], board[j] = board[j], board[i]
                local_conflict = self.local_value(board)
                if local_conflict < conflicts:
                    conflicts = local_conflict
                    move = (i, j)
        return move, conflicts

    def __repr__(self):
        board = [[0 for j in range(self.n)] for i in range(self.n)]
        for i in range(len(self.board)):
            board[self.board[i] - 1][i] = 1
            board[self.board[i] - 1] = str(board[self.board[i] - 1])
        return '\n'.join(board)


pos = NQPosition(6)  # test with the tiny 4x4 board first
print("Initial position value", pos.value())
best_pos, best_value = hill_climbing(pos)
print("Final value", best_value)
print(best_pos)
# if best_value is 0, we solved the problem
