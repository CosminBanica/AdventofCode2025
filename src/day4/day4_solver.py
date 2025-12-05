"""
Solver for day 4: Printing Department
"""
from src.day_management.day_solver import DaySolver


class Day4Solver(DaySolver):
    """
    Solver for day 4: Printing Department
    """
    def __init__(self, input_data: str):
        super().__init__(input_data)

        # Create a 2D map representing the grid of dots
        # A @ symbol means a paper roll is present at that position
        # A . symbol means no paper roll is present at that position
        self.grid = []
        for line in self.input_data:
            self.grid.append(list(line.strip()))

    def solve_part_one(self, update_grid=False):
        """
        Solves part one
        """
        # Each position has 8 neighbors
        # Check how many paper rolls are neighbored by fewer than 4 other paper rolls
        accessible_rolls = 0
        rows = len(self.grid)
        cols = len(self.grid[0]) if rows > 0 else 0
        
        accessible_positions = []

        for r in range(rows):
            for c in range(cols):
                if self.grid[r][c] == '@':
                    neighbor_count = 0
                    for dr in [-1, 0, 1]:
                        for dc in [-1, 0, 1]:
                            if dr == 0 and dc == 0:
                                continue
                            nr, nc = r + dr, c + dc
                            if 0 <= nr < rows and 0 <= nc < cols:
                                if self.grid[nr][nc] == '@':
                                    neighbor_count += 1
                    if neighbor_count < 4:
                        accessible_rolls += 1
                        accessible_positions.append((r, c))

        if update_grid:
            for pos in accessible_positions:
                self.grid[pos[0]][pos[1]] = '.'

        return accessible_rolls

    def solve_part_two(self):
        """
        Solves part two
        """
        # Now, keep removing accessible paper rolls until no more can be removed
        removable_rolls = 0
        
        while True:
            removed_in_this_round = self.solve_part_one(update_grid=True)
            if removed_in_this_round == 0:
                break
            removable_rolls += removed_in_this_round

        return removable_rolls