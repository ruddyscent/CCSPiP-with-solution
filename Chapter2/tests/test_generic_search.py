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
        

    def test_compare_performance(self) -> None:
        n_samples: int = 10
        numbers: list[int] = [x for x in range(1_000_000)]
        keys: int = random.choices(numbers, k=n_samples)

        t: float = time.process_time()
        [generic_search.linear_contains(numbers, key) for key in keys]
        elapsed_time_linear: int = time.process_time() - t
        
        t: float = time.process_time()
        key: int = random.choice(numbers)
        [generic_search.binary_contains(numbers, key) for key in keys]
        elapsed_time_binary: int = time.process_time() - t

        self.assertGreater(elapsed_time_linear / elapsed_time_binary, 0.01 * 1_000_000 / math.log(1_000_000, 2))
        

if __name__ == '__main__':
    unittest.main()
