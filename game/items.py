from game.Character import Player
from Map import Map
from data.item_data import items
import floorchallenge


class Items:
    def __init__(self, player, map):
        self.item = items
        self.player = player
        self.map = map
        self.floor_challenge = None


    @staticmethod
    def get_item(name: str) -> dict:
        for item in items:
            if name == item['name']:
                return item




    def current_item_in_room(self):
        for item in self.item:
            if item['id'] in self.map.map2[self.player.current_floor]['items']:
                if item["visible"]:
                    print("There is", item['description'], "in this room")


    def print_chest(self):
        ids = []
        print("The chest contains:")
        for item in items:
            if item["container"]:
                item["visible"] = False
                for i in item['contains']:
                    ids.append(i)
        for item in items:
            for id2 in ids:
                if item['id'] == id2:
                    print("a", item['name'])


    def open_chest(self):
        chest_open = True
        if self.item[0]["visible"]:
            while chest_open:
                self.print_chest()
                command1 = input("What item would you like to pick up? ")
                match command1.lower().split():
                    case ["none"] | ["close"] | ["stop"]:
                        chest_open = False
                    case ["knife"] | ["potion"]:
                        item = self.get_item(command1)
                        if item:
                            self.player.inventory.append(item)
                            self.item[0]['contains'].remove(item["id"])
                    case _:
                        print(f"I dont understand {command1}")







