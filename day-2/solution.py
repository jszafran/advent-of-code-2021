from dataclasses import dataclass
from typing import List, Tuple


def parse_line(line: str) -> Tuple[str, int]:
    direction, val = line.split(" ")
    return direction, int(val)


def solution(lines: List[str]) -> int:
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

    def handle_down_command(self, value: int) -> None:
        self.aim += value

    def handle_up_command(self, value: int) -> None:
        self.aim -= value

    def handle_forward_command(self, value: int) -> None:
        self.horizontal_position += value
        self.depth += self.aim * value

    def handle_string_command(self, s: str) -> None:
        command, val = parse_line(s)
        command_mapping = {
            "down": self.handle_down_command,
            "up": self.handle_up_command,
            "forward": self.handle_forward_command,
        }
        command_mapping[command](val)

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
    print(solution(data))
    print(solution_part_2(data))
