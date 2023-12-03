import unittest
from weighted_graph import WeightedGraph
from weighted_edge import WeightedEdge

class TestWeightedGraph(unittest.TestCase):
    def setUp(self):
        self.wg = WeightedGraph(['A', 'B', 'C'])

    def test_add_edge_by_indices(self):
        self.wg.add_edge_by_indices(0, 1, 1.0)
        self.assertEqual(len(self.wg.edges_for_index(0)), 1)
        self.assertEqual(self.wg.edges_for_index(0)[0], WeightedEdge(0, 1, 1.0))

    def test_add_edge_by_vertices(self):
        self.wg.add_edge_by_vertices('A', 'B', 1.0)
        self.assertEqual(len(self.wg.edges_for_index(0)), 1)
        self.assertEqual(self.wg.edges_for_index(0)[0], WeightedEdge(0, 1, 1.0))

    def test_neighbors_for_index_with_weights(self):
        self.wg.add_edge_by_indices(0, 1, 1.0)
        self.assertEqual(self.wg.neighbors_for_index_with_weights(0), [('B', 1.0)])

if __name__ == '__main__':
    unittest.main()