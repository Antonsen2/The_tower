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
        self.items = Items(self.player, self.map)
        self.engage = False

    def run(self):
        print("You can see all commands by typing: commands")
        while self.running:
            self.update_floor_info()
            self.print_floor_info()
            self.user_input()
        print("Thanks for playing the game")

    def update_floor_info(self):
        if self.engage:
            self.battle(self.player, self.floor_challenge.enemy)
        self.floor_challenge = FloorChallenge(self.player.current_floor, self.npc)

    def print_floor_info(self):
        print(self.map.map2[self.player.current_floor]['name'])
        self.floor_challenge.print_current_challenge()
        self.items.print_current_item_in_room()

    def climb_up(self):
        if self.player.current_floor > len(self.map.map2) - 1:
            print("You can't go there")
        if self.player.current_floor != len(self.map.map2) - 1:
            self.player.current_floor += 1
            self.npc = Npc(self.player.current_floor)
        else:
            print("You are on the top floor, you can't go any further")

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
                    if not self.npc:
                        self.climb_up()
                    else:
                        print("You need to defeat the enemy before climbing up")
                case ["descend"] | ["climb down"] | ["down"]:
                    self.descend()
                case["get", *items] | ["pick", "up", *items] | ["pick", *items, "up"]:
                    for item in items:
                        self.items.get_item(item)
                case["drop", *items]:
                    for item in items:
                        self.items.drop_item(item)
                case["use", *items]:
                    for item in items:
                        self.player.use_item(item, self.player)
                case ["inventory"] | ["inv"] | ["bag"]:
                    self.player.print_inventory()
                case ["equip", *items]:
                    for item in items:
                        self.player.equip(item)
                        self.player.equipped_stats(self.player)
                case ["equipped"] | ["character"] | ["stats"]:
                    self.player.print_character(self.player)
                case ["open"] | ["open chest"]:
                    self.floor_challenge.chest_challenge()
                    self.items.open_chest()
                case ["fight"] | ["engage"] | ["attack"]:
                    self.engage = True
                case ["quit"] | ["exit"] | ["stop"]:
                    self.running = False
                case _:
                    print(f"I dont understand {command}, you can see a list of commands by typing commands")

    def commands(self):

        print("The commands to climb up are: climb, climb up and up")
        print("The commands to descend are: descend, climb down and down")
        print("The commands to check your inventory is: inventory, inv and bag")
        print("the command to equip something is equip and the item name")
        print("the commands to check what items you have equipped and your stats is equipped, character and stats")
        print("the commands to open the chest is: open and open chest")
        print("The commands to fight is: fight, engage and attack")
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

            if npc.hp <= 0:
                self.npc = None
                self.engage = False
                self.items.boss_drop()



def main():

    game = Game()
    game.run()


if __name__ == '__main__':

    main()


