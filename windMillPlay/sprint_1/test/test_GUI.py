import unittest
from unittest import *
from unittest import TestCase
from windMillPlay.sprint_1.production.Data import Position
from windMillPlay.sprint_1.production.GUI import WindMillPlay

class TestWindMillPlay(TestCase):
    def test_create_board(self):
        gameGUI = WindMillPlay()
        self.assertEqual(True, gameGUI.state)

    def test_validate_position(self):
        gameGUI = WindMillPlay()
        #Insertamos posiciones cercanas a los vértices
        self.assertEqual(True, gameGUI.validatePosition(185,45,185,90))

if __name__ == '__main__':
    unittest.main()



