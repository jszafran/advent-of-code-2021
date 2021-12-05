from dataclasses import dataclass
from typing import List, Tuple


def parse_line(line: str) -> Tuple[str, int]:
    direction, val = line.split(" ")
    return direction, int(val)


def solution_part_1(lines: List[str]) -> int:
    directions_sums = {
        "up": 0,
        "down": 0,
        "forward": 0,
    }

    for line in lines:
        direction, val = parse_line(line)
        directions_sums[direction] += val

    depth = directions_sums["down"] - directions_sums["up"]
    horizontal_position = directions_sums["forward"]

    return depth * horizontal_position


@dataclass
class Submarine:
    aim: int = 0
    depth: int = 0
    horizontal_position: int = 0

    def down(self, value: int) -> None:
        self.aim += value

    def up(self, value: int) -> None:
        self.aim -= value

    def forward(self, value: int) -> None:
        self.horizontal_position += value
        self.depth += self.aim * value

    def handle_string_command(self, s: str) -> None:
        command, val = parse_line(s)
        getattr(self, command)(val)

    @property
    def final_position(self) -> int:
        return self.depth * self.horizontal_position


def solution_part_2(lines: List[str]) -> int:
    submarine = Submarine()
    for line in lines:
        submarine.handle_string_command(line)
    return submarine.final_position


if __name__ == "__main__":
    with open("aoc-day-2-input.txt", "rt") as f:
        data = f.readlines()
    print(solution_part_1(data))
    print(solution_part_2(data))
