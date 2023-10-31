# tests_circuit_board.py
# unit test of circuit_board.py
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
from circuit_board import generate_domain, generate_grid, Chip, ChipSearchConstraint, GridLocation


class TestCircuitBoard(unittest.TestCase):
    def test_generate_domain(self):
        chip = Chip(1, 1)
        grid = generate_grid(2, 2)
        domain = generate_domain(chip, grid)
        expected_domain = [[GridLocation(0, 0)],
                           [GridLocation(0, 1)],
                           [GridLocation(1, 0)],
                           [GridLocation(1, 1)]]
        self.assertCountEqual(domain, expected_domain)

    def test_chip_search_constraint(self):
        chip1 = Chip(1, 1)
        chip2 = Chip(2, 1)
        constraint = ChipSearchConstraint(chip1)
        assignment = {chip1: [GridLocation(0, 0)],
                      chip2: [GridLocation(0, 0), GridLocation(1, 0)]}
        self.assertFalse(constraint.satisfied(assignment))

        assignment = {chip1: [GridLocation(0, 0)],
                      chip2: [GridLocation(0, 1), GridLocation(1, 1)]}
        self.assertTrue(constraint.satisfied(assignment))


if __name__ == '__main__':
    unittest.main()
