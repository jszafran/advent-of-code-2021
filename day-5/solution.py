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
    def is_diagonal(self) -> bool:
        return abs(self.start.x - self.end.x) == abs(self.start.y - self.end.y)

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
        elif self.is_diagonal:
            # TODO: Can it be somehow simplified?
            x_step = 1 if self.start.x < self.end.x else -1
            y_step = 1 if self.start.y < self.end.y else -1
            x_coords = (x for x in range(self.start.x, self.end.x + x_step, x_step))
            y_coords = (y for y in range(self.start.y, self.end.y + y_step, y_step))
            return [
                Point(x=coords[0], y=coords[1]) for coords in zip(x_coords, y_coords)
            ]


def get_solution(lines: List[Line], condition) -> int:
    filtered_lines = list(filter(condition, lines))
    points = [point for line in filtered_lines for point in line.all_points]
    return sum(1 for v in Counter(points).values() if v >= 2)


def get_data_from_text_file(path: str) -> List[Line]:
    with open(path, "rt") as f:
        data = f.readlines()

    return list(map(lambda line: Line.from_string(line), data))


if __name__ == "__main__":
    part_1_condition = lambda line: line.is_vertical or line.is_horizontal  # noqa
    part_2_condition = (
        lambda line: line.is_vertical or line.is_horizontal or line.is_diagonal
    )  # noqa
    lines_from_file = get_data_from_text_file("input.txt")
    print(get_solution(lines_from_file, part_1_condition))
    print(get_solution(lines_from_file, part_2_condition))
