from unittest import TestCase

from windMillPlay.sprint_2.production.Logic import WindMillPlayGame
from windMillPlay.sprint_2.production.Data import *

class TestWindMillPlayGame(TestCase):
    def test_volada(self):
        game =  WindMillPlayGame()
        game.volada()

