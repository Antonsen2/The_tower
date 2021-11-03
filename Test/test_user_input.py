import builtins
import unittest
from unittest.mock import patch
from game import Game
from game_files import item

from data.item_data import items
from utils import item_creator


class TestUserInput(unittest.TestCase):


    @patch("builtins.input", return_value="equip knife")
    def test_equip_item_input(self, input):
        game = Game()
        item = item_creator("i2")
        game.player.inventory.append(item)
        game.user_input()
        self.assertTrue(item in game.player.equipment.hands.items)

    @patch("builtins.input", return_value="use potion")
    def test_use_item_input(self, input):
        game = Game()
        item = item_creator("i3")
        game.player.inventory.append(item)
        game.user_input()
        self.assertEqual(game.player.hp, 250)

    @patch("builtins.input", return_value="fight")
    def test_fight_input(self, input):
        game = Game()
        game.user_input()
        self.assertTrue(game.engage)

