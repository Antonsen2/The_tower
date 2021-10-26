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


    def use_item(self, item_name, player):
        for i in self.inventory:
            if item_name == i["name"] and i["usable"]:
                if item_name == "potion":
                    player.hp += i["heals"]
                    print(f"the potion heals you for {i['heals']} hp")

    def print_inventory(self):
        print("Your inventory contains: ")
        for i in self.inventory:
            print(i["name"])
#  toDO make it so that you can only equip limited stuff. It makes no sense to be able to equip several weapons.
    def equip(self, item_name):
        for i in self.inventory:
            if item_name == i["name"] and i["equippable"]:
                self.equipped.append(i)
                self.inventory.remove(i)
            else:
                print(f"You can't equip {item_name}")

    def print_character(self, player):
        print(f"your current attack power is {player.ap}")
        print(f"your current hit points is {player.hp}")
        print("You have the following equipped:")
        for i in self.equipped:
            print(i["name"])

    def equipped_stats(self, player):
        for i in self.equipped:
            player.ap += i["bonus_ap"]
            if i["bonus_armor"]:
                player.armor += i["bonus_armor"]











