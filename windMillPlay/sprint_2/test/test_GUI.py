import unittest
from unittest import TestCase
from windMillPlay.sprint_2.production.GUI import *
from windMillPlay.sprint_2.production.Data import *

class TestWindMillPlay(TestCase):

    gameGUI = WindMillPlay()

    def test_create_board(self):

        self.assertEqual(True, self.gameGUI.state)

    def test_validate_positive_position(self):
        #Insertamos posiciones cercanas a los vértices
        self.assertEqual(True, self.gameGUI.validatePosition(116, 116, 377, 116))

    def test_not_validate_positive_position(self):
        #Insertamos posiciones cercanas a los vértices
        self.assertFalse(False, self.gameGUI.validatePosition(30,377,116, 116))

    def test_not_validate_negative_position(self):
        #Insertamos posiciones cercanas a los vértices
        self.assertFalse(False, self.gameGUI.validatePosition(116, 116,-45,-30))

if __name__ == '__main__':
    unittest.main()



