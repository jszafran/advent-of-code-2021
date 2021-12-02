from typing import List


def get_input_data() -> List[int]:
    with open("aoc-day-1-input.txt", "rt") as f:
        data = [int(line) for line in f.readlines()]
    return data


def get_increased_count(input_data: List[int]) -> int:
    index_to_value = {}

    comparisons = []
    for i, v in enumerate(input_data):
        index_to_value[i] = v
        if i == 0:
            continue
        comparisons.append(v > index_to_value[i - 1])
    return sum(comparisons)


if __name__ == "__main__":
    input_data = get_input_data()
    print(get_increased_count(input_data))
