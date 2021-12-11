from dataclasses import dataclass
from typing import Dict, List, Optional

BOARD_LENGTH = 9


class InvalidCoordinatesError(Exception):
    pass


@dataclass(frozen=True)
class XYCoords:
    x: int
    y: int

    def __post_init__(self):
        def validate_coord(coordinate: int) -> None:
            if not 0 <= coordinate <= 9:
                raise InvalidCoordinatesError()

        validate_coord(self.x)
        validate_coord(self.y)


@dataclass
class Octopus:
    energy_level: int

    @property
    def is_flashing(self) -> bool:
        return self.energy_level > 9

    def reset_energy_level(self) -> None:
        self.energy_level = 0


def get_adjacent_coordinates(coords: XYCoords) -> List[XYCoords]:
    adjacent_coords = []
    possible_coords = (
        (0, 1),
        (0, -1),
        (1, 0),
        (-1, 0),
        (1, 1),
        (1, -1),
        (-1, -1),
        (-1, 1),
    )
    for p_coord in possible_coords:
        try:
            adjacent_coords.append(
                XYCoords(x=coords.x + p_coord[0], y=coords.y + p_coord[1])
            )
        except InvalidCoordinatesError:
            pass
    return adjacent_coords


@dataclass
class OctopusBoard:
    data: Dict[XYCoords, Octopus]

    def is_synchronized(self):
        return len(set(o.energy_level for o in self.data.values())) == 1

    def get_flashing_octopuses_count(self) -> int:
        return sum(1 for oc in self.data.values() if oc.is_flashing)

    def get_flashing_octopuses_coords(self):
        return [k for k, oc in self.data.items() if oc.is_flashing]

    def reset_flashing_octopuses_energy_levels(self) -> None:
        for oc in self.data.values():
            if oc.is_flashing:
                oc.reset_energy_level()

    def increment_energy_levels(self, coords: Optional[List[XYCoords]] = None):
        if coords:
            for coord in coords:
                self.data[coord].energy_level += 1
            return
        for oc in self.data.values():
            oc.energy_level += 1

    def trigger_flashing_octopuses(
        self, coords: List[XYCoords], flashed_coords=None, adjacent_coords=None
    ) -> int:
        if not flashed_coords:
            flashed_coords = set()
        if not coords:
            return len(flashed_coords)
        coord = coords[0]
        adjacent_coords = get_adjacent_coordinates(coord)
        self.increment_energy_levels(adjacent_coords)
        flashed_coords.add(coord)
        coords = [coord for coord in coords[1:] if coord not in flashed_coords]
        coords += [
            adj_coord
            for adj_coord in adjacent_coords
            if self.data[adj_coord].is_flashing and adj_coord not in flashed_coords
        ]
        return self.trigger_flashing_octopuses(coords, flashed_coords)

    def run_simulation(self, steps: int) -> None:
        flashes_count = 0
        synchronizations = []
        for step in range(1, steps + 1):
            self.increment_energy_levels()
            flashing_coords = self.get_flashing_octopuses_coords()
            flashes_count += self.trigger_flashing_octopuses(flashing_coords)
            self.reset_flashing_octopuses_energy_levels()
            if self.is_synchronized():
                synchronizations.append(step)
        print(f"Flashes count: {flashes_count}")
        if synchronizations:
            print(f"First synchronization occured at: {synchronizations[0]}")

    @classmethod
    def from_text_file(cls, path: str):
        with open(path, "rt") as f:
            data = [line.replace("\n", "") for line in f.readlines()]
        board_data = {}
        for y, row in enumerate(data):
            for x, energy_level in enumerate(row):
                board_data[XYCoords(x=x, y=y)] = Octopus(energy_level=int(energy_level))
        return cls(board_data)


def part_1_solution(board: OctopusBoard) -> None:
    board.run_simulation(300)


if __name__ == "__main__":
    input_path = "input.txt"
    board = OctopusBoard.from_text_file(input_path)
    part_1_solution(board)
