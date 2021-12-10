import sys
from dataclasses import dataclass
from functools import reduce
from typing import Dict, List, Optional, Tuple

from utils import measure_execution_time


@dataclass(frozen=True)
class Coords:
    x: int
    y: int


@dataclass(frozen=True)
class DataPoint:
    coords: Coords
    height: int


@dataclass
class Basin:
    points: List[DataPoint]

    @property
    def size(self) -> int:
        return len(self.points)


@dataclass
class HeightMap:
    points: Dict[Tuple[int, int], DataPoint]

    def get_point_for_coords(self, coords: Coords) -> Optional[DataPoint]:
        return self.points.get((coords.x, coords.y))

    def get_adjacent_points_for_coords(
        self,
        coords: Coords,
    ) -> List[DataPoint]:
        points = [
            self.points.get((coords.x + 1, coords.y)),
            self.points.get((coords.x - 1, coords.y)),
            self.points.get((coords.x, coords.y + 1)),
            self.points.get((coords.x, coords.y - 1)),
        ]
        return [point for point in points if point is not None]

    def is_lower_point(self, point: DataPoint) -> bool:
        adjacent_points = self.get_adjacent_points_for_coords(coords=point.coords)
        return all(point.height < adj_point.height for adj_point in adjacent_points)

    def get_low_points(self) -> List[DataPoint]:
        return [point for point in self.points.values() if self.is_lower_point(point)]

    def calculate_basin(self, low_point: DataPoint) -> Basin:
        def fetch_higher_points(points, higher_points):
            if not points:
                return higher_points
            curr_point = points.pop()
            curr_higher_points = [
                point
                for point in self.get_adjacent_points_for_coords(curr_point.coords)
                if point.height != 9 and point.height > curr_point.height
            ]
            for point in curr_higher_points:
                if point not in points:
                    points.append(point)
            higher_points |= set(curr_higher_points)
            return fetch_higher_points(points, higher_points)

        points = [low_point] + self.get_adjacent_points_for_coords(low_point.coords)
        result = list(fetch_higher_points(points, set())) + [low_point]
        return Basin(list(result))

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

    low_points = map.get_low_points()
    basins_sizes = [map.calculate_basin(low_point).size for low_point in low_points]
    part_2_answer = reduce(lambda x, y: x * y, sorted(basins_sizes, reverse=True)[:3])
    print(f"Part 2 answer: {part_2_answer}")


if __name__ == "__main__":
    # kind of cheating ;-P
    sys.setrecursionlimit(3000)
    input_path = "input.txt"
    get_solutions(input_path)
