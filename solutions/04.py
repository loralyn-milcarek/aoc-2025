import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
from tools.readers import read_grid
from copy import deepcopy

class Roll:
    """
    Wrapping paper roll with awareness of surrounding positions.
    """

    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.neighbors = []

    def set_adjacent_positions(self, grid):
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        self.neighbors = []
        for dr, dc in directions:
            nr, nc = self.row + dr, self.col + dc
            if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
                self.neighbors.append(grid[nr][nc])
            else:
                self.neighbors.append(".")
    
    def count_occupied_positions(self):
        return self.neighbors.count("@")
              

def parse_input(day):
    """Parse the input file for this day."""
    lines = read_grid(day)
    return lines

def count_accessible_rolls(grid, remove=False):
    """
    Counts accessible rolls of wrapping paper stored in a grid. 
    Rolls are accessible if fewer than four of the adjacent 8 positions are occupied.
    
    Arguments: 
        grid: a 2-dimensional list of "." representing an empty space and "@" representing a wrapping paper roll.
        remove: if True, removes accessible rolls from the grid and repeats until no more rolls are accessible.

    Returns: Count of accessible rolls.
    """
    accessible_count = 0
    if remove:
        while True:
            positions_to_remove = find_accessible_rolls(grid)
            accessible_count += len(positions_to_remove)

            for p in positions_to_remove:
                grid[p[0]][p[1]] = "."

            if not positions_to_remove:
                break
    else:
        accessible_count = len(find_accessible_rolls(grid))

    return accessible_count

def find_accessible_rolls(grid):
    """
    Finds accessible rolls of wrapping paper stored in a grid. 
    Rolls are accessible if fewer than four of the adjacent 8 positions are occupied.
    
    Arguments: 
        grid: a 2-dimensional list of "." representing an empty space and "@" representing a wrapping paper roll.

    Returns: Positions of accessible rolls as list of (row, col).
    """
    accessible_positions = []
    for r, row in enumerate(grid):
        for c, pos in enumerate(row):
            if pos != "@":
                continue

            roll = Roll(r, c)
            roll.set_adjacent_positions(grid)
            should_remove = roll.count_occupied_positions() < 4

            if should_remove:
                accessible_positions.append((r, c))
    return accessible_positions

if __name__ == "__main__":
    day = 4
    data = parse_input(day)
    
    print(f"Day {day}")
    print(f"Part 1: {count_accessible_rolls(deepcopy(data))}")
    print(f"Part 2: {count_accessible_rolls(deepcopy(data), True)}")
