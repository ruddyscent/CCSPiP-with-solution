# tests_fib7.py
# From Classic Computer Science Problems in Python Chapter 1
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

import time
import unittest

from typing import Dict, List

import fib1
import fib2
import fib3
import fib4
import fib5
import fib6
import fib7


FIB_TABLE: Dict[int, int] = {
    0: 0, 
    1: 1, 
    5: 5, 
    10: 55, 
    30: 832_040,
    # 50: 12_586_269_025
    }

# Note that fib1 is purposefully wrong.
# class Fib1TestCase(unittest.TestCase):
#     def test_fib1_1(self):
#         ...

class Fib2TestCase(unittest.TestCase):
    def test_value(self) -> None:
        for n, fib_n in FIB_TABLE.items():
            result: int = fib2.fib2(n)
            assert result == fib_n


class Fib3TestCase(unittest.TestCase):
    def test_value(self) -> None:
        for n, fib_n in FIB_TABLE.items():
            result: int = fib3.fib3(n)
            assert result == fib_n

    def test_elapsed_time(self) -> None:
        t: float = time.process_time()
        result: List[int] = [fib2.fib2(n) for n in FIB_TABLE.keys()]
        elapsed_time_fib2: float = time.process_time() - t

        t: float = time.process_time()
        result: List[int] = [fib3.fib3(n) for n in FIB_TABLE.keys()]
        elapsed_time_fib3: float = time.process_time() - t

        assert elapsed_time_fib3 < elapsed_time_fib2


class Fib4TestCase(unittest.TestCase):
    def test_value(self) -> None:
        for n, fib_n in FIB_TABLE.items():
            result: int = fib4.fib4(n)
            assert result == fib_n

    def test_elapsed_time(self) -> None:
        t: float = time.process_time()
        result: List[int] = [fib2.fib2(n) for n in FIB_TABLE.keys()]
        elapsed_time_fib2: float = time.process_time() - t

        t: float = time.process_time()
        result: List[int] = [fib4.fib4(n) for n in FIB_TABLE.keys()]
        elapsed_time_fib4: float = time.process_time() - t

        assert elapsed_time_fib4 < elapsed_time_fib2


class Fib5TestCase(unittest.TestCase):
    def test_value(self) -> None:
        for n, fib_n in FIB_TABLE.items():
            result: int = fib5.fib5(n)
            assert result == fib_n

    def test_elapsed_time(self) -> None:
        t: float = time.process_time()
        result: List[int] = [fib2.fib2(n) for n in FIB_TABLE.keys()]
        elapsed_time_fib2: float = time.process_time() - t

        t: float = time.process_time()
        result: List[int] = [fib4.fib4(n) for n in FIB_TABLE.keys()]
        elapsed_time_fib5: float = time.process_time() - t

        assert elapsed_time_fib5 < elapsed_time_fib2


class Fib6TestCase(unittest.TestCase):
    def test_value(self) -> None:
        reuslt: List[int] = [n for n in fib6.fib6(max(FIB_TABLE.keys()))]
        for n, fib_n in FIB_TABLE.items():
            assert reuslt[n] == fib_n

    def test_elapsed_time(self) -> None:
        t: float = time.process_time()
        result: List[int] = [fib2.fib2(n) for n in FIB_TABLE.keys()]
        elapsed_time_fib2: float = time.process_time() - t

        t: float = time.process_time()
        result: List[int] = [n for n in fib6.fib6(max(FIB_TABLE.keys()))]
        elapsed_time_fib6: float = time.process_time() - t

        assert elapsed_time_fib6 < elapsed_time_fib2


class Fib7TestCase(unittest.TestCase):
    def test_value(self) -> None:
        for n, fib_n in FIB_TABLE.items():
            result: int = fib7.fib7(n)
            assert result == fib_n

    def test_elapsed_time(self) -> None:
        t: float = time.process_time()
        result: List[int] = [fib2.fib2(n) for n in FIB_TABLE.keys()]
        elapsed_time_fib2: float = time.process_time() - t

        t: float = time.process_time()
        result: List[int] = [fib7.fib7(n) for n in FIB_TABLE.keys()]
        elapsed_time_fib7: float = time.process_time() - t

        assert elapsed_time_fib7 < elapsed_time_fib2


if __name__ == '__main__':
    unittest.main()
