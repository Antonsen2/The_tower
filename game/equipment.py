from game.equip import Equip


class Equipment:
    def __init__(self):
        self.hands = Equip('hands', 2)
        self.helm = Equip('helm', 1)
        self.chest = Equip('chest', 1)
        self.legs = Equip('legs', 1)


    def equip_this(self, item):

        print(item)
        # if i.slot == "hands":
        #     self.hands.equip(item)
        # if i.slot == "helm":
        #     self.helm.equip(item)
        # if i.slot == "chest":
        #     self.chest.equip(item)
        # if i.slot == "legs":
        #     self.legs.equip(item)








