from game_files.equip import Equip


class Equipment:
    def __init__(self, player):
        self.hands = Equip('hands', 2)
        self.head = Equip('head', 1)
        self.chest = Equip('chest', 1)
        self.legs = Equip('legs', 1)
        self.player = player

    def print_equipment(self):
        equipment = [self.hands, self.head, self.chest, self.legs]
        print(f"your current attack power is {self.player.ap}")
        print(f"your current hit points is {int(self.player.hp)}")
        print("You have the following equipped:")
        for i in equipment:
            for x in i.items:
                print(f"a {x.name} with {x.bonus_ap} bonus ap and {x.bonus_armor} bonus armor")


    def equipment_stats(self):
        equipment = [self.hands, self.head, self.chest, self.legs]
        for i in equipment:
            for x in i.items:
                self.player.ap += x.bonus_ap
                self.player.armor += x.bonus_armor















