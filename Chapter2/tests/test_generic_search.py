# tests_generic_search.py
# unit test of generic_search.py
# Copyright 2023 Kyungwon Chun
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import math
import random
import time
import unittest

import generic_search


class GenericSearchTestCase(unittest.TestCase):
    def test_linear_contains(self) -> None:
        self.assertTrue(generic_search.linear_contains([1, 5, 15, 15, 15, 15, 20], 5))

    def test_binary_contains(self) -> None:
        self.assertTrue(generic_search.binary_contains(["a", "d", "e", "f", "z"], "f"))
        self.assertFalse(generic_search.binary_contains(["john", "mark", "ronald", "sarah"], "sheila"))

    def test_linear_binary_compare_performance(self) -> None:
        n_samples: int = 10
        n_numbers: int = 1_000_000
        numbers: list[int] = [x for x in range(n_numbers)]
        keys: int = random.choices(numbers, k=n_samples)

        t: float = time.process_time()
        [generic_search.linear_contains(numbers, key) for key in keys]
        elapsed_time_linear: int = time.process_time() - t
        
        t: float = time.process_time()
        key: int = random.choice(numbers)
        [generic_search.binary_contains(numbers, key) for key in keys]
        elapsed_time_binary: int = time.process_time() - t

        self.assertGreater(elapsed_time_linear / elapsed_time_binary, 0.01 * n_numbers / math.log(n_numbers, 2))
        

class StackTestCase(unittest.TestCase):
    def test_stack(self) -> None:
        s: generic_search.Stack[int] = generic_search.Stack()
        s.push(1)
        s.push(2)
        s.push(3)
        self.assertEqual(s.pop(), 3)
        self.assertEqual(s.pop(), 2)
        self.assertEqual(s.pop(), 1)
        self.assertTrue(s.empty)


class NodeTestCase(unittest.TestCase):
    def test_node(self) -> None:
        n1: generic_search.Node[int] = generic_search.Node(1, None)
        n2: generic_search.Node[int] = generic_search.Node(2, n1)
        n3: generic_search.Node[int] = generic_search.Node(3, n2)
        self.assertEqual(n1.state, 1)
        self.assertEqual(n2.state, 2)
        self.assertEqual(n3.state, 3)
        self.assertEqual(n2.parent, n1)
        self.assertEqual(n3.parent, n2)
        self.assertEqual(n1.parent, None)


class DfsTestCase(unittest.TestCase):
    def test_dfs(self) -> None:
        self.assertEqual(
            generic_search.dfs(1, lambda x: x == 5, lambda x: [x + 1, x + 2, x + 3, x + 4])[0].state, 
            5)
        self.assertEqual(
            generic_search.dfs(1, lambda x: x == 5, lambda x: [(x + 1) % 5, (x + 2) % 5, (x + 3) % 5, (x + 4) % 5])[0],
            None)


class NodeToPathTestCase(unittest.TestCase):
    def test_node_to_path(self) -> None:
        n1: generic_search.Node[int] = generic_search.Node(1, None)
        n2: generic_search.Node[int] = generic_search.Node(2, n1)
        n3: generic_search.Node[int] = generic_search.Node(3, n2)
        self.assertEqual(generic_search.node_to_path(n3), [1, 2, 3])


class QueueTestCase(unittest.TestCase):
    def test_queue(self) -> None:
        q: generic_search.Queue[int] = generic_search.Queue()
        q.push(1)
        q.push(2)
        q.push(3)
        self.assertEqual(q.pop(), 1)
        self.assertEqual(q.pop(), 2)
        self.assertEqual(q.pop(), 3)
        self.assertTrue(q.is_empty())


class BfsTestCase(unittest.TestCase):
    def test_bfs(self) -> None:
        self.assertEqual(
            generic_search.bfs(1, lambda x: x == 5, lambda x: [x + 1, x + 2, x + 3, x + 4])[0].state, 
            5)
        self.assertEqual(
            generic_search.bfs(1, lambda x: x == 5, lambda x: [(x + 1) % 5, (x + 2) % 5, (x + 3) % 5, (x + 4) % 5])[0],
            None)


class PriorityQueueTestCase(unittest.TestCase):
    def test_priority_queue(self) -> None:
        pq: generic_search.PriorityQueue[int] = generic_search.PriorityQueue()
        pq.push(1)
        pq.push(2)
        pq.push(3)
        self.assertEqual(pq.pop(), 1)
        self.assertEqual(pq.pop(), 2)
        self.assertEqual(pq.pop(), 3)
        self.assertTrue(pq.empty)


class AStarTestCase(unittest.TestCase):
    def test_astar(self) -> None:
        self.assertEqual(
            generic_search.astar(1, lambda x: x == 5, lambda x: [x + 1, x + 2, x + 3, x + 4], lambda x: 0)[0].state, 
            5)
        self.assertEqual(
            generic_search.astar(1, lambda x: x == 5, lambda x: [(x + 1) % 5, (x + 2) % 5, (x + 3) % 5, (x + 4) % 5], lambda x: 0)[0],
            None)

        
if __name__ == '__main__':
    unittest.main()

