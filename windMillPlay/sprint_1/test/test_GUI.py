import unittest
from windMillPlay.sprint_1.production.GUI import WindMillPlay


class TestWindMillPlay(unittest.TestCase):
    def test_create_board(self):
        gameGUI = WindMillPlay()
        self.assertEqual(True, gameGUI.state)


if __name__ == '__main__':
    unittest.main()