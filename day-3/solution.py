from collections import Counter
from typing import List


def binary_str_to_int(s: str) -> int:
    return int(s, 2)


def get_data() -> List[str]:
    with open("aoc-day-3-input.txt", "rt") as f:
        data = [x.replace("\n", "") for x in f.readlines()]
    return data


def solution(input_data: List[str]) -> int:
    # sanity check for input data - all numbers must be of same length
    assert len(set([len(line) for line in input_data])) == 1  # noqa

    num_length = len(input_data[0])

    gamma_rate_str = ""
    epsilon_rate_str = ""

    for i in range(num_length):
        most_common = Counter([line[i] for line in input_data]).most_common()
        gamma_rate_str += most_common[0][0]
        epsilon_rate_str += most_common[1][0]

    gamma_rate = binary_str_to_int(gamma_rate_str)
    epsilon_rate_str = binary_str_to_int(epsilon_rate_str)

    return gamma_rate * epsilon_rate_str


if __name__ == "__main__":
    input_data = get_data()
    print(solution(input_data))
