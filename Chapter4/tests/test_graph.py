import unittest
from graph import Graph, Edge

class TestGraph(unittest.TestCase):
    def setUp(self):
        self.graph = Graph([])

    def test_add_vertex(self):
        self.assertEqual(self.graph.vertex_count, 0)
        self.graph.add_vertex('A')
        self.assertEqual(self.graph.vertex_count, 1)
        self.graph.add_vertex('B')
        self.assertEqual(self.graph.vertex_count, 2)

    def test_remove_vertex(self):
        self.graph.add_vertex('A')
        self.graph.add_vertex('B')
        self.graph.add_vertex('C')
        self.graph.add_edge_by_vertices('A', 'B')
        self.graph.add_edge_by_vertices('B', 'C')
        self.assertEqual(self.graph.vertex_count, 3)
        self.assertEqual(self.graph.edge_count, 4)
        self.graph.remove_vertex('B')
        self.assertEqual(self.graph.vertex_count, 2)
        self.assertEqual(self.graph.edge_count, 0)

    def test_add_edge(self):
        self.graph.add_vertex('A')
        self.graph.add_vertex('B')
        self.graph.add_vertex('C')
        self.graph.add_edge_by_vertices('A', 'B')
        self.graph.add_edge_by_vertices('B', 'C')
        self.assertEqual(self.graph.edge_count, 4)
        self.assertEqual(len(self.graph.edges_for_vertex('A')), 1)
        self.assertEqual(len(self.graph.edges_for_vertex('B')), 2)
        self.assertEqual(len(self.graph.edges_for_vertex('C')), 1)

    def test_remove_edge(self):
        self.graph.add_vertex('A')
        self.graph.add_vertex('B')
        self.graph.add_vertex('C')
        self.graph.add_edge_by_vertices('A', 'B')
        self.graph.add_edge_by_vertices('B', 'C')
        self.assertEqual(self.graph.edge_count, 4)
        self.graph.remove_edge_by_vertices('A', 'B')
        self.assertEqual(self.graph.edge_count, 2)
        self.assertEqual(len(self.graph.edges_for_vertex('A')), 0)
        self.assertEqual(len(self.graph.edges_for_vertex('B')), 1)
        self.assertEqual(len(self.graph.edges_for_vertex('C')), 1)

    def test_neighbors_for_vertex(self):
        self.graph.add_vertex('A')
        self.graph.add_vertex('B')
        self.graph.add_vertex('C')
        self.graph.add_edge_by_vertices('A', 'B')
        self.graph.add_edge_by_vertices('B', 'C')
        self.assertEqual(self.graph.neighbors_for_vertex('A'), ['B'])
        self.assertEqual(self.graph.neighbors_for_vertex('B'), ['A', 'C'])
        self.assertEqual(self.graph.neighbors_for_vertex('C'), ['B'])

    def test_edges_for_vertex(self):
        self.graph.add_vertex('A')
        self.graph.add_vertex('B')
        self.graph.add_vertex('C')
        self.graph.add_edge_by_vertices('A', 'B')
        self.graph.add_edge_by_vertices('B', 'C')
        self.assertEqual(len(self.graph.edges_for_vertex('A')), 1)
        self.assertEqual(len(self.graph.edges_for_vertex('B')), 2)
        self.assertEqual(len(self.graph.edges_for_vertex('C')), 1)

    def test_str(self):
        self.graph.add_vertex('A')
        self.graph.add_vertex('B')
        self.graph.add_vertex('C')
        self.graph.add_edge_by_vertices('A', 'B')
        self.graph.add_edge_by_vertices('B', 'C')
        expected_output = "A -> ['B']\nB -> ['A', 'C']\nC -> ['B']\n"
        self.assertEqual(str(self.graph), expected_output)

if __name__ == '__main__':
    unittest.main()