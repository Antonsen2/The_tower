from game.Character import Player
from Map import Map
from data.item_data import items


class Items:
    def __init__(self, player, map):
        self.item = None
        self.player = player
        self.map = map

    def current_item_in_room(self):
        for self.item in items:
            if self.item['id'] in self.map.map2[self.player.current_floor]['items']:
                print("There is ", self.item['description'], "")

    def open(self):
        ids = []
        for item in items:
           # if item['id'] in self.map.map2[self.player.current_floor]['items']:
            if item["container"]:
                for i in item['contains']:
                    ids.append(i)
        for item in items:
            for id2 in ids:
                if item['id'] == id2:
                    print(item['name'])




                  #  if item["contains"][0] == item['id']:
                       # print(items['name'])
                       #  print(f"the chest contains {self.item['contains'][0]}")
                    # coomand = input("")



