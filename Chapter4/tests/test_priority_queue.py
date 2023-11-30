import unittest
from priority_queue import PriorityQueue

class TestPriorityQueue(unittest.TestCase):
    def setUp(self):
        self.pq = PriorityQueue()

    def test_push_and_pop(self):
        self.pq.push(3)
        self.pq.push(1)
        self.pq.push(2)
        self.assertEqual(self.pq.pop(), 1)
        self.assertEqual(self.pq.pop(), 2)
        self.assertEqual(self.pq.pop(), 3)

    def test_empty(self):
        self.assertTrue(self.pq.empty)
        self.pq.push(1)
        self.assertFalse(self.pq.empty)

if __name__ == '__main__':
    unittest.main()