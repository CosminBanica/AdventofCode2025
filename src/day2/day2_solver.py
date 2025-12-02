"""
Solver for day 2: Gift Shop
"""
from src.day_management.day_solver import DaySolver


class Day2Solver(DaySolver):
    """
    Solver for day 2: Gift Shop
    """
    def __init__(self, input_data: str):
        super().__init__(input_data)
        
        # It's only 1 line, split by ,
        self.ranges = [(int(r.split('-')[0]), int(r.split('-')[1])) for r in self.input_data[0].split(',')]

        # Order by second value ascending
        self.ranges.sort(key=lambda x: x[1])

        self.max_value = self.ranges[-1][1]

    def solve_part_one(self):
        """
        Solves part one
        """
        # We need to check for every number, whether the number made up by repeating
        # this number's digits is in any of the ranges
        # Stop when the number you get by repeating the digits exceeds max_value
        proceed = True
        i = 1
        sum_found = 0
        while proceed:
            str_i = str(i)
            repeated_num = int(str_i + str_i)
            if repeated_num > self.max_value:
                proceed = False
                continue

            for r in self.ranges:
                if r[0] <= repeated_num <= r[1]:
                    sum_found += repeated_num
                    break

            i += 1

        return sum_found

    def solve_part_two(self):
        """
        Solves part two
        """
        # For part two it's almost the same, except the number can repeat any number
        # of times, so we check for each until the repeated number exceeds max_value
        proceed = True
        i = 1
        sum_found = 0
        numbers_in_ranges = {}
        while proceed:
            str_i = str(i)
            repeat_count = 2
            while True:
                repeated_num = int(str_i * repeat_count)
                if repeated_num > self.max_value:
                    break

                for r in self.ranges:
                    if r[0] <= repeated_num <= r[1]:
                        if repeated_num in numbers_in_ranges.get(r, []):
                            continue
                        sum_found += repeated_num
                        if r in numbers_in_ranges:
                            numbers_in_ranges[r].append(repeated_num)
                        else:
                            numbers_in_ranges[r] = [repeated_num]
                        break

                repeat_count += 1

            if int(str_i * 2) > self.max_value:
                proceed = False

            i += 1

        return sum_found