from unittest import TestCase

from GUI import WindMillPlay


class TestWindMillPlay(TestCase):
    def test_create_board(self):
        game = WindMillPlay()
        self.assertEqual(True, game.state)
