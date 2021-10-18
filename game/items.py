from game.Character import Player
from Map import Map
from data.item_data import items
#  import floorchallenge


class Items:
    def __init__(self, player, map):
        self.item = None
        self.player = player
        self.map = map
        # self.floorchallenge = floorchallenge

    def current_item_in_room(self):
        for self.item in items:
            if self.item['id'] in self.map.map2[self.player.current_floor]['items']:
                if self.item["visible"]:
                    print("There is", self.item['description'], "in this room")


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
        #  ToDo only open chest if puzzle is complete.. this is a project for tomorrow
        while chest_open:
            self.print_chest()
            command1 = input("What item would you like to pick up? ")
            if command1 == 'none':
                chest_open = False
            else:
                for item in items:
                    if item['name'] == command1:
                        command1 = item['id']
                for item in items:
                    if item['container']:
                        for id in item['contains']:
                            if id == command1:
                                item['contains'].remove(id)
                                self.player.inventory.append(id)
                                if len(item['contains']) == 0:
                                    chest_open = False

                    print("Poof the chest magicly dissapears")




