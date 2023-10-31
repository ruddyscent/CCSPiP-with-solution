# circuit_board.py
# From Classic Computer Science Problems in Python Chapter 3
# Copyright 2018 Kyungwon Chun
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

import random

from typing import NamedTuple, List, Dict, Optional
from random import choice
from string import ascii_uppercase
from csp import CSP, Constraint

Grid = List[List[str]]  # type alias for grids


class GridLocation(NamedTuple):
    row: int
    column: int


class Chip(NamedTuple):
    height: int
    width: int


def generate_grid(rows: int, columns: int) -> Grid:
    # initialize grid with blanks
    return [["." for c in range(columns)] for r in range(rows)]


def display_grid(grid: Grid) -> None:
    for row in grid:
        print("".join(row))


def generate_domain(chip: Chip, grid: Grid) -> List[List[GridLocation]]:
    domain: List[List[GridLocation]] = []
    height: int = len(grid)
    width: int = len(grid[0])
    
    for row in range(height):
        for col in range(width):
            columns: range = range(col, col + chip.width)
            rows: range = range(row, row + chip.height)
            location: List[GridLocation]
            if col + chip.width <= width and row + chip.height <= height:
                location = [GridLocation(r, c) for c in columns for r in rows]
                domain.append(location)

    return domain


class ChipSearchConstraint(Constraint[Chip, List[GridLocation]]):
    def __init__(self, chip: Chip) -> None:
        super().__init__(chip)
        self.chip: Chip = chip

    def satisfied(self, assignment: Dict[Chip, List[GridLocation]]) -> bool:
        # if there are any duplicates grid locations then there is an overlap
        all_locations = [locs for values in assignment.values() for locs in values]
        return len(set(all_locations)) == len(all_locations)
    

if __name__ == "__main__":
    grid: Grid = generate_grid(9, 9)
    chips: List[Chip] = [Chip(6, 1), Chip(4, 4), Chip(3, 3), Chip(2, 2), Chip(2, 5)]
    locations: Dict[str, List[List[GridLocation]]] = {}
    for chip in chips:
        locations[chip] = generate_domain(chip, grid)
    csp: CSP[Chip, List[GridLocation]] = CSP(chips, locations)
    csp.add_constraint(ChipSearchConstraint(chips))
    solution: Optional[Dict[Chip, List[GridLocation]]] = csp.backtracking_search()
    
    markers: str = [*reversed(ascii_uppercase)]
    if solution is None:
        print("No solution found!")
    else:
        for chip, grid_locations in solution.items():
            marker: str = markers.pop()
            for grid_location in grid_locations:
                row: int = grid_location.row
                col: int = grid_location.column
                grid[row][col] = marker
        display_grid(grid)
