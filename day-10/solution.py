from typing import List, Optional

ILLEGAL_CHAR_SCORES = {")": 3, "]": 57, "}": 1197, ">": 25137}

AUTOCOMPLETE_SCORES = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4,
}


def get_opening_char(char: str) -> str:
    return {
        ">": "<",
        "}": "{",
        "]": "[",
        ")": "(",
    }[char]


def get_closing_char(char: str) -> str:
    return {"<": ">", "{": "}", "[": "]", "(": ")"}[char]


def get_autocomplete_score(completion: str) -> int:
    def get_score(chars, score=0):
        if not chars:
            return score
        score = score * 5 + AUTOCOMPLETE_SCORES[chars[0]]
        return get_score(chars[1:], score)

    return get_score(completion)


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


def complete_line(line: str) -> str:
    stack = []
    for char in line:
        if char in "<{([":
            stack.append(char)
        else:
            stack.pop()
    return "".join(reversed([get_closing_char(c) for c in stack]))


def get_solution(lines: List[str]) -> None:
    part_1_solution = sum(
        ILLEGAL_CHAR_SCORES.get(get_illegal_char_for_line(line), 0) for line in lines
    )
    print(f"Part 1 solution: {part_1_solution}")
    incomplete_lines = [
        line for line in lines if get_illegal_char_for_line(line) is None
    ]
    completion_scores = [
        get_autocomplete_score(complete_line(line)) for line in incomplete_lines
    ]
    part_2_solution = sorted(completion_scores)[len(completion_scores) // 2]
    print(f"Part 2 solution: {part_2_solution}")


def get_input(path: str) -> List[str]:
    with open(path, "rt") as f:
        data = [line.replace("\n", "") for line in f.readlines()]
    return data


if __name__ == "__main__":
    input_path = "input.txt"
    lines = get_input(input_path)
    get_solution(lines)
