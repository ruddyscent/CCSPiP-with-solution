import unittest
from edge import Edge

class TestEdge(unittest.TestCase):
    def setUp(self):
        self.edge = Edge(1, 2)

    def test_reversed(self):
        reversed_edge = self.edge.reversed()
        self.assertEqual(reversed_edge.u, 2)
        self.assertEqual(reversed_edge.v, 1)

    def test_str(self):
        self.assertEqual(str(self.edge), "1 -> 2")

if __name__ == '__main__':
    unittest.main()