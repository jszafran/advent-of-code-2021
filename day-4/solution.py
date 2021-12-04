from dataclasses import dataclass
from typing import Iterable, List, Sequence, Set, Tuple

Row = List[int]
Column = List[int]

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
    def columns(self) -> List[Column]:
        return [[row[i] for row in self.rows] for i in range(self.board_length)]

    @property
    def are_numbers_unique(self) -> bool:
        """
        Making sure that all numbers in particular board are unique.
        """
        return (
            len(set([num for row in self.rows for num in row]))
            == self.board_length ** 2
        )

    @property
    def all_numbers(self) -> Set[int]:
        return set([num for row in self.rows for num in row])

    def get_unmarked_numbers(self, drawn_numbers: Iterable[int]) -> Set[int]:
        return self.all_numbers - set(drawn_numbers)

    def has_won(self, drawn_numbers: List[int]) -> bool:
        drawn_numbers_set = set(drawn_numbers)
        has_winning_row = any(set(row) <= drawn_numbers_set for row in self.rows)
        has_winning_column = any(
            set(column) <= drawn_numbers_set for column in self.columns
        )
        return has_winning_row or has_winning_column

    def get_board_score(self, drawn_numbers: List[int]) -> int:
        return sum(self.get_unmarked_numbers(drawn_numbers)) * drawn_numbers[-1]

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


def calculate_winning_board_score_from_file(path: str) -> int:
    all_drawn_numbers, boards = parse_game_data(path)

    for i in range(5, len(all_drawn_numbers)):
        for board in boards:
            drawn_numbers = all_drawn_numbers[:i]
            if board.has_won(drawn_numbers):
                return board.get_board_score(drawn_numbers)


if __name__ == "__main__":
    winning_board_score = calculate_winning_board_score_from_file("input.txt")
    print(winning_board_score)
