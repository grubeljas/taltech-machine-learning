import random


class Sim:

    def __init__(self, agent):
        self.agent = agent
        self.rooms = {"A": 1, "B": 1}
        self.location = "A"
        self.costs = 0

    def cost(self, action):
        if action == "NoOp":
            return 0
        else:
            return 1

    def run(self, steps=10):
        for i in range(steps):
            self.step()

    def random_effect(self):
        for room in self.rooms.keys():
            if random.random() <= 0.25:
                self.rooms[room] = 1

    def step(self):
        action = self.agent.decide_action(self.location, self.rooms.get(self.location))
        print(action)
        if action == "Vacuum":
            self.rooms[self.location] = 0
        elif action == "Right":
            self.location = "B"
        elif action == "Left":
            self.location = "A"
        self.costs += self.cost(action)

    def perf(self, steps):
        return steps - self.costs


class Agent:
    def decide_action(self, room, status):
        if status == 1:
            return "Vacuum"
        elif room == "A":
            return "Right"
        else:
            return "Left"


class AgentSmart:

    def __init__(self):
        self.come_from = None

    def decide_action(self, room, status):
        if status == 1:
            return "Vacuum"
        elif room == "A" and self.come_from != "B":
            self.come_from = "A"
            return "Right"
        elif room == "B" and self.come_from != "A":
            self.come_from = "B"
            return "Left"
        else:
            return "NoOp"


sim = Sim(AgentSmart())
sim.run()
print(sim.perf(10))
