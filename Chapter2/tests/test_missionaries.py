# tests_missionaries.py
# unit test of missionaries.py
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

from missionaries import MCState


class TestMCState(unittest.TestCase):
    def test_init(self):
        state = MCState(3, 2, True)
        self.assertEqual(state.wm, 3)
        self.assertEqual(state.wc, 2)
        self.assertEqual(state.em, 0)
        self.assertEqual(state.ec, 1)
        self.assertEqual(state.boat, True)

    def test_goal_test(self):
        state = MCState(3, 2, True)
        self.assertFalse(state.goal_test())

        state = MCState(3, 2, False)
        self.assertFalse(state.goal_test())

    def test_is_legal(self):
        state = MCState(3, 2, True)
        self.assertTrue(state.is_legal)

        state = MCState(2, 3, False)
        self.assertFalse(state.is_legal)

    def test_str(self):
        state = MCState(3, 2, True)
        expected_str = "On the west bank there are 3 missionaries and 2 cannibals.\nOn the east bank there are 0 missionaries and 1 cannibals.\nThe boat is on the west bank."
        self.assertEqual(str(state), expected_str)


if __name__ == '__main__':
    unittest.main()
