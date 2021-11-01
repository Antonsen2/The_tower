import unittest

from game import Game


class TestClimb(unittest.TestCase):

    def test_climb_up(self):
        game = Game()
        game.climb_up()
        self.assertEqual(game.player.current_floor, 1)

    def test_descend(self):
        game = Game()
        game.player.current_floor = 2
        game.descend()
        self.assertEqual(game.player.current_floor, 1)