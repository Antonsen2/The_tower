from game.Character import Npc


class FloorChallenge:
    def __init__(self, current_floor, npc):
        self.current_floor = current_floor
        self.enemy = npc

    def print_current_challenge(self):
        print("there is a", self.enemy.name, "stopping you from climbing up")


