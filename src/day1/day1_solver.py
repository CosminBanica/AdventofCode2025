"""
Solver for day 1: Secret Entrance
"""
from src.day_management.day_solver import DaySolver


class Day1Solver(DaySolver):
    """
    Solver for day 1: Secret Entrance
    """
    def __init__(self, input_data: str):
        super().__init__(input_data)
        self.rotations = []
        self._read_input()

    def _read_input(self):
        """
        Reads the input data
        """
        for line in self.input_data:
            if line[0] == 'L':
                self.rotations.append(-1 * int(line[1:]))
            else:
                self.rotations.append(int(line[1:]))

    def solve_part_one(self):
        """
        Solves part one
        """
        position = 50
        times_pos_is_zero = 0

        for rotation in self.rotations:
            position += rotation
            position %= 100
            if position == 0:
                times_pos_is_zero += 1

        return times_pos_is_zero

    def solve_part_two(self):
        """
        Solves part two (counts every time the dial points at 0 during any rotation)
        """
        position = 50
        times_pos_passed_zero = 0

        for rotation in self.rotations:
            for _ in range(abs(rotation)):
                if rotation > 0:
                    position += 1
                else:
                    position -= 1
                position %= 100
                if position == 0:
                    times_pos_passed_zero += 1

        return times_pos_passed_zero
