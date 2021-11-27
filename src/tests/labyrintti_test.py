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

        self.assertEqual(self.lab.tulosta()[0][0], ".")

    def test_koordinaatti_ok(self):
        self.lab.luo()
        self.lab.dfs(0,0)

        self.assertEqual(self.lab.alku_ja_loppu(["0","0"]), (0,0))

    def test_koordinaatti_liian_pitka(self):
        self.lab.luo()
        self.lab.dfs(0,0)
        try:
            self.lab.alku_ja_loppu(["0","0","0"])
        except ValueError:
            pass
        else:
            raise AssertionError("ValueError was not raised")

    def test_x_koordinaatti_liian_iso(self):
        self.lab.luo()
        self.lab.dfs(0,0)
        try:
            self.lab.alku_ja_loppu(["5","5"])
        except ValueError:
            pass
        else:
            raise AssertionError("ValueError was not raised")

    def test_y_koordinaatti_liian_pitka(self):
        self.lab.luo()
        self.lab.dfs(0,0)
        try:
            self.lab.alku_ja_loppu(["0","5"])
        except ValueError:
            pass
        else:
            raise AssertionError("ValueError was not raised")

    def test_koordinaatti_seinaa(self):
        self.lab.luo()
        try:
            self.lab.alku_ja_loppu(["0","0"])
        except ValueError:
            pass
        else:
            raise AssertionError("ValueError was not raised")
    