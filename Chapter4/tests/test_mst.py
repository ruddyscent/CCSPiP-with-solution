import unittest
from mst import mst, total_weight
from weighted_graph import WeightedGraph
from weighted_edge import WeightedEdge

class TestMST(unittest.TestCase):
    def setUp(self):
        self.wg = WeightedGraph(['A', 'B', 'C', 'D'])
        self.wg.add_edge_by_indices(0, 1, 1)
        self.wg.add_edge_by_indices(1, 2, 2)
        self.wg.add_edge_by_indices(2, 3, 1)
        self.wg.add_edge_by_indices(0, 3, 3)

    def test_mst(self):
        mst_edges = mst(self.wg)
        self.assertEqual(len(mst_edges), 3)
        self.assertEqual(total_weight(mst_edges), 4)

if __name__ == '__main__':
    unittest.main()