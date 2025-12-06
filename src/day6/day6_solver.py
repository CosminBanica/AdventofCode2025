"""
Solver for day 6: Trash Compactor
"""
from src.day_management.day_solver import DaySolver


class Day6Solver(DaySolver):
    """
    Solver for day 6: Trash Compactor
    """
    def __init__(self, input_data: str):
        super().__init__(input_data)

        # Each problem's numbers are arranged vertically; at the bottom of the problem 
        # is the symbol for the operation that needs to be performed. Problems are 
        # separated by a full column of only spaces. The left/right alignment of numbers 
        # within each problem can be ignored.
        self.columns = []
        self.symbols = []
        for i, line in enumerate(self.input_data):
            if i == 0:
                for _ in range(len(line)):
                    self.columns.append([])

            if i == len(self.input_data) - 1:
                # Last line contains operation symbols
                symbols = line.split(" ")
                symbols = [sym for sym in symbols if sym != ""]
                self.symbols = symbols
                break
            
            # Split line into numbers; spaces are ignored
            numbers = line.split(" ")
            numbers = [num for num in numbers if num != ""]
            for j, number in enumerate(numbers):
                if number != "":
                    self.columns[j].append(int(number))

        # Remove empty columns (separators between problems)
        self.columns = [col for col in self.columns if len(col) > 0]

        # For part 2, operations are still split into columns
        # Now however, the numbers in each column are not per row,
        # but rather they are to be read vertically down the column, if they are
        # on the same column.
        self.part_two_columns = [[] for _ in range(len(self.symbols))]

        with open("src/day6/input.txt", "r") as f:
            self.input_data = f.read().splitlines()
        
        curr_col = 0
        # Easier to read column-wise
        for j in range(len(self.input_data[0])):
            col = []
            for i in range(len(self.input_data) - 1):
                if j >= len(self.input_data[i]):
                    continue

                char = self.input_data[i][j]
                if char != " ":
                    col.append(char)

            if len(col) > 0:
                col = int("".join(col))
                self.part_two_columns[curr_col].append(col)
            else:
                curr_col += 1
            

    def solve_part_one(self):
        """
        Solves part one
        """
        # Each problem consists of a column of numbers and an operation symbol at 
        # the bottom. Perform the indicated operation on the numbers in each column
        # and sum the results. Symbol is either + or *
        result = 0

        for col, sym in zip(self.columns, self.symbols):
            if sym == "+":
                result += sum(col)
            elif sym == "*":
                prod = 1
                for num in col:
                    prod *= num
                result += prod
            else:
                raise ValueError(f"Unknown symbol: {sym}")

        return result

    def solve_part_two(self):
        """
        Solves part two
        """
        # Same but for part_two_columns
        result = 0

        for col, sym in zip(self.part_two_columns, self.symbols):
            if sym == "+":
                result += sum(col)
            elif sym == "*":
                prod = 1
                for num in col:
                    prod *= num
                result += prod
            else:
                raise ValueError(f"Unknown symbol: {sym}")

        return result