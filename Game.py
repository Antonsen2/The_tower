from Character import Player, Npc
from Map import Map


class Game:
    def __init__(self):
        self.map = Map()
        self.player = Player("glenn", "axe", 100)
        self.running = True
        #  self.npc = Npc()

    def run(self):
        while self.running:
            self.print_floor_info()
            self.user_input()
        print("Thanks for playing the game")

    def print_floor_info(self):
        print(self.map.map2[self.player.current_floor])

    def climb_up(self):
        if self.player.current_floor > len(self.map.map2) - 1:
            print("You can't go there")
        if self.player.current_floor != len(self.map.map2) - 1:
            self.player.current_floor += 1
        else:
            print("You are on the top floor")

    def descend(self):
        if self.player.current_floor > 0:
            self.player.current_floor -= 1
        else:
            print("You can't go any lower")

    def user_input(self):
        command = input("what to do? ")

        if len(command) > 0:
            match command.lower().split():
                case ["climb"] | ["climb up"] | ["up"]:
                    self.climb_up()
                case ["descend"] | ["climb down"] | ["down"]:
                    self.descend()
                case ["quit"] | ["exit"] | ["stop"]:
                    self.running = False


def main():

    game = Game()
    game.run()


if __name__ == '__main__':

    main()


