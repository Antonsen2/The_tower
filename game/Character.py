from data.npc_data import monsters

class Character:

    def __init__(self, name, ap, hp):
        self.hp = hp
        self.name = name
        self.ap = ap


class Player(Character):

    def __init__(self):
        super().__init__("Tja", 5, 20)
        self.inventory = "hej"
        self.current_floor = 0
        self.armor = 1


class Npc(Character):

    def __init__(self, i):
        super().__init__(monsters[i]['name'], monsters[i]['ap'], monsters[i]['hp'])


