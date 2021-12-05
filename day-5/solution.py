from collections import Counter
from dataclasses import dataclass
from typing import List


@dataclass(frozen=True)
class Point:
    x: int
    y: int

    @classmethod
    def from_string(cls, s: str):
        x_str, y_str = s.split(",")
        return cls(x=int(x_str), y=int(y_str))


@dataclass(frozen=True)
class Line:
    start: Point
    end: Point

    @classmethod
    def from_string(cls, s: str):
        start, end = s.split(" -> ")
        return cls(start=Point.from_string(start), end=Point.from_string(end))

    @property
    def is_horizontal(self) -> bool:
        return self.start.y == self.end.y

    @property
    def is_vertical(self) -> bool:
        return self.start.x == self.end.x

    @property
    def all_points(self) -> List[Point]:
        if self.is_vertical:
            step = 1 if self.start.y < self.end.y else -1
            return [
                Point(x=self.start.x, y=i)
                for i in range(self.start.y, self.end.y + step, step)
            ]
        elif self.is_horizontal:
            step = 1 if self.start.x < self.end.x else -1
            return [
                Point(x=i, y=self.start.y)
                for i in range(self.start.x, self.end.x + step, step)
            ]


def part_1_solution(lines: List[Line]) -> int:
    filtered_lines = [line for line in lines if line.is_vertical or line.is_horizontal]
    points = [point for line in filtered_lines for point in line.all_points]
    return sum(1 for v in Counter(points).values() if v >= 2)


def get_data_from_text_file(path: str) -> List[Line]:
    with open(path, "rt") as f:
        data = f.readlines()

    return list(map(lambda line: Line.from_string(line), data))


if __name__ == "__main__":
    lines_from_file = get_data_from_text_file("input.txt")
    print(part_1_solution(lines_from_file))
