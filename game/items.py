from data.item_data import items
from data.npc_data import monsters

class Items:
    def __init__(self, player, map):
        self.item = items
        self.player = player
        self.map = map
        self.floor_challenge = None
        self.found_item = []
        self.monsters = monsters

    @staticmethod
    def get_current_item(name: str) -> dict:
        for item in items:
            if name == item['name']:
                return item

    def print_current_item_in_room(self):
        for item in self.item:
            if item['id'] in self.map.map2[self.player.current_floor]['items']:
                if item["visible"]:
                    # self.found_item.append(item)
                    print("There is", item['description'], "in this room")

    def get_item(self, item_name):
        found_item = None
        for item in self.item:
            if item["name"] == item_name:
                found_item = item
                break
        if found_item:
            if found_item["pick_up"]:
                print(f"You pick up the {item_name} from the ground")
                self.map.map2[self.player.current_floor]['items'].remove(found_item["id"])
                self.player.inventory.append(found_item)
            else:
                print(f"You can see the {item_name} but there is no way for you to pick it up")
        else:
            print(f"There is no {item_name} in this room")

    def drop_item(self, item_name):
        for item in self.player.inventory:
            if item_name == item["name"]:
                self.player.inventory.remove(item)
                self.map.map2[self.player.current_floor]['items'].append(item["id"])

    def boss_drop(self):
        self.map.map2[self.player.current_floor]['items'].append(self.monsters[self.player.current_floor]["drop"])



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

        if self.item[0]["visible"]:
            chest_open = True
            while chest_open:
                self.print_chest()
                command1 = input("You can get the items or close to chest: ")
                match command1.lower().split():
                    case ["none"] | ["close"] | ["stop"]:
                        chest_open = False
                        self.item[0]["visible"] = False
                    case ["knife"] | ["potion"]:
                        item = self.get_current_item(command1)
                        if item:
                            self.player.inventory.append(item)
                            self.item[0]['contains'].remove(item["id"])
                    case _:
                        print(f"I dont understand {command1}")







