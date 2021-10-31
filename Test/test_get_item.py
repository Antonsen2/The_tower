from Game import Game

import unittest


class TestItem(unittest.TestCase):
    def test_get_item(self):
        game = Game()
        current_floor = game.map.get_current_floor(game.player.current_floor)
        target_item = [item for item in current_floor.items if item.name == "shield"]
        game.player.get_item("shield", current_floor)
        items_in_floor = current_floor.items
        self.assertTrue(target_item not in items_in_floor)


    def test_drop_item(self):
        game = Game()
        current_floor = game.map.get_current_floor(game.player.current_floor)
        game.player.get_item("shield", current_floor)

        game.climb_up()
        current_floor = game.map.get_current_floor(game.player.current_floor)
        game.player.drop_item("shield", current_floor)

        target_item = [item for item in current_floor.items if item.name == "shield"]
        items_in_floor = current_floor.items
        self.assertEqual(target_item,  items_in_floor)

    def test_get_item_to_inv(self):
        game = Game()
        current_floor = game.map.get_current_room(game.player.current_floor)
        item = current_floor.items[1]
        game.player.get_item("shield", current_floor)
        inventory = game.player.inventory
        self.assertTrue(item in inventory)
