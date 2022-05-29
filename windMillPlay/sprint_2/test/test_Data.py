import unittest
from windMillPlay.sprint_2.production.Data import Position


class TestPosition(unittest.TestCase):
    def test_in_the_radio_true(self):
        posicion = Position(10, 10)
        punto = [11, 12]  # dentro del radio permitido
        self.assertTrue(posicion.in_the_radio(punto[0], punto[1]))

    def test_in_the_radio_False(self):
        posicion = Position(10, 10)
        punto = [20, 20]  # fuera del radio permitido
        self.assertFalse(posicion.in_the_radio(punto[0], punto[1]))

if __name__ == '__main__':
    unittest.main()
