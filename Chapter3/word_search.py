# word_search.py
# From Classic Computer Science Problems in Python Chapter 3
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

from typing import NamedTuple, List, Dict, Optional
from random import choice
from string import ascii_uppercase
from csp import CSP, Constraint

Grid = List[List[str]]  # type alias for grids


class GridLocation(NamedTuple):
    row: int
    column: int


def generate_grid(rows: int, columns: int) -> Grid:
    # initialize grid with random letters
    return [[choice(ascii_uppercase) for c in range(columns)] for r in range(rows)]


def display_grid(grid: Grid) -> None:
    for row in grid:
        print("".join(row))


def generate_domain(word: str, grid: Grid) -> List[List[GridLocation]]:
    domain: List[List[GridLocation]] = []
    height: int = len(grid)
    width: int = len(grid[0])
    length: int = len(word)
    for row in range(height):
        for col in range(width):
            columns: range = range(col, col + length)
            rows: range = range(row, row + length)
            location = List[GridLocation]
            if col + length <= width:
                # left to right
                location = [GridLocation(row, c) for c in columns]
                domain.extend([location, list(reversed(location))])
                # diagonal towards bottom right
                if row + length <= height:
                    location = [GridLocation(r, col + (r - row)) for r in rows]
                    domain.extend([location, list(reversed(location))])
            if row + length <= height:
                # top to bottom
                location = [GridLocation(r, col) for r in rows]
                domain.extend([location, list(reversed(location))])
                # diagonal towards bottom left
                if col + 1 - length >= 0:
                    location = [GridLocation(r, col - (r - row)) for r in rows]
                    domain.extend([location, list(reversed(location))])
    return domain


class WordSearchConstraint(Constraint[str, List[GridLocation]]):
    def __init__(self, words: List[str]) -> None:
        super().__init__(words)
        self.words: List[str] = words

    def satisfied(self, assignment: Dict[str, List[GridLocation]]) -> bool:
        # The overlapping letters should be the smae letters among multiple words
        assigned_locations: Dict[GridLocation, str] = {}
        for word, location in assignment.items():
            for letter, grid_location in zip(word, location):
                if grid_location not in assigned_locations:
                    assigned_locations[grid_location] = letter
                elif assigned_locations[grid_location] != letter:
                    return False
        return True
    

if __name__ == "__main__":
    grid: Grid = generate_grid(9, 9)
    words: List[str] = ["MATTHEW", "JOE", "MARY", "SARAH", "SALLY"]
    locations: Dict[str, List[List[GridLocation]]] = {}
    for word in words:
        locations[word] = generate_domain(word, grid)
    csp: CSP[str, List[GridLocation]] = CSP(words, locations)
    csp.add_constraint(WordSearchConstraint(words))
    solution: Optional[Dict[str, List[GridLocation]]] = csp.backtracking_search()
    if solution is None:
        print("No solution found!")
    else:
        for word, grid_locations in solution.items():
            for index, letter in enumerate(word):
                (row, col) = (grid_locations[index].row, grid_locations[index].column)
                grid[row][col] = letter
        display_grid(grid)
