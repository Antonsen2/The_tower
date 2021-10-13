import random
from game.Character import Player, Npc
from Map import Map
from game.fight import Fight
from game.floorchallenge import FloorChallenge
from items import Items


class Game:
    def __init__(self):
        self.map = Map()
        self.player = Player()
        self.npc = Npc(self.player.current_floor)
        self.running = True
        self.floor_challenge = None
        self.fight = Fight()
        self.items = Items()
        self.engage = False

    def run(self):
        print("You can see all commands by typing: commands")
        while self.running:
            self.update_floor_info()
            self.print_floor_info()
            self.user_input()
        print("Thanks for playing the game")

    def update_floor_info(self):
        self.floor_challenge = FloorChallenge(self.player.current_floor)
        if self.engage:
            self.battle(self.player, self.floor_challenge.enemy)

    def print_floor_info(self):
        print(self.map.map2[self.player.current_floor]['name'])
        self.floor_challenge.print_current_challenge()

    def climb_up(self):
        if self.player.current_floor > len(self.map.map2) - 1:
            print("You can't go there")
        if self.player.current_floor != len(self.map.map2) - 1:
            self.player.current_floor += 1
            self.npc = Npc(self.player.current_floor)
        else:
            print("You are on the top floor")

    def descend(self):
        if self.player.current_floor > 0:
            self.player.current_floor -= 1
            self.npc = Npc(self.player.current_floor)
        else:
            print("You can't go any lower")

    def user_input(self):
        command = input("What would you like to do? ")

        if len(command) > 0:
            match command.lower().split():
                case ["commands"]:
                    self.commands()
                case ["climb"] | ["climb up"] | ["up"]:
                    self.climb_up()
                case ["descend"] | ["climb down"] | ["down"]:
                    self.descend()
                case ["quit"] | ["exit"] | ["stop"]:
                    self.running = False
                case ["fight"] | ["engage"] | ["attack"]:
                    self.engage = True
                    print("attacking")

    def commands(self):

        print("The commands to climb up are: climb, climb up and up")
        print("The commands to descend are: descend, climb down and down")
        print("The commands to stop the game are: quit, exit and stop")

    def battle(self, player, npc):
        print("You engage the enemy, you can attack the enemy or you can defend yourself from their attack")
        while player.hp > 0 and npc.hp > 0:
            npc_damage = random.randrange(1, npc.ap + 1) - player.armor
            command = input("What would you like to do? ")
            if len(command) > 0:
                match command.lower().split():
                    case ["attack"]:
                        self.fight.attack(self.npc, self.player, npc_damage)

                    case ["defend"]:
                        self.fight.defend(self.npc, self.player, npc_damage)



def main():

    game = Game()
    game.run()


if __name__ == '__main__':

    main()


