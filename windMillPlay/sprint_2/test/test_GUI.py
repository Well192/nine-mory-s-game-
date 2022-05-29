import unittest
from unittest import TestCase
from windMillPlay.sprint_2.production.GUI import *
from windMillPlay.sprint_2.production.Data import *

class TestWindMillPlay(TestCase):
    def test_create_board(self):
        gameGUI = WindMillPlay()
        self.assertEqual(True, gameGUI.state)

    def test_validate_positive_position(self):
        gameGUI = WindMillPlay()
        #Insertamos posiciones cercanas a los vértices
        self.assertEqual(True, gameGUI.validatePosition(116, 116, 377, 116))

    def test_not_validate_positive_position(self):
        gameGUI = WindMillPlay()
        #Insertamos posiciones cercanas a los vértices
        self.assertFalse(False,gameGUI.validatePosition(30,377,116, 116))

    def test_not_validate_negative_position(self):
        gameGUI = WindMillPlay()
        #Insertamos posiciones cercanas a los vértices
        self.assertFalse(False,gameGUI.validatePosition(116, 116,-45,-30))

if __name__ == '__main__':
    unittest.main()



