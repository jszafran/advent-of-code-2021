from typing import List, Tuple

InputRow = Tuple[List[str], List[str]]

# 1 - 2
# 4 - 4
# 7 - 3
# 8 - 7

unique_segment_numbers = {2, 4, 3, 7}


def get_input_data(path: str) -> List[InputRow]:
    input_rows = []
    with open(path, "rt") as f:
        rows = [row.replace("\n", "") for row in f.readlines()]
        for row in rows:
            row_split = row.split(" | ")
            input_rows.append((row_split[0].split(" "), row_split[1].split(" ")))
    return input_rows


def part_1_solution(rows: List[InputRow]) -> int:
    output_digits = [row[1] for row in rows]
    return len(
        [
            len(num)
            for out_dig in output_digits
            for num in out_dig
            if len(num) in unique_segment_numbers
        ]
    )


if __name__ == "__main__":
    input_path = "input.txt"
    parsed_data = get_input_data(input_path)
    print(part_1_solution(parsed_data))
