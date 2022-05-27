import unittest
from unittest import TestCase
from windMillPlay.sprint_1.production.GUI import WindMillPlay

class TestWindMillPlay(TestCase):

    def test_create_board(self):
        gameGUI = WindMillPlay()
        self.assertEqual(True, gameGUI.state)

    def test_validate_positive_position(self):
        gameGUI = WindMillPlay()
        #Insertamos posiciones cercanas a los vértices
        self.assertEqual(True, gameGUI.validatePosition(185,45,185,45))

    def test_not_validate_positive_position(self):
        gameGUI = WindMillPlay()
        #Insertamos posiciones cercanas a los vértices
        self.assertFalse(False,gameGUI.validatePosition(185,45,185,1000))

    def test_not_validate_negative_position(self):
        gameGUI = WindMillPlay()
        #Insertamos posiciones cercanas a los vértices
        self.assertFalse(False,gameGUI.validatePosition(60,45,-45,-30))

if __name__ == '__main__':
    unittest.main()



