from collections import Counter
from functools import partial
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


def get_life_support_rating(nums: List[str]) -> int:
    # trying to use more functional programming style
    def generic_bit_criteria(mc_index: int, default: str, c: Counter) -> str:
        mc = c.most_common()
        if mc[0][1] == mc[1][1]:
            return default
        return mc[mc_index][0]

    oxygen_generator_bit_criteria = partial(generic_bit_criteria, 0, "1")
    co2_scrubber_bit_criteria = partial(generic_bit_criteria, -1, "0")

    def calculate_rate_by_bit_criteria(
        numbers: List[str], bit_criteria, ix: int = 0
    ) -> str:
        if len(numbers) == 1:
            return numbers[0]
        dominating_bit = bit_criteria(Counter([n[ix] for n in numbers]))
        filtered_numbers = list(filter(lambda x: x[ix] == dominating_bit, numbers))
        return calculate_rate_by_bit_criteria(filtered_numbers, bit_criteria, ix + 1)

    oxygen_rate = binary_str_to_int(
        calculate_rate_by_bit_criteria(nums, oxygen_generator_bit_criteria)
    )
    co2_scrubber_rate = binary_str_to_int(
        calculate_rate_by_bit_criteria(nums, co2_scrubber_bit_criteria)
    )

    return oxygen_rate * co2_scrubber_rate


if __name__ == "__main__":
    test_data = [
        "00100",
        "11110",
        "10110",
        "10111",
        "10101",
        "01111",
        "00111",
        "11100",
        "10000",
        "11001",
        "00010",
        "01010",
    ]
    input_data = get_data()
    print(solution(input_data))
    print(get_life_support_rating(test_data))
    print(get_life_support_rating(input_data))
