from typing import List, Tuple


def solution(lines: List[str]) -> int:
    def parse_line(line: str) -> Tuple[str, int]:
        direction, val = line.split(" ")
        return direction, int(val)

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


if __name__ == "__main__":
    with open("aoc-day-2-input.txt", "rt") as f:
        data = f.readlines()
    print(solution(data))
