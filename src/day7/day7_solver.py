"""
Solver for day 7: Laboratories
"""
from src.day_management.day_solver import DaySolver


class Day7Solver(DaySolver):
    """
    Solver for day 7: Laboratories
    """
    def __init__(self, input_data: str):
        super().__init__(input_data)

        # Find starting position in the first line
        for index, char in enumerate(self.input_data[0]):
            if char == 'S':
                self.starting_position = (0, index)

        # Also find all the positions of '^' in the grid, per row
        self.caret_positions = {}
        for row_index, line in enumerate(self.input_data):
            self.caret_positions[row_index] = {}
            for col_index, char in enumerate(line):
                if char == '^':
                    self.caret_positions[row_index][col_index] = True
        

    def solve_part_one(self):
        """
        Solves part one
        """
        # From starting position, the beam goes down
        # Every time you encounter a '^', the beam gets split in 2, 
        # to the direct left and right, and both beams keep going down
        # Count how many times beam is split by a '^' until it reaches the bottom
        self.beams = [(self.starting_position[0], self.starting_position[1])]
        splits = 0
        curr_row = 0

        # There's always one row of just dots, followed by a row of dots and some '^'
        # Row 0 has just dots and the 'S', and row 1 has just dots
        while curr_row < len(self.input_data) - 1:
            curr_row += 1
            new_beams = []
            for beam in self.beams:
                beam_col = beam[1]
                if beam_col in self.caret_positions.get(curr_row, {}):
                    # Beam hits a '^', split it
                    splits += 1
                    if beam_col > 0:
                        if (curr_row, beam_col - 1) not in new_beams:
                            new_beams.append((curr_row, beam_col - 1))
                    if beam_col < len(self.input_data[0]) - 1:
                        if (curr_row, beam_col + 1) not in new_beams:
                            new_beams.append((curr_row, beam_col + 1))
                else:
                    # Beam continues down
                    if (curr_row, beam_col) not in new_beams:
                        new_beams.append((curr_row, beam_col))
            self.beams = new_beams

        return splits

    def solve_part_two(self):
        """
        Solves part two
        """
        # Part 2 is similar, but instead of counting splits, we need to count
        # all routes that beams can take to reach the bottom
        # So if the beam reaches the same end position at the bottom, but from
        # different paths, we count those separately
        self.beams = {(self.starting_position[0], self.starting_position[1]): 1}  # (row, col): path_count
        timelines = 0
        curr_row = 0

        # When 2 beams reach the same position, we need to count them separately
        # so just increment the path_count accordingly
        while curr_row < len(self.input_data) - 1:
            curr_row += 1
            new_beams = {}
            for beam, path_count in self.beams.items():
                beam_col = beam[1]
                if beam_col in self.caret_positions.get(curr_row, {}):
                    # Beam hits a '^', split it
                    if beam_col > 0:
                        new_pos = (curr_row, beam_col - 1)
                        if new_pos in new_beams:
                            new_beams[new_pos] += path_count
                        else:
                            new_beams[new_pos] = path_count
                    if beam_col < len(self.input_data[0]) - 1:
                        new_pos = (curr_row, beam_col + 1)
                        if new_pos in new_beams:
                            new_beams[new_pos] += path_count
                        else:
                            new_beams[new_pos] = path_count
                else:
                    # Beam continues down
                    new_pos = (curr_row, beam_col)
                    if new_pos in new_beams:
                        new_beams[new_pos] += path_count
                    else:
                        new_beams[new_pos] = path_count
            self.beams = new_beams
           
        timelines = sum(self.beams.values())
        return timelines
