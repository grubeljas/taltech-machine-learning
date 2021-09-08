import math
from queue import Queue

lava_map1 = [
    "      **               **      ",
    "     ***     D        ***      ",
    "     ***                       ",
    "                      *****    ",
    "           ****      ********  ",
    "           ***          *******",
    " **                      ******",
    "*****             ****     *** ",
    "*****              **          ",
    "***                            ",
    "              **         ******",
    "**            ***       *******",
    "***                      ***** ",
    "                               ",
    "                s              ",
]
start_row = 14
start_col = 16

start1 = (start_row, start_col)


class PathFinder:

    def __init__(self, map, start):
        self.map = map
        self.start = start
        self.came_from = {start: None}

    def find_neighbors(self, current: tuple):
        return [(current[0], current[1] + 1),
                (current[0], current[1] - 1),
                (current[0] + 1, current[1]),
                (current[0] - 1, current[1])]

    def my_search(self):
        frontier = Queue()
        frontier.put(self.start)

        while not frontier.empty():
            current = frontier.get()

            # we don't care about all paths, so we should check if current is a diamond.
            # If it is, we store the coordinates of the diamond and stop the search
            # (implement this yourself)

            for next_graph in self.find_neighbors(current):  # lots of changes needed here
                # find neighboring cells on the map as it is given
                # (the cells up, down, left and right)
                try:
                    symbol = self.map[next_graph[0]][next_graph[1]]
                    if next_graph not in self.came_from and symbol != "*":
                        frontier.put(next_graph)
                        self.came_from[next_graph] = current
                        if symbol == "D":
                            return next_graph
                except IndexError:
                    continue

    def find_path(self):
        current = self.my_search()
        path = []
        while current != self.start:
            path.append(current)
            current = self.came_from[current]
            row = stringToList(self.map[current[0]])
            row[current[1]] = "'"
            self.map[current[0]] = listToString(row)
        path.append(self.start)  # optional
        path.reverse()
        print('\n'.join(self.map))
        return path


def h(node, goal):
    return abs(node[0] - goal[0]) + abs(goal[0], goal[1])


def listToString(l):
   str1 = ""
   for ele in l:
      str1 += ele
   return str1


def stringToList(s):
   list = []
   for symbol in s:
      list.append(symbol)

   return list


with open("cave300x300") as f:
    map_data = [l.strip() for l in f.readlines() if len(l)>1]
path = PathFinder(map_data, start1)
print(path.find_path())
