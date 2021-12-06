import pathlib
import sys


def main():
    if len(sys.argv) == 1:
        raise ValueError(
            "You must pass number of day you'd like to generate a skeleton for when running this script!"
        )

    try:
        day_number = int(sys.argv[1])
    except ValueError:
        print(f"{sys.argv[1]} must be integer! Quitting script.")
        sys.exit(1)

    directory = pathlib.Path(f"day-{day_number}")
    input_file = directory / "input.txt"
    readme_file = directory / "README.md"
    solution_file = directory / "solution.py"
    test_input_file = directory / "test_input.txt"

    if pathlib.Path(directory).exists():
        raise ValueError(f"Directory for day {day_number} already exists!")

    directory.mkdir()
    input_file.touch()
    readme_file.touch()
    solution_file.touch()
    test_input_file.touch()

    print(f"Skeleton for day number {day_number} generated successfully!")


if __name__ == "__main__":
    main()
