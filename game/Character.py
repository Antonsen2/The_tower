from data.item_data import items
from data.npc_data import monsters


class Character:

    def __init__(self, name, ap, hp):
        self.hp = hp
        self.name = name
        self.ap = ap


class Npc(Character):

    def __init__(self, i):
        super().__init__(monsters[i]['name'], monsters[i]['ap'], monsters[i]['hp'])


class Player(Character):

    def __init__(self):
        super().__init__("Hero", 200, 100)
        self.inventory = []
        self.current_floor = 0
        self.armor = 1
        self.equipped = []
        self.player = Player


    def print_inventory(self):
        print("Your inventory contains: ")
        for i in self.inventory:
            print(i["name"])

    def equip(self):
        command2 = input("What item would you like to equip?")
        for i in self.inventory:
            if command2 == i["name"] and i["equippable"]:
                self.equipped.append(i)
                self.inventory.remove(i)
            else:
                print(f"You can't equip {command2}")

    def print_equipped(self):
        print("You have the following equipped:")
        for i in self.equipped:
            print(i["name"])

    def equipped_stats(self, player):
        for i in self.equipped:
            player.ap += i["bonus_ap"]











