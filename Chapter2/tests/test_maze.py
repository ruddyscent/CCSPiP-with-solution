# tests_maze.py
# unit test of maze.py
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
import unittest

from typing import Callable, Optional
import maze


class MazeTestCase(unittest.TestCase):
    m: maze.Maze = maze.Maze(
        rows=3, columns=3, sparseness=0, start=maze.MazeLocation(0, 0), goal=maze.MazeLocation(2, 2)
        )
    
    def test_goal_test(self) -> None:
        self.assertTrue(self.m.goal_test(maze.MazeLocation(2, 2)))
        self.assertFalse(self.m.goal_test(maze.MazeLocation(2, 1)))

    def test_successors(self) -> None:
        successors: list[maze.MazeLocation] = self.m.successors(maze.MazeLocation(1, 1))
        self.assertCountEqual(successors, [maze.MazeLocation(1, 0), maze.MazeLocation(1, 2), maze.MazeLocation(0, 1), maze.MazeLocation(2, 1)])

    # def test_astar(self) -> None:
    #     distance: Callable[[maze.MazeLocation], float] = maze.manhattan_distance(self.m.goal)
    #     solution3: Optional[maze.Node[maze.MazeLocation]] = maze.astar(
    #         self.m.start, self.m.goal_test, self.m.successors, distance
    #         )
    #     self.assertIsNotNone(solution3)
        
    def test_distance(self) -> None:
        distance: Callable[[maze.MazeLocation], float] = maze.manhattan_distance(self.m.goal)
        self.assertEqual(distance(maze.MazeLocation(0, 0)), 2 + 2)

    def test_euclidean_distance(self) -> None:
        distance: Callable[[maze.MazeLocation], float] = maze.euclidean_distance(self.m.goal)
        self.assertEqual(distance(maze.MazeLocation(0, 0)), math.sqrt(2**2 + 2**2))


if __name__ == '__main__':
    unittest.main()
