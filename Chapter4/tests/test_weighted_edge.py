import unittest
from weighted_edge import WeightedEdge

class TestWeightedEdge(unittest.TestCase):
    def setUp(self):
        self.edge = WeightedEdge(1, 2, 3.0)

    def test_reversed(self):
        reversed_edge = self.edge.reversed()
        self.assertEqual(reversed_edge.u, 2)
        self.assertEqual(reversed_edge.v, 1)
        self.assertEqual(reversed_edge.weight, 3.0)

    def test_lt(self):
        other_edge = WeightedEdge(3, 4, 4.0)
        self.assertTrue(self.edge < other_edge)

    def test_str(self):
        self.assertEqual(str(self.edge), "1 3.0> 2")

if __name__ == '__main__':
    unittest.main()