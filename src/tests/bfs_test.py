import unittest
from bfs import BFS

lab = [['.', '.', '#', '#'], ['#', '.', '.', '#'], ['#', '#', '.', '.'], ['#', '#', '#', '.']]

class TestBFS(unittest.TestCase):
    def setUp(self):
        self.bfs = BFS(lab, 4, 4, (0,0), (3,3))
        self.bfs2 = BFS(lab, 4, 4, (0,0), (3,2))

    def test_haku_ok(self):
        etaisyys = self.bfs.syvyyshaku()

        self.assertEqual(etaisyys, 6)

    def test_reittia_ei_ole(self):
        etaisyys = self.bfs2.syvyyshaku()

        self.assertEqual(etaisyys, -1)
