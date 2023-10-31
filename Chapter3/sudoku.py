# sudoku.py
# This module contains functions and classes for generating and solving Sudoku puzzles. It includes functions to generate a Sudoku grid, display the grid, generate a domain for the Sudoku puzzle, and fill the grid with a given assignment. The module also uses the `CSP` and `Constraint` classes from the `csp` module to represent the Sudoku puzzle as a constraint satisfaction problem.
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

from typing import NamedTuple, List, Dict, Optional, Tuple
from csp import CSP, Constraint

Grid = List[List[int]]

def generate_grid(rows: int = 9, columns: int = 9) -> Grid:
    """
    Generates a 2D grid of zeros with the specified number of rows and columns.

    Args:
        rows (int): The number of rows in the grid. Defaults to 9.
        columns (int): The number of columns in the grid. Defaults to 9.

    Returns:
        Grid: A 2D list of integers representing the grid.
    """
    return [[0 for _ in range(columns)] for _ in range(rows)]


def display_grid(grid: Grid) -> None:
    """
    Prints the given Sudoku grid to the console.

    Args:
    - grid (List[List[int]]): a 9x9 Sudoku grid represented as a list of lists of integers

    Returns: None
    """
    for i, row in enumerate(grid):
        for j, col in enumerate(row):
            print(col, end=" ")
            if j == 2 or j == 5:
                print("|", end=" ")
        print()
        if i == 2 or i == 5:
            print("------+-------+------")
        

def generate_domain() -> Dict[Tuple[int, int], List[int]]:
    """
    Generates a domain for a Sudoku puzzle.

    Returns:
    A dictionary with keys as tuples representing the (row, column) of each cell in the puzzle,
    and values as lists of integers representing the possible values that can be assigned to each cell.
    """
    domain: Dict[Tuple[int, int], List[int]] = {}
    for i in range(9):
        for j in range(9):
            domain[(i, j)] = list(range(1, 10))
    return domain


def fill_grid(grid: Grid, assignment: Dict[Tuple[int, int], List[int]]) -> Grid:
    """
    Fills the given Sudoku grid with the values in the given assignment.

    Args:
        grid (List[List[int]]): The Sudoku grid to fill.
        assignment (Dict[Tuple[int, int], List[int]]): The assignment of values to fill the grid with.

    Returns:
        List[List[int]]: The filled Sudoku grid.
    """
    for point, value in assignment.items():
        grid[point[0]][point[1]] = value
    return grid


def duplicate_in_list(l: List[int]) -> bool:
    """
    Check if there are any duplicates in a list of integers.

    Args:
        l: A list of integers.

    Returns:
        True if there are duplicates, False otherwise.
    """
    for i in range(1, 10):
        if l.count(i) > 1:
            return True
    return False


class SodukoRowConstraint(Constraint[Tuple[int, int], int]):
    """
    A constraint for a Sudoku row.

    Args:
    row (int): The row number.

    Attributes:
    row (int): The row number.
    """
    def __init__(self, row: int) -> None:
        pos: List[Tuple[int, int]] = [(row, i) for i in range(9)]
        super().__init__(pos)
        self.row: int = row
        
    def satisfied(self, assignment: Dict[Tuple[int, int], int]) -> bool:
        """
        Check if the constraint is satisfied.

        Args:
        assignment (Dict[Tuple[int, int], int]): The current assignment.

        Returns:
        bool: True if the constraint is satisfied, False otherwise.
        """
        grid = fill_grid(generate_grid(), assignment)
        if duplicate_in_list(grid[self.row]):
            return False
        return True


class SodukoColumnConstraint(Constraint[Tuple[int, int], int]):
    """
    A constraint for a Sudoku puzzle that checks if a column has any duplicate values.

    Attributes:
    -----------
    column : int
        The column number to check for duplicates.
    """

    def __init__(self, column: int) -> None:
        """
        Initializes the constraint with the given column number.

        Parameters:
        -----------
        column : int
            The column number to check for duplicates.
        """
        pos: List[Tuple[int, int]] = [(i, column) for i in range(9)]
        super().__init__(pos)
        self.col: int = column

    def satisfied(self, assignment: Dict[Tuple[int, int], int]) -> bool:
        """
        Checks if the given assignment satisfies the constraint.

        Parameters:
        -----------
        assignment : Dict[Tuple[int, int], int]
            The current assignment of values to positions in the Sudoku grid.

        Returns:
        --------
        bool
            True if the constraint is satisfied, False otherwise.
        """
        grid = fill_grid(generate_grid(), assignment)
        if duplicate_in_list([grid[i][self.col] for i in range(9)]):
            return False
        return True


class SodukoSubgridConstraint(Constraint[Tuple[int, int], int]):
    """
    A constraint for a Sudoku subgrid.

    Args:
    cell (Tuple[int, int]): The top-left cell of the subgrid.

    Attributes:
    loc (Tuple[int, int]): The top-left cell of the subgrid.

    Methods:
    satisfied(assignment: Dict[Tuple[int, int], int]) -> bool:
        Returns True if the subgrid constraint is satisfied, False otherwise.
    """
    def __init__(self, cell: Tuple[int, int]) -> None:
        pos: List[Tuple[int, int]] = [(i, j) for i in range(cell[0], cell[0] + 3) for j in range(cell[1], cell[1] + 3)]
        super().__init__(pos)
        self.loc: Tuple[int, int] = cell

    def satisfied(self, assignment: Dict[Tuple[int, int], int]) -> bool:
        """
        Returns True if the subgrid constraint is satisfied, False otherwise.

        Args:
        assignment (Dict[Tuple[int, int], int]): A dictionary of cell-value assignments.

        Returns:
        bool: True if the subgrid constraint is satisfied, False otherwise.
        """
        grid = fill_grid(generate_grid(), assignment)
        
        row: int
        col: int
        row, col = self.loc
        subgrid = [grid[i][j] for i in range(row, row + 3) for j in range(col, col + 3)]
        if duplicate_in_list(subgrid):
            return False
        return True


if __name__ == "__main__":
    grid: Grid = generate_grid()
    domains = generate_domain()
    variables = list(domains.keys())
    csp: CSP[Tuple[int, int], int] = CSP(variables, domains)

    for i in range(9):
        csp.add_constraint(SodukoRowConstraint(i))
        csp.add_constraint(SodukoColumnConstraint(i))
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            csp.add_constraint(SodukoSubgridConstraint((i, j)))

    solution: Optional[Dict[Tuple[int, int], int]] = csp.backtracking_search()

    if solution is None:
        print("No solution found!")
    else:
        display_grid(fill_grid(grid, solution))

