from Character import Player, Npc
from Map import Map
from item_data import items
from npc_data import monsters


class Game:
    def __init__(self):
        self.map = Map()
        self.player = Player()
        self.running = True
        self.floor_challenge = None
        self.fight = Fight()
        self.items = Items()
        self.engage = None


    def run(self):
        print("You can see all commands by typing: commands")
        while self.running:
            self.update_floor_info()
            self.print_floor_info()
            self.user_input()
           # self.items.current_item_in_room()

        print("Thanks for playing the game")

    def update_floor_info(self):
        self.floor_challenge = FloorChallenge(self.player.current_floor)
        if self.engage:
            self.fight.engage(self.player, self.floor_challenge.enemy)

    def print_floor_info(self):
        print(self.map.map2[self.player.current_floor]['name'])
        self.floor_challenge.print_current_challenge()

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


class Fight:

    def engage(self, player, npc):
        print("You engage the enemy, you can attack the enemy or you can defend yourself from their attack")
        while player.hp > 0 and npc.hp > 0:
            command = input("What would you like to do? ")
            if len(command) > 0:
                match command.lower().split():
                    case ["attack"]:
                        player.hp -= npc.ap - player.armor
                        npc.hp -= player.ap
                        print(player.hp)
                    case ["defend"]:
                        player.hp -= npc.ap - player.armor * 3
                        npc.hp -= player.armor
                        print(player.hp)


class FloorChallenge:
    def __init__(self, current_floor):
        self.current_floor = current_floor
        self.enemy = Npc(current_floor)

    def print_current_challenge(self):
        print("there is a", self.enemy.name, "stopping you from climbing up")



class Items:
    def __init__(self):
        self.item = None
        self.map = Map()
        self.player = Player()

    def current_item_in_room(self):
        for self.item in items:
            if self.item['id'] in self.map.map2[self.player.current_floor]['items']:
                print("There is a", self.item['name'], "that you can open in this room")

    #  problem.. den uppdaterar inte current_floor.. finns det något snyygare sätt att göra detta än vad jag har gjort ovanför?


def main():

    game = Game()
    game.run()


if __name__ == '__main__':

    main()


