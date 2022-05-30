from unittest import TestCase

from windMillPlay.sprint_2.production.Logic import WindMillPlayGame
from windMillPlay.sprint_2.production.Data import *

class TestWindMillPlayGame(TestCase):

    def test_volada_case1(self):
        game =  WindMillPlayGame()

        position_list[0].ficha = 1
        position_list[0].empty = False
        position_list[6].ficha = 3
        position_list[6].empty = False
        position_list[7].ficha = 5
        position_list[7].empty = False
        self.assertEqual(True, game.volada(5))

    def test_volada_case1_2(self):

        game =  WindMillPlayGame()

        position_list[8].ficha = 1
        position_list[8].empty = False
        position_list[14].ficha = 3
        position_list[14].empty = False
        position_list[15].ficha = 5
        position_list[15].empty = False
        self.assertEqual(True, game.volada(5))

    def test_volada_case1_3(self):

        game =  WindMillPlayGame()

        position_list[16].ficha = 1
        position_list[16].empty = False
        position_list[22].ficha = 3
        position_list[22].empty = False
        position_list[23].ficha = 5
        position_list[23].empty = False
        self.assertEqual(True, game.volada(5))

    def test_volada_case2(self):
        game =  WindMillPlayGame()

        position_list[0].ficha = 2
        position_list[0].empty = False
        position_list[6].ficha = 4
        position_list[6].empty = False
        position_list[7].ficha = 6
        position_list[7].empty = False
        self.assertEqual(True, game.volada(4))

    def test_volada_case2_2(self):

        game =  WindMillPlayGame()

        position_list[8].ficha = 2
        position_list[8].empty = False
        position_list[14].ficha = 4
        position_list[14].empty = False
        position_list[15].ficha = 6
        position_list[15].empty = False
        self.assertEqual(True, game.volada(2))

    def test_volada_case2_3(self):

        game =  WindMillPlayGame()

        position_list[16].ficha = 2
        position_list[16].empty = False
        position_list[22].ficha = 4
        position_list[22].empty = False
        position_list[23].ficha = 6
        position_list[23].empty = False
        self.assertEqual(True, game.volada(6))

    def test_volada_case3(self):

        game =  WindMillPlayGame()

        position_list[0].ficha = 1
        position_list[0].empty = False
        position_list[1].ficha = 3
        position_list[1].empty = False
        position_list[2].ficha = 5
        position_list[2].empty = False
        self.assertEqual(True, game.volada(5))

    def test_volada_case3_2(self):

        game =  WindMillPlayGame()

        position_list[8].ficha = 1
        position_list[8].empty = False
        position_list[9].ficha = 3
        position_list[9].empty = False
        position_list[10].ficha = 5
        position_list[10].empty = False
        self.assertEqual(True, game.volada(5))

    def test_volada_case3_3(self):

        game =  WindMillPlayGame()

        position_list[16].ficha = 1
        position_list[16].empty = False
        position_list[17].ficha = 3
        position_list[17].empty = False
        position_list[18].ficha = 5
        position_list[18].empty = False
        self.assertEqual(True, game.volada(5))

    def test_volada_case4(self):
        game =  WindMillPlayGame()

        position_list[0].ficha = 2
        position_list[0].empty = False
        position_list[1].ficha = 4
        position_list[1].empty = False
        position_list[2].ficha = 6
        position_list[2].empty = False
        self.assertEqual(True, game.volada(4))

    def test_volada_case4_2(self):

        game =  WindMillPlayGame()

        position_list[8].ficha = 2
        position_list[8].empty = False
        position_list[9].ficha = 4
        position_list[9].empty = False
        position_list[10].ficha = 6
        position_list[10].empty = False
        self.assertEqual(True, game.volada(2))

    def test_volada_case4_3(self):

        game =  WindMillPlayGame()

        position_list[16].ficha = 2
        position_list[16].empty = False
        position_list[17].ficha = 4
        position_list[17].empty = False
        position_list[18].ficha = 6
        position_list[18].empty = False
        self.assertEqual(True, game.volada(6))

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

