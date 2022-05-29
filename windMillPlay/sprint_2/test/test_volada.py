from unittest import TestCase

from windMillPlay.sprint_2.production.Logic import WindMillPlayGame
from windMillPlay.sprint_2.production.Data import *

class TestWindMillPlayGame(TestCase):
    def test_volada_case5(self):
        game =  WindMillPlayGame()
        position_list[1].ficha = 1
        position_list[1].empty = False
        position_list[9].ficha = 3
        position_list[9].empty = False
        position_list[17].ficha = 5
        position_list[17].empty = False
        self.assertEqual(True, game.volada(5))

    def test_volada_case5_false(self):
        game =  WindMillPlayGame()
        position_list[1].ficha = 1
        position_list[1].empty = False
        position_list[9].ficha = 3
        position_list[9].empty = False
        position_list[17].ficha = 6
        position_list[17].empty = False
        self.assertEqual(False, game.volada(6))

    def test_volada_case6(self):
        game =  WindMillPlayGame()
        position_list[1].ficha = 1
        position_list[1].empty = False
        position_list[9].ficha = 3
        position_list[9].empty = False
        position_list[17].ficha = 5
        position_list[17].empty = False
        self.assertEqual(True, game.volada(5))

    def test_volada_case6_false(self):
        game =  WindMillPlayGame()
        position_list[1].ficha = 1
        position_list[1].empty = False
        position_list[9].ficha = 3
        position_list[9].empty = False
        position_list[17].ficha = 5
        position_list[17].empty = False
        self.assertEqual(False, game.volada(5))

