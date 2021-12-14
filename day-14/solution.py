from collections import Counter
from dataclasses import dataclass
from typing import Dict

from utils import measure_execution_time


@dataclass(frozen=True)
class Polymer:
    template: str
    pair_insertions: Dict[str, str]

    def apply_insertion(self, pair: str) -> str:
        return f"{pair[0]}{self.pair_insertions.get(pair)}"

    def simulate_step(self) -> "Polymer":
        pairs = [
            self.template[i : i + 2] for i in range(len(self.template) - 1)  # noqa
        ]
        new_template = (
            "".join(list(map(lambda pair: self.apply_insertion(pair), pairs)))
            + self.template[-1]
        )
        return Polymer(template=new_template, pair_insertions=self.pair_insertions)

    @classmethod
    def from_text_file(cls, path: str) -> "Polymer":
        with open(path, "rt") as f:
            data = [line.replace("\n", "") for line in f.readlines() if line != "\n"]
        template, *pair_insertions = data
        return cls(
            template=template,
            pair_insertions={pi[:2]: pi[-1] for pi in pair_insertions},
        )


@measure_execution_time
def part_1_solution(polymer: Polymer, steps: int = 1) -> None:
    for step in range(steps):
        polymer = polymer.simulate_step()
        print(f"{step + 1} step done.")
    mc = Counter(polymer.template).most_common()
    print(f"Part 1 answer: {mc[0][1] - mc[-1][1]}")


if __name__ == "__main__":
    input_path = "input.txt"
    polymer = Polymer.from_text_file(input_path)
    print(len(polymer.template))

    print("Part 1")
    part_1_solution(polymer, 10)

    # TODO: This will kill the computer :(
    print("Part 2")
    part_1_solution(polymer, 40)
