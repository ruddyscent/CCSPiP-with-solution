import sys
sys.path.insert(0, '..') # so we can access the Chapter2 package in the parent directory

import unittest
from weighted_graph import WeightedGraph
from weighted_edge import WeightedEdge
from konigsberg import KonigsbergNode, goal_test, traverse

class TestKonigsberg(unittest.TestCase):
    def setUp(self):
        self.konigsberg = WeightedGraph(["A", "B", "C", "D"])
        self.konigsberg.add_edge_by_vertices("A", "B", 1)
        self.konigsberg.add_edge_by_vertices("A", "B", 2)
        self.konigsberg.add_edge_by_vertices("B", "C", 3)
        self.konigsberg.add_edge_by_vertices("A", "C", 4)
        self.konigsberg.add_edge_by_vertices("B", "D", 5)
        self.konigsberg.add_edge_by_vertices("B", "D", 6)
        self.konigsberg.add_edge_by_vertices("C", "D", 7)

    def test_goal_test(self):
        node = KonigsbergNode(WeightedEdge("A", "B", 1), 7, None)
        self.assertTrue(goal_test(node, 7))
        self.assertFalse(goal_test(node, 6))

    def test_traverse(self):
        for start in ["A", "B", "C", "D"]:
            node = traverse(self.konigsberg, start)
            self.assertIsNone(node)

if __name__ == '__main__':
    unittest.main()