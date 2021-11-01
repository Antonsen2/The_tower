from data.item_data import items
from data.npc_data import monsters
from game_files.utils import item_creator

class Items:
    def __init__(self, player, map):
        self.player = player
        self.map = map
        self.floor_challenge = None
        self.found_item = []
        self.monsters = monsters
        self.items = items



    # @staticmethod
    # def get_current_item(name: str) -> dict:
    #     for item in items:
    #         if name == item['name']:
    #             return item


    # def boss_drop(self, current_floor):
    #     current_floor.items.append(self.monsters[self.player.current_floor]["drop"])

   # self.map.map2[self.player.current_floor]['items'].append(self.monsters[self.player.current_floor]["drop"])











