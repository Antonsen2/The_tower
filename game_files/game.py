import pickle
from os import listdir

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
        print("You have stepped in to a tower, the only way to exit is defeating all challenges")
        while self.running:
            self.update_floor_info()
            self.print_floor_info()
            self.user_input()
            self.game_complete()

        print("Thanks for playing the game")

    def update_floor_info(self):
        if self.engage:
            self.fight.battle(self.player, self.floor_challenge.enemy)
        if self.npc:
            if self.npc.hp <= 0:
                self.engage = False
                self.npc = None
        self.floor_challenge = FloorChallenge(self.player.current_floor, self.npc)
        if self.player.hp <= 0:
            print("oh no, you died. game over!")
            self.running = False

    def print_floor_info(self):
        current_floor = self.map.get_current_floor(self.player.current_floor)
        self.floor_challenge.print_current_challenge()
        if len(current_floor.items) >= 1:
            found_items = [item.name for item in current_floor.items if item.visible]
            print("Items in the room:", found_items)

    def climb_up(self):
        if self.player.current_floor > len(self.map.map2) - 1:
            print("You can't go there")
        if self.player.current_floor != len(self.map.map2) - 1:
            self.player.current_floor += 1
            print(self.map.get_current_floor(self.player.current_floor).name)
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
                case ["climb"] | ["climb", "up"] | ["up"]:
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
                case ["unequip", *items]:
                    for item in items:
                        self.player.unequip(item)
                case ["equipped"] | ["character"] | ["stats"] | ["equipment"]:
                    self.player.equipment.print_equipment()
                case ["open"] | ["open", "chest"]:
                    self.floor_challenge.open_chest(current_floor, self.player)
                case ["fight"] | ["engage"] | ["attack"]:
                    self.engage = True
                case ["save"]:
                    self.save()
                case ["load"]:
                    self.load()
                case ["quit"] | ["exit"] | ["stop"]:
                    self.running = False
                case _:
                    print(f"I dont understand {command}, you can see a list of commands by typing commands")

    def game_complete(self):
        if self.player.current_floor == len(self.map.map2) - 1 and not self.npc:
            self.running = False

    def save(self):
        file_name = input("What would you like to call this save? ")
        file_name += '.tt'

        data_to_save = {
            'player': self.player,
            'map': self.map
        }

        with open('./saved_games/' + file_name, 'wb') as save_file:
            pickle.dump(data_to_save, save_file)

    @staticmethod
    def list_saved_games():
        files = []
        for f in listdir('./saved_games'):
            if f.endswith('.tt'):
                files.append(f.replace('.tt', ''))

        files = [f.replace('.ttt', '') for f in listdir('./saved_games') if f.endswith('.tt')]

        return files

    def load(self):
        saved_games = self.list_saved_games()

        while True:
            print("You have these games saved:")
            for game in saved_games:
                print(game)
            file_name = input("What save would you like to load? ")
            if file_name in saved_games:
                break
            print(f"{file_name} is not the name of a saved game")

        file_name += '.taf'
        with open('./saved_games/' + file_name, 'rb') as save_file:
            loaded_data = pickle.load(save_file)

        self.map = loaded_data['map']
        self.player = loaded_data['player']

    @staticmethod
    def commands():
        print("The commands to climb up are: climb, climb up and up")
        print("The commands to descend are: descend, climb down and down")
        print("The commands to check your inventory is: inventory, inv and bag")
        print("the command to equip something is equip and the item name")
        print("the command to unequip something is unequip and the item name")
        print("the commands to check what items you have equipped and your stats is equipped, character and stats")
        print("the commands to open the chest is: open and open chest")
        print("The commands to fight is: fight, engage and attack")
        print("The commands to stop the game_files are: quit, exit and stop")
