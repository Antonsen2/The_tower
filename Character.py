

class Character:

    def __init__(self, name, ap, hp):
        self.hp = hp
        self.name = name
        self.ap = ap


class Player(Character):

    def __init__(self, name, ap, hp):
        super().__init__(name, ap, hp)
        self.inventory = "hej"
        self.current_floor = 0


class Npc(Character):

    def __init__(self, name, ap, hp):
        super().__init__(name, ap,  hp)


