from dataclasses import dataclass
from typing import List, Sequence, Tuple

Row = List[int]

EMPTY_LINE = "\n"

BOARD_LENGTH = 5


@dataclass(frozen=True)
class BingoBoard:
    rows: List[Row]

    def __post_init__(self):
        board_length = len(self.rows)
        for row in self.rows:
            if len(row) != board_length:
                raise ValueError("Board dimensions must be the same (i.e. 5 x 5).")

    @property
    def board_length(self) -> int:
        return len(self.rows)

    @property
    def are_numbers_unique(self) -> bool:
        """
        Making sure that all numbers in particular board are unique.
        """
        return (
            len(set([num for row in self.rows for num in row]))
            == self.board_length ** 2
        )

    @classmethod
    def from_sequence_of_strings(cls, string_sequence: Sequence[str]):
        rows = [[int(x) for x in line.split(" ")] for line in string_sequence]
        return cls(rows)


def parse_game_data(path: str) -> Tuple[List[int], List[BingoBoard]]:
    with open(path, "rt") as f:
        data = f.readlines()
    drawn_numbers = [int(x) for x in data[0].split(",")]

    boards = []
    board_buffer = []
    for line in data[1:]:
        if line == EMPTY_LINE:
            continue
        board_buffer.append(line.replace("\n", "").strip().replace("  ", " "))
        if len(board_buffer) == BOARD_LENGTH:
            board = BingoBoard.from_sequence_of_strings(board_buffer)
            boards.append(board)
            board_buffer.clear()

    return drawn_numbers, boards
