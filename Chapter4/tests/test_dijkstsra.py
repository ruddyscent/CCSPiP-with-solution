import unittest
from dijkstra import dijkstra
from weighted_graph import WeightedGraph
from weighted_edge import WeightedEdge

class TestDijkstra(unittest.TestCase):
    def setUp(self):
        self.wg = WeightedGraph(['A', 'B', 'C', 'D'])
        self.wg.add_edge_by_indices(0, 1, 1)
        self.wg.add_edge_by_indices(1, 2, 2)
        self.wg.add_edge_by_indices(2, 3, 1)
        self.wg.add_edge_by_indices(0, 3, 3)

    def test_dijkstra(self):
        distances, path_dict = dijkstra(self.wg, 'A')
        self.assertEqual(distances, [0, 1, 3, 3])
        self.assertEqual(path_dict[1].weight, 1)
        self.assertEqual(path_dict[2].weight, 2)
        self.assertEqual(path_dict[3].weight, 3)

if __name__ == '__main__':
    unittest.main()