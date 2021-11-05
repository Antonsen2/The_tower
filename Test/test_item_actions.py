from game import Game
from utils import item_creator
import unittest


class TestItem(unittest.TestCase):
    def test_get_item(self):
        game = Game()
        current_floor = game.map.get_current_floor(game.player.current_floor)
        item = item_creator("i2")
        current_floor.items.append(item)
        game.player.get_item("knife", current_floor)
        items_in_floor = current_floor.items
        self.assertTrue(item not in items_in_floor)


    def test_drop_item(self):
        game = Game()
        item = item_creator("i5")
        game.player.inventory.append(item)

        game.climb_up()
        current_floor = game.map.get_current_floor(game.player.current_floor)
        game.player.drop_item("shield", current_floor)

        target_item = [item for item in current_floor.items if item.name == "shield"]
        items_in_floor = current_floor.items
        self.assertEqual(target_item,  items_in_floor)

    def test_get_item_to_inv(self):
        game = Game()
        current_floor = game.map.get_current_floor(game.player.current_floor)
        item = item_creator("i2")
        current_floor.items.append(item)
        game.player.get_item("knife", current_floor)
        inventory = game.player.inventory

        self.assertTrue(item in inventory)
