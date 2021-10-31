class Equip:
    def __init__(self, slot, max_items):
        self.slot = slot
        self.items = []
        self.max_items = max_items


    def equip(self, item):
        if len(self.items < self.max_items):
            self.items.append(item)
            print(self.items)
        else:
            print("There is no room to equip that")
