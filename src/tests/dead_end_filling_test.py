import unittest
from dead_end_filling import DeadEndFilling

lab =  [['.', '.', '#', '#'],
        ['#', '.', '.', '#'],
        ['#', '#', '.', '.'],
        ['#', '#', '#', '.']]

lab2 = [[".",".",'.','.'],
        ['#','.','#','.'],
        ['.','.','.','#'],
        ['.','#','.','.']]

class TestBFS(unittest.TestCase):
    def setUp(self):
        self.def1 = DeadEndFilling(lab, 4, 4, (0,0), (3,3))
        self.def2 = DeadEndFilling(lab2, 4, 4, (0,0), (3,2))
    def test_ei_yhtaan_dead_endia(self):
        self.def1.dead_end_filling()

        self.assertEqual(self.def1.labyrintti[3][3], "polku")
    def test_tunnistaa_reunat_umpikujiksi(self):
        self.def2.dead_end_filling()

        self.assertEqual(self.def2.labyrintti[3][0], "#")
    def test_polun_pituus_oikein(self):
        self.def1.dead_end_filling()

        self.assertEqual(self.def1.polun_pituus(), 6)
