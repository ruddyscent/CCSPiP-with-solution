import unittest
from graph import DiGraph


class TestDiGraph(unittest.TestCase):
    """
    A test case for the DiGraph class.

    This test case includes tests for adding edges to a directed graph.
    """

    def setUp(self):
        """
        Set up the test case by creating an empty DiGraph instance.
        """
        self.graph = DiGraph([])

    def test_add_edge(self):
        """
        Test the add_edge method of the DiGraph class.

        This test checks if the edge count is updated correctly after adding an edge,
        and if the edges for the vertices are updated correctly.
        """
        self.assertEqual(self.graph.edge_count, 0)
        self.graph.add_edge_by_vertices('A', 'B')
        self.assertEqual(self.graph.edge_count, 1)
        self.assertEqual(len(self.graph.edges_for_vertex('A')), 1)
        self.assertEqual(len(self.graph.edges_for_vertex('B')), 1)

    def test_add_edge_by_indices(self):
        """
        Test the add_edge_by_indices method of the DiGraph class.

        This test checks if the edge count is updated correctly after adding an edge,
        and if the edges for the vertices are updated correctly.
        """
        self.assertEqual(self.graph.edge_count, 0)
        self.graph.add_edge_by_indices(0, 1)
        self.assertEqual(self.graph.edge_count, 1)
        self.assertEqual(len(self.graph.edges_for_vertex('A')), 1)
        self.assertEqual(len(self.graph.edges_for_vertex('B')), 1)

    def test_add_edge_by_vertices(self):
        """
        Test the add_edge_by_vertices method of the DiGraph class.

        This test checks if the edge count is updated correctly after adding an edge,
        and if the edges for the vertices are updated correctly.
        """
        self.assertEqual(self.graph.edge_count, 0)
        self.graph.add_edge_by_vertices('A', 'B')
        self.assertEqual(self.graph.edge_count, 1)
        self.assertEqual(len(self.graph.edges_for_vertex('A')), 1)
        self.assertEqual(len(self.graph.edges_for_vertex('B')), 1)


if __name__ == '__main__':
    unittest.main()