from typing import List, Optional

ILLEGAL_CHAR_SCORES = {")": 3, "]": 57, "}": 1197, ">": 25137}


def get_opening_char(char: str) -> str:
    return {
        ">": "<",
        "}": "{",
        "]": "[",
        ")": "(",
    }[char]


def get_illegal_char_for_line(line: str) -> Optional[str]:
    illegal_char = None
    stack = []
    for char in line:
        if char in "<{([":
            stack.append(char)
        else:
            if not stack.pop() == get_opening_char(char):
                return char
    return illegal_char


def get_solution(lines: List[str]) -> None:
    part_1_solution = sum(
        ILLEGAL_CHAR_SCORES.get(get_illegal_char_for_line(line), 0) for line in lines
    )
    print(f"Part 1 solution: {part_1_solution}")


def get_input(path: str) -> List[str]:
    with open(path, "rt") as f:
        data = [line.replace("\n", "") for line in f.readlines()]
    return data


if __name__ == "__main__":
    input_path = "input.txt"
    lines = get_input(input_path)
    get_solution(lines)
