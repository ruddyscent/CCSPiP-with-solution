# tests_map_coloring.py
# unit test of map_coloring.py
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

from map_coloring import MapColoringConstraint


class TestMapColoring(unittest.TestCase):
    def test_satisfied(self):
        constraint = MapColoringConstraint("Western Australia", "Northern Territory")
        assignment = {"Western Australia": "red", "Northern Territory": "green"}
        self.assertTrue(constraint.satisfied(assignment))

        assignment = {"Western Australia": "red", "Northern Territory": "red"}
        self.assertFalse(constraint.satisfied(assignment))

        assignment = {"Western Australia": "green"}
        self.assertTrue(constraint.satisfied(assignment))


if __name__ == '__main__':
    unittest.main()
