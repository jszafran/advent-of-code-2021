from dataclasses import dataclass
from typing import Dict, List, Optional, Tuple

from utils import measure_execution_time


@dataclass
class Coords:
    x: int
    y: int


@dataclass(frozen=True)
class DataPoint:
    coords: Coords
    height: int


@dataclass
class HeightMap:
    points: Dict[Tuple[int, int], DataPoint]

    def get_point_for_coords(self, coords: Coords) -> Optional[DataPoint]:
        return self.points.get((coords.x, coords.y))

    def get_adjacent_points_for_coords(
        self, coords: Coords, include_diagonals=False
    ) -> List[DataPoint]:
        points = [
            self.points.get((coords.x + 1, coords.y)),
            self.points.get((coords.x - 1, coords.y)),
            self.points.get((coords.x, coords.y + 1)),
            self.points.get((coords.x, coords.y - 1)),
        ]
        if include_diagonals:
            points += [
                self.points.get((coords.x + 1, coords.y + 1)),
                self.points.get((coords.x + 1, coords.y - 1)),
                self.points.get((coords.x - 1, coords.y + 1)),
                self.points.get((coords.x - 1, coords.y - 1)),
            ]
        return [point for point in points if point is not None]

    def is_lower_point(self, point: DataPoint, include_diagonals=False) -> bool:
        adjacent_points = self.get_adjacent_points_for_coords(
            coords=point.coords, include_diagonals=include_diagonals
        )
        return all(point.height < adj_point.height for adj_point in adjacent_points)

    @classmethod
    def from_text_file(cls, path: str):
        with open(path, "rt") as f:
            data = f.readlines()
        points = {}
        for y, row in enumerate(data):
            for x, height in enumerate(row.replace("\n", "")):
                points[(x, y)] = DataPoint(coords=Coords(x=x, y=y), height=int(height))
        return cls(points)


@measure_execution_time
def get_solutions(path: str) -> None:
    map = HeightMap.from_text_file(path)
    part_1_answer = sum(
        point.height + 1 for point in map.points.values() if map.is_lower_point(point)
    )
    print(f"Part 1 answer: {part_1_answer}")


if __name__ == "__main__":
    input_path = "input.txt"
    get_solutions(input_path)
