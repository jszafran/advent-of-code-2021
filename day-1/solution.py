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


def get_increased_count_for_sliding_window(input_data: List[int]) -> int:
    sums = [sum(input_data[i : i + 3]) for i in range(0, len(input_data) - 2)]
    return get_increased_count(sums)


if __name__ == "__main__":
    input_data = get_input_data()
    print(get_increased_count(input_data))
    print(get_increased_count_for_sliding_window(input_data))
