# tests_queens.py
# unit test of queens.py
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

from queens import QueensConstraint


class TestQueensConstraint(unittest.TestCase):
    def test_satisfied(self):
        constraint = QueensConstraint([1, 2, 3, 4, 5, 6, 7, 8])
        assignment = {1: 1, 2: 5, 3: 8, 4: 6, 5: 3, 6: 7, 7: 2, 8: 4}
        self.assertTrue(constraint.satisfied(assignment))

        assignment = {1: 1, 2: 5, 3: 8, 4: 6, 5: 3, 6: 7, 7: 2, 8: 5}
        self.assertFalse(constraint.satisfied(assignment))

        assignment = {1: 1, 2: 5, 3: 8, 4: 6, 5: 3, 6: 7, 7: 2}
        self.assertTrue(constraint.satisfied(assignment))


if __name__ == '__main__':
    unittest.main()
