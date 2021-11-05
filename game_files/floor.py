from game_files.utils import item_creator


class Floor:
    def __init__(self, **floor):
        self.__dict__ = floor
        floor_items = []
        for item_id in self.items:
            if item_id:
                floor_items.append(item_creator(item_id))
        self.items = floor_items
