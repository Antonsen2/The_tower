from data.npc_data import monsters
from equipment import Equipment


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
        super().__init__("Hero", 30, 250)
        self.inventory = []
        self.current_floor = 0
        self.armor = 30
        self.equipment = Equipment(self)

    def get_item(self, item_name, current_floor):
        found_item = None
        for item in current_floor.items:
            if item.name == item_name:
                found_item = item
                break
        if found_item:
            if found_item.pick_up:
                print(f"You pick up the {item_name} from the ground")
                current_floor.items.remove(found_item)
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
                    player.inventory.remove(i)
                    print(f"the potion heals you for {i.heals} hp")
                    break

    def print_inventory(self):
        print("Your inventory contains: ")
        for i in self.inventory:
            if i.equippable:
                print(f"a {i.name} with {i.bonus_ap} bonus ap and {i.bonus_armor} bonus armor")
            else:
                print(i.description)

    def equip(self, item_name):
        for i in self.inventory:
            if item_name == i.name and i.equippable:
                match i.slot:
                    case "hands":
                        self.equipment.hands.equip(i)
                        self.inventory.remove(i)
                    case "helm":
                        self.equipment.head.equip(i)
                        self.inventory.remove(i)
                    case "chest":
                        self.equipment.chest.equip(i)
                        self.inventory.remove(i)
                    case "legs":
                        self.equipment.legs.equip(i)
                        self.inventory.remove(i)

    def unequip(self, item_name):
        equipment = [self.equipment.hands.items, self.equipment.head.items,
                     self.equipment.chest.items, self.equipment.legs.items]
        for i in equipment:
            for x in i:
                if item_name == x.name:
                    match x.slot:
                        case "hands":
                            self.equipment.hands.items.remove(x)
                            self.inventory.append(x)
                            self.equipment.equipment_stats()
                        case "helm":
                            self.equipment.head.items.remove(x)
                            self.inventory.append(x)
                            self.equipment.equipment_stats()
                        case "chest":
                            self.equipment.chest.items.remove(x)
                            self.inventory.append(x)
                            self.equipment.equipment_stats()
                        case "legs":
                            self.equipment.legs.items.remove(x)
                            self.inventory.append(x)
                            self.equipment.equipment_stats()
