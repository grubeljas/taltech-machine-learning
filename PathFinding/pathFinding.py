from queue import Queue, PriorityQueue


class PathFinder:

    def __init__(self, map, start, goal=None):
        self.map = map
        self.start = start
        self.came_from = {start: None}
        self.goal = goal

    def find_neighbors(self, current: tuple):
        return [(current[0], current[1] - 1),
                (current[0], current[1] + 1),
                (current[0] - 1, current[1]),
                (current[0] + 1, current[1])]

    def my_search(self):
        frontier = Queue()
        frontier.put(self.start)

        while not frontier.empty():
            current = frontier.get()
            for next_graph in self.find_neighbors(current):
                try:
                    symbol = self.map[next_graph[0]][next_graph[1]]
                    if next_graph not in self.came_from and symbol != "*":
                        frontier.put(next_graph)
                        self.came_from[next_graph] = current
                        if symbol == "D":
                            self.goal = next_graph
                            return self.find_path()
                except IndexError:
                    continue
        return None

    def greedy(self):
        frontier = PriorityQueue()
        frontier.put((0, self.start))

        while not frontier.empty():
            _, current = frontier.get()
            if current == self.goal:
                break
            for next in self.find_neighbors(current):
                try:
                    if next not in self.came_from and self.map[next[0]][next[1]] != "*":
                        priority = h(self.goal, next)
                        frontier.put((priority, next))
                        self.came_from[next] = current
                except IndexError:
                    continue
        return self.find_path()

    def astar(self):
        frontier = PriorityQueue()
        frontier.put((0, self.start))
        cost_so_far = {}
        cost_so_far[self.start] = 0

        while not frontier.empty():
            _, current = frontier.get()
            if current == self.goal:
                break
            for next in self.find_neighbors(current):
                try:
                    new_cost = cost_so_far[current] + 1
                    if (next not in cost_so_far or new_cost < cost_so_far[next]) and self.map[next[0]][next[1]] != "*":
                        cost_so_far[next] = new_cost
                        priority = new_cost + h(next, self.goal)  # g(n) + h(n)
                        frontier.put((priority, next))
                        self.came_from[next] = current
                except IndexError:
                    continue
        return self.find_path()

    def find_path(self):
        current = self.goal
        if not current:
            return current  #None path
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
    return abs(node[0] - goal[0]) + abs(goal[1] - goal[1])


def listToString(list):
    str = ""
    for ele in list:
        str += ele
    return str


def stringToList(s):
    """
    Convert string to list.
    :param s:
    :return:
    """
    list = []
    for symbol in s:
        list.append(symbol)
    return list


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


lava_map2 = [
    "     **********************    ",
    "   *******   D    **********   ",
    "   *******                     ",
    " ****************    **********",
    "***********          ********  ",
    "            *******************",
    " ********    ******************",
    "********                   ****",
    "*****       ************       ",
    "***               *********    ",
    "*      ******      ************",
    "*****************       *******",
    "***      ****            ***** ",
    "                               ",
    "                s              ",
]

start1 = (14, 16)
goal1 = (1, 13)
start2 = (2, 2)
goal3 = (295, 257)

maps_variants = ["cave300x300", "cave600x600", "cave900x900"]

with open(maps_variants[2]) as f:
    map_data = [line.strip() for line in f.readlines() if len(line) > 1]

path = PathFinder(map_data, start2)
print(path.goal)
print(path.my_search())
