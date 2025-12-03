"""
Solver for day 3: Lobby
"""
from src.day_management.day_solver import DaySolver



class Day3Solver(DaySolver):
    """
    Solver for day 3: Lobby
    """
    def __init__(self, input_data: str):
        super().__init__(input_data)
        self.banks = [list(map(int, self.input_data[i])) for i in range(len(self.input_data))]
        # print(self.banks)
        # Output: [[9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 1, 1, 1, 1, 1], [8, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 9], [2, 3, 4, 2, 3, 4, 2, 3, 4, 2, 3, 4, 2, 7, 8], [8, 1, 8, 1, 8, 1, 9, 1, 1, 1, 1, 2, 1, 1, 1]]


    def solve_part_one(self):
        """
        Solves part one
        """
        # For each bank, only 2 of the digits can be selected
        # Find the largest number that can be formed by selecting 2 digits from each bank
        # e.g. if you select 9 and 5 from the first bank, you can form 95, but not 59
        # It matters which digit is on the left and which is on the right
        # Return the sum of these largest numbers
        output = 0


        for bank in self.banks:
            largest_number = 0
            for i in range(len(bank)):
                for j in range(i + 1, len(bank)):
                    number = bank[i] * 10 + bank[j]
                    if number > largest_number:
                        largest_number = number
            output += largest_number


        return output


    def solve_part_two(self):
        """
        Solves part two
        """
        # Almost identical to part one, but now we need to select 12 digits from each bank
        # Can't be done with a simple nested loop anymore, as it will be too slow
        output = 0


        for bank in self.banks:
            # Again, we need to maintain the order, so we can't just sort
            largest_number = 0
            n = len(bank)
            # Use dynamic programming to find the largest number that can be formed by selecting 12 digits
            dp = [[0] * (13) for _ in range(n + 1)]


            for i in range(1, n + 1):
                for j in range(1, 13):
                    dp[i][j] = dp[i - 1][j]
                    if j <= i:
                        candidate = dp[i - 1][j - 1] * 10 + bank[i - 1]
                        if candidate > dp[i][j]:
                            dp[i][j] = candidate
            largest_number = dp[n][12]
            output += largest_number


        return output