from dataclasses import dataclass
from typing import List, Sequence

Row = List[int]


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
