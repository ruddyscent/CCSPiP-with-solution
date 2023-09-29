# hanoi.py
# From Classic Computer Science Problems in Python Chapter 1
# Copyright 2018 David Kopec
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

from typing import TypeVar, Generic, List
T = TypeVar('T')


class Stack(Generic[T]):

    def __init__(self) -> None:
        self._container: List[T] = []

    def push(self, item: T) -> None:
        self._container.append(item)

    def pop(self) -> T:
        return self._container.pop()

    def __repr__(self) -> str:
        return repr(self._container)


num_discs: int = 3
tower_a: Stack[int] = Stack()
tower_b: Stack[int] = Stack()
tower_c: Stack[int] = Stack()
for i in range(1, num_discs + 1):
    tower_a.push(i)


def hanoi(begin: Stack[int], end: Stack[int], temp: Stack[int], n: int) -> None:
    if n == 1:
        end.push(begin.pop())
    else:
        hanoi(begin, temp, end, n - 1)
        hanoi(begin, end, temp, 1)
        hanoi(temp, end, begin, n - 1)


def hanoi_n(begin: Stack[int], end: Stack[int], temp: List[Stack[int]], n: int) -> None:
    if n <= len(temp):
        for i in range(n):
            temp[i].push(begin.pop())
        for i in range(n):
            end.push(temp[n - i - 1].pop())
    else:
        chunk: int = n - len(temp) // len(temp)
        nn: int = n
        i: int = 0
        while nn > len(temp):
            nn -= chunk
            if nn > len(temp):
                hanoi(begin, temp[i], end, chunk)
            else:
                hanoi(begin, temp[i], end, nn + chunk - len(temp))
            i += 1
        
        hanoi_n(begin, end, temp, len(temp))
        
        while i > 0:
            i -= 1
            hanoi(temp[i], end, begin, len(temp[i]._container))


if __name__ == "__main__":
    hanoi(tower_a, tower_c, tower_b, num_discs)
    print(tower_a)
    print(tower_b)
    print(tower_c)
