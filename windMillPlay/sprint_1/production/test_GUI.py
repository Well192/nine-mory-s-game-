from unittest import TestCase

from GUI import WindMillPlay


class TestWindMillPlay(TestCase):
    def test_create_board(self):
        gameGUI = WindMillPlay()
        self.assertEqual(True, gameGUI.state)
