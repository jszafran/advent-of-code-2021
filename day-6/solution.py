from collections import defaultdict
from typing import List


class LanternfishGrowthTracker:
    def __init__(self, initial_ages: List[int]) -> None:
        self.data = defaultdict(int)
        for age in initial_ages:
            self.data[age] += 1

    def process_day(self) -> None:
        about_to_reproduce = sum([v for k, v in self.data.items() if k == 0])
        self.data = defaultdict(
            int, {(k - 1): v for k, v in self.data.items() if k != 0}
        )
        if about_to_reproduce:
            self.data[8] += about_to_reproduce
            self.data[6] += about_to_reproduce

    @property
    def total_number(self) -> int:
        return sum(self.data.values())


def get_input(path: str) -> List[int]:
    with open(path, "rt") as f:
        ages = list(map(lambda age: int(age), f.readline().split(",")))
    return ages


def solution_part_one(ages: List[int], days_amount: int) -> int:
    tracker = LanternfishGrowthTracker(ages)

    for _ in range(1, days_amount + 1):
        tracker.process_day()

    return tracker.total_number


if __name__ == "__main__":
    path = "input.txt"
    ages_from_file = get_input(path)
    print(solution_part_one(ages_from_file, 80))
    print(solution_part_one(ages_from_file, 256))
