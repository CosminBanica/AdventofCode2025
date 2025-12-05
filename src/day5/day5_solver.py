"""
Solver for day 5: Cafeteria
"""
from src.day_management.day_solver import DaySolver


class Day5Solver(DaySolver):
    """
    Solver for day 5: Cafeteria
    """
    def __init__(self, input_data: str):
        super().__init__(input_data)
        self.ranges = []
        self.ids = []
        reading_ids = False
        for line in self.input_data:
            if not reading_ids:
                if line:
                    self.ranges.append(tuple(map(int, line.split('-'))))
                else:
                    reading_ids = True
                    continue

            if reading_ids:
                self.ids.append(int(line))

    def solve_part_one(self):
        """
        Solves part one
        """
        # Check how many IDs are in at least one of the ranges
        valid_ids = set()
        for r in self.ranges:
            for id_ in self.ids:
                if r[0] <= id_ <= r[1]:
                    valid_ids.add(id_)
                    continue
        return len(valid_ids)

    def solve_part_two(self):
        """
        Solves part two
        """
        # The IDs are now not relevant for part 2
        # Count how many numbers are in the ranges (some ranges may overlap)
        # We can merge the ranges first, then count the total length.
        merged_ranges = []
        
        for r in sorted(self.ranges):
            if not merged_ranges or merged_ranges[-1][1] < r[0] - 1:
                merged_ranges.append(r)
            else:
                merged_ranges[-1] = (merged_ranges[-1][0], max(merged_ranges[-1][1], r[1]))
        
        total_covered = 0
        for r in merged_ranges:
            total_covered += r[1] - r[0] + 1

        return total_covered
