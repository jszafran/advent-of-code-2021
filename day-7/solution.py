from dataclasses import dataclass
from typing import Callable, List

from utils import measure_execution_time


@dataclass(frozen=True)
class Crab:
    position: int

    def get_fuel_consumption_for_position_change(
        self,
        other_position: int,
        fuel_consumption_algorithm: Callable[[int, int], int],
    ) -> int:
        return fuel_consumption_algorithm(self.position, other_position)


def get_data(path: str) -> List[Crab]:
    with open(path, "rt") as f:
        data = [Crab(position=int(x)) for x in f.readline().split(",")]
    return data


def single_unit_per_move_algorithm(cur_pos: int, other_pos: int) -> int:
    return abs(cur_pos - other_pos)


def increase_previous_rate_by_one_algorithm(cur_pos: int, other_pos: int) -> int:
    return sum(range(abs(cur_pos - other_pos) + 1))


@measure_execution_time
def solution(
    crabs: List[Crab], fuel_consumption_algorithm: Callable[[int, int], int]
) -> int:
    fuel_consumptions = []
    max_pos = max([c.position for c in crabs])

    for pos in range(0, max_pos):
        fuel_consumption = sum(
            [
                c.get_fuel_consumption_for_position_change(
                    pos, fuel_consumption_algorithm
                )
                for c in crabs
            ]
        )
        fuel_consumptions.append(fuel_consumption)
    return min(fuel_consumptions)


if __name__ == "__main__":
    crabs_from_file = get_data("input.txt")
    print(solution(crabs_from_file, single_unit_per_move_algorithm))
    print(solution(crabs_from_file, increase_previous_rate_by_one_algorithm))
