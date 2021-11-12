import unittest
from labyrintti import Labyrintti

class TestLabyrintti(unittest.TestCase):
    def setUp(self):
        self.lab = Labyrintti(4,4)

    def test_luonti_ok(self):
        self.lab.luo()
        
        self.assertEqual(len(self.lab.labyrintti), 4)

    def test_tulostus_ok(self):
        self.lab.luo()
        self.lab.tulosta()

        self.assertEqual(self.lab.labyrintti[0][0], ".")
        
