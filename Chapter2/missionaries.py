# missionaries.py
# From Classic Computer Science Problems in Python Chapter 2
# Copyright 2018 David Kopec
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

from __future__ import annotations
from typing import List, Optional
from generic_search import bfs, Node, node_to_path

TOTAL_MISSIONARY: int = 3
TOTAL_CANNIBAL: int = 3


class MCState:
    def __init__(self, missionaries: int, cannibals: int, boat: bool, total_missionary: int = 3, total_canimal: int = 3) -> None:
        self.wm: int = missionaries  # west bank missionaries
        self.wc: int = cannibals  # west bank cannibals
        self.total_m: int = total_missionary
        self.total_c: int = total_canimal
        self.em: int = self.total_m - self.wm  # east bank missionaries
        self.ec: int = self.total_c - self.wc  # east bank cannibals
        self.boat: bool = boat

    def __str__(self) -> str:
        return ("On the west bank there are {} missionaries and {} cannibals.\n"
                "On the east bank there are {} missionaries and {} cannibals.\n"
                "The boat is on the {} bank.")\
            .format(self.wm, self.wc, self.em, self.ec, ("west" if self.boat else "east"))

    def goal_test(self) -> bool:
        return self.is_legal and self.em == self.total_m and self.ec == self.total_c

    @property
    def is_legal(self) -> bool:
        if self.wm < self.wc and self.wm > 0:
            return False
        if self.em < self.ec and self.em > 0:
            return False
        return True

    def successors(self) -> List[MCState]:
        sucs: List[MCState] = []
        if self.boat:  # boat on west bank
            if self.wm > 1:
                sucs.append(MCState(self.wm - 2, self.wc,
                            not self.boat, self.total_m, self.total_c))
            if self.wm > 0:
                sucs.append(MCState(self.wm - 1, self.wc,
                            not self.boat, self.total_m, self.total_c))
            if self.wc > 1:
                sucs.append(MCState(self.wm, self.wc - 2,
                            not self.boat, self.total_m, self.total_c))
            if self.wc > 0:
                sucs.append(MCState(self.wm, self.wc - 1,
                            not self.boat, self.total_m, self.total_c))
            if (self.wc > 0) and (self.wm > 0):
                sucs.append(MCState(self.wm - 1, self.wc - 1,
                            not self.boat, self.total_m, self.total_c))
        else:  # boat on east bank
            if self.em > 1:
                sucs.append(MCState(self.wm + 2, self.wc,
                            not self.boat, self.total_m, self.total_c))
            if self.em > 0:
                sucs.append(MCState(self.wm + 1, self.wc,
                            not self.boat, self.total_m, self.total_c))
            if self.ec > 1:
                sucs.append(MCState(self.wm, self.wc + 2,
                            not self.boat, self.total_m, self.total_c))
            if self.ec > 0:
                sucs.append(MCState(self.wm, self.wc + 1,
                            not self.boat, self.total_m, self.total_c))
            if (self.ec > 0) and (self.em > 0):
                sucs.append(MCState(self.wm + 1, self.wc + 1,
                            not self.boat, self.total_m, self.total_c))
        return [x for x in sucs if x.is_legal]


def display_solution(path: List[MCState]):
    if len(path) == 0:  # sanity check
        return
    old_state: MCState = path[0]
    print(old_state)
    for current_state in path[1:]:
        if current_state.boat:
            print("{} missionaries and {} cannibals moved from the east bank to the west bank.\n"
                  .format(old_state.em - current_state.em, old_state.ec - current_state.ec))
        else:
            print("{} missionaries and {} cannibals moved from the west bank to the east bank.\n"
                  .format(old_state.wm - current_state.wm, old_state.wc - current_state.wc))
        print(current_state)
        old_state = current_state


if __name__ == "__main__":
    TOTAL_MISSIONARY = 4
    TOTAL_CANNIBAL = 3
    start: MCState = MCState(
        TOTAL_MISSIONARY, TOTAL_CANNIBAL, True, TOTAL_MISSIONARY, TOTAL_CANNIBAL)
    solution: Optional[Node[MCState]] = bfs(
        start, MCState.goal_test, MCState.successors)[0]
    if solution is None:
        print("No solution found!")
    else:
        path: List[MCState] = node_to_path(solution)
        display_solution(path)
