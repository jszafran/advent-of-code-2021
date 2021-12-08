from typing import List, Tuple

InputRow = Tuple[List[str], List[str]]


def get_input_data(path: str) -> List[InputRow]:
    input_rows = []
    with open(path, "rt") as f:
        rows = [row.replace("\n", "") for row in f.readlines()]
        for row in rows:
            row_split = row.split(" | ")
            input_rows.append((row_split[0].split(" "), row_split[1].split(" ")))
    return input_rows


if __name__ == "__main__":
    input_path = "test_input.txt"
    parsed_data = get_input_data(input_path)
    for row in parsed_data:
        print(row)
