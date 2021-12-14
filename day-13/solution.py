from dataclasses import dataclass
from typing import List, Set, Tuple


@dataclass(frozen=True)
class FoldCommand:
    axis: str
    position: int


@dataclass(frozen=True)
class Point:
    x: int
    y: int


@dataclass(frozen=True)
class OrigamiPaper:
    points: Set[Point]

    def apply_fold_command(self, c: FoldCommand) -> "OrigamiPaper":
        fold_pos = c.position
        if c.axis == "y":
            unaltered_points = {
                Point(x=p.x, y=p.y) for p in self.points if p.y < fold_pos
            }
            altered_points = {
                Point(x=p.x, y=2 * fold_pos - p.y)
                for p in self.points
                if p.y > fold_pos
            }
            return OrigamiPaper(points=unaltered_points | altered_points)
        if c.axis == "x":
            unaltered_points = {
                Point(x=p.x, y=p.y) for p in self.points if p.x < fold_pos
            }
            altered_points = {
                Point(x=2 * fold_pos - p.x, y=p.y)
                for p in self.points
                if p.x > fold_pos
            }
            return OrigamiPaper(points=unaltered_points | altered_points)

    @property
    def visible_points(self) -> int:
        return len(self.points)

    def visualize(self) -> None:
        def print_row(row: List[Point]) -> None:
            print("".join(["." if p in self.points else " " for p in row]))

        max_x = max(p.x for p in self.points)
        max_y = max(p.y for p in self.points)
        for y in range(max_y + 1):
            row = []
            for x in range(max_x + 1):
                row.append(Point(x=x, y=y))
            print_row(row)


def get_input_data(path: str) -> Tuple[List[FoldCommand], OrigamiPaper]:
    def parse_point_line(line: str) -> Point:
        line_split = line.split(",")
        return Point(x=int(line_split[0]), y=int(line_split[1]))

    def parse_command_line(line: str) -> FoldCommand:
        line_split = line.replace("fold along ", "").split("=")
        return FoldCommand(axis=line_split[0], position=int(line_split[1]))

    with open(path, "rt") as f:
        data = [line.replace("\n", "") for line in f.readlines()]
    split_pos = data.index("")
    points = [parse_point_line(p_line) for p_line in data[:split_pos]]
    commands = [parse_command_line(c_line) for c_line in data[split_pos + 1 :]]  # noqa
    return commands, OrigamiPaper(points=set(points))


def part_1_solution(
    origami_paper: OrigamiPaper, fold_commands: List[FoldCommand]
) -> None:
    paper_1 = origami_paper.apply_fold_command(fold_commands[0])
    print(paper_1.apply_fold_command(commands[0]).visible_points)

    folded_paper = origami_paper
    for command in commands:
        folded_paper = folded_paper.apply_fold_command(command)
    folded_paper.visualize()


if __name__ == "__main__":
    input_path = "input.txt"
    commands, origami_paper = get_input_data(input_path)
    part_1_solution(origami_paper, commands)
