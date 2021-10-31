from data.item_data import items
from data.npc_data import monsters
from equipment import Equipment
from game.equip import Equip


class Character:

    def __init__(self, name, ap, hp):
        self.hp = hp
        self.name = name
        self.ap = ap


class Npc(Character):

    def __init__(self, i):
        super().__init__(monsters[i]['name'], monsters[i]['ap'], monsters[i]['hp'],)
        self.drop = monsters[i]["drop"]

class Player(Character):

    def __init__(self):
        super().__init__("Hero", 200, 100)
        self.inventory = []
        self.current_floor = 0
        self.armor = 1
        self.equipped = {
                        "hands": [],
                        "helm": [],
                        "chest": [],
                        "legs": [],
        }


    def get_item(self, item_name, current_room):
        found_item = None
        for item in current_room.items:
            if item.name == item_name:
                found_item = item
                break
        if found_item:
            if found_item.pick_up:
                print(f"You pick up the {item_name} from the ground")
                current_room.items.remove(found_item)
                self.inventory.append(found_item)
            else:
                print(f"You can see the {item_name} but you can't pick it up")
        else:
            print(f"There is no {item_name} in this room")

    def drop_item(self, item_name, current_floor):
        for item in self.inventory:
            if item_name == item.name:
                self.inventory.remove(item)
                current_floor.items.append(item)

    def use_item(self, item_name, player):
        for i in self.inventory:
            if item_name == i.name and i.usable:
                if item_name == "potion":
                    player.hp += i.heals
                    print(f"the potion heals you for {i.heals} hp")

    def print_inventory(self):
        print("Your inventory contains: ")
        for i in self.inventory:
            print(i.name)

    def equip(self, item_name):

        for i in self.inventory:
            if item_name == i.name and i.equippable:
                if i.slot == "hands":
                    if len(self.equipped["hands"]) < 2:
                        print(f"you equip the {i.name}")
                        self.equipped["hands"].append(i)
                    else:
                        print("Your hands are full, try to unequip something from your hands")
                if i.slot == "helm":
                    if len(self.equipped["helm"]) < 1:
                        print(f"you equip the {i.name}")
                        self.equipped["helm"].append(i)
                    else:
                        print("You are already wearing a helmet, try to unequip it")
                if i.slot == "chest":
                    if len(self.equipped["chest"]) < 1:
                        print(f"you equip the {i.name}")
                        self.equipped["chest"].append(i)
                    else:
                        print("You are already wearing a chest piece, try to unequip it")
                if i.slot == "legs":
                    if len(self.equipped["legs"]) < 1:
                        print(f"you equip the {i.name}")
                        self.equipped["legs"].append(i)
                    else:
                        print("You are already wearing something on your legs, try to unequip it")



    def print_character(self, player):
        print(f"your current attack power is {player.ap}")
        print(f"your current hit points is {player.hp}")
        print("You have the following equipped:")
        for i in self.equipped:
            pass

    def equipped_stats(self, player):

        for x in self.equipped["hands"]:
            if x["bonus_armor"]:
                player.armor += x["bonus_armor"]
            print(x["bonus_armor"])












