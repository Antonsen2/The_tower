from game_files.character import Player, Npc
from map import Map
from game_files.fight import Fight
from game_files.floorchallenge import FloorChallenge


class Game:
    def __init__(self):
        self.map = Map()
        self.player = Player()
        self.npc = Npc(self.player.current_floor)
        self.running = True
        self.floor_challenge = None
        self.fight = Fight()
        self.engage = False

    def run(self):
        print("You can see all commands by typing: commands")
        while self.running:
            self.update_floor_info()
            self.print_floor_info()
            self.user_input()
        print("Thanks for playing the game_files")

    def update_floor_info(self):
        if self.engage:
            self.fight.battle(self.player, self.floor_challenge.enemy)
        if self.npc.hp <= 0:
            self.engage = False
            self.npc = None
        self.floor_challenge = FloorChallenge(self.player.current_floor, self.npc)

    def print_floor_info(self):
        current_floor = self.map.get_current_floor(self.player.current_floor)
        print(current_floor.name)
        self.floor_challenge.print_current_challenge()
        if len(current_floor.items) >= 1:
            found_items = [item.name for item in current_floor.items if item.visible]
            print("Items in the room:", found_items)

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
        current_floor = self.map.get_current_floor(self.player.current_floor)

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
                case ["get", *items] | ["pick", "up", *items] | ["pick", *items, "up"]:
                    for item in items:
                        self.player.get_item(item, current_floor)
                case ["drop", *items]:
                    for item in items:
                        self.player.drop_item(item, current_floor)
                case ["use", *items]:
                    for item in items:
                        self.player.use_item(item, self.player)
                case ["inventory"] | ["inv"] | ["bag"]:
                    self.player.print_inventory()
                case ["equip", *items]:
                    for item in items:
                        self.player.equip(item)
                        self.player.equipment.equipment_stats()
                case ["equipped"] | ["character"] | ["stats"] | ["equipment"]:
                    self.player.equipment.print_equipment()
                case ["open"] | ["open", "chest"]:
                    self.floor_challenge.open_chest(current_floor, self.player)
                case ["fight"] | ["engage"] | ["attack"]:
                    self.engage = True
                case ["quit"] | ["exit"] | ["stop"]:
                    self.running = False
                case _:
                    print(f"I dont understand {command}, you can see a list of commands by typing commands")

    @staticmethod
    def commands():
        print("The commands to climb up are: climb, climb up and up")
        print("The commands to descend are: descend, climb down and down")
        print("The commands to check your inventory is: inventory, inv and bag")
        print("the command to equip something is equip and the item name")
        print("the commands to check what items you have equipped and your stats is equipped, character and stats")
        print("the commands to open the chest is: open and open chest")
        print("The commands to fight is: fight, engage and attack")
        print("The commands to stop the game_files are: quit, exit and stop")

