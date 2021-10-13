from game.Character import Player
from Map import Map
from data.item_data import items


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

