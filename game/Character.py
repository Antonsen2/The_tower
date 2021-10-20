from data.item_data import items
from data.npc_data import monsters


class Character:

    def __init__(self, name, ap, hp):
        self.hp = hp
        self.name = name
        self.ap = ap


class Player(Character):

    def __init__(self):
        super().__init__("Hero", 100, 100)
        self.inventory = []
        self.current_floor = 0
        self.armor = 1
        self.equipped = []


    def print_inventory(self):
        print("Your inventory contains: ")
        for i in self.inventory:
            print(i["name"])



class Npc(Character):

    def __init__(self, i):
        super().__init__(monsters[i]['name'], monsters[i]['ap'], monsters[i]['hp'])



