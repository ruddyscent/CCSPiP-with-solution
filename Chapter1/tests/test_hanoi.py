# test_hanoi.py
# unit test of hanoi
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

import unittest

from typing import List

import hanoi


class StackTestCase(unittest.TestCase):
    def test_push(self) -> None:
        stack: hanoi.Stack[int] = hanoi.Stack[int]()
        stack.push(1)
        self.assertEqual(stack._container, [1])

    def test_pop(self) -> None:
        stack: hanoi.Stack[int] = hanoi.Stack[int]()
        stack._container = [1]
        self.assertEqual(stack.pop(), 1)


class HanoiTestCase(unittest.TestCase):
    def test_hanoi3(self) -> None:
        num_discs: int = 3
        tower_a: hanoi.Stack[int] = hanoi.Stack()
        tower_b: hanoi.Stack[int] = hanoi.Stack()
        tower_c: hanoi.Stack[int] = hanoi.Stack()
        for i in range(1, num_discs + 1):
            tower_a.push(i)

        hanoi.hanoi(tower_a, tower_c, tower_b, num_discs)
        self.assertListEqual(tower_a._container, [])
        self.assertListEqual(tower_b._container, [])
        self.assertListEqual(tower_c._container, list(range(1, num_discs + 1)))

    def test_hanoi10(self) -> None:
        num_discs: int = 10
        tower_a: hanoi.Stack[int] = hanoi.Stack()
        tower_b: hanoi.Stack[int] = hanoi.Stack()
        tower_c: hanoi.Stack[int] = hanoi.Stack()
        for i in range(1, num_discs + 1):
            tower_a.push(i)

        hanoi.hanoi(tower_a, tower_c, tower_b, num_discs)
        self.assertListEqual(tower_a._container, [])
        self.assertListEqual(tower_b._container, [])
        self.assertListEqual(tower_c._container, list(range(1, num_discs + 1)))

    def test_hanoi_n_20_5(self) -> None:
        num_discs: int = 20 
        num_towers: int = 5 # num_towers must be greater than 3
        towers: List[hanoi.Stack[int]] = [hanoi.Stack() for _ in range(num_towers)]
        for i in range(1, num_discs + 1):
            towers[0].push(i)

        hanoi.hanoi_n(towers[0], towers[-1], towers[1: -1], num_discs)
        for i in range(num_towers - 1):
            self.assertListEqual(towers[i]._container, [])
        self.assertListEqual(towers[-1]._container, list(range(1, num_discs + 1)))

    def test_hanoi_n_3_3(self) -> None:
        num_discs: int = 3 
        num_towers: int = 3 # num_towers must be greater than 2
        towers: List[hanoi.Stack[int]] = [hanoi.Stack() for _ in range(num_towers)]
        for i in range(1, num_discs + 1):
            towers[0].push(i)

        hanoi.hanoi_n(towers[0], towers[-1], towers[1: -1], num_discs)
        for i in range(num_towers - 1):
            self.assertListEqual(towers[i]._container, [])
        self.assertListEqual(towers[-1]._container, list(range(1, num_discs + 1)))


if __name__ == '__main__':
    unittest.main()
