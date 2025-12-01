import aoclib
from pathlib import Path
import sys
import argparse


def main():
    parser = argparse.ArgumentParser(
        prog="Advent of Code Solver",
        description="Solves advent of code puzzles",
    )

    parser.add_argument(
        "day", choices=list(map(str, range(1, 13))), help="Puzzle to solve: ex: '3'"
    )
    parser.add_argument(
        "part", choices=["1", "2"], help="Puzzle part to solve (either 1 or 2)"
    )
    parser.add_argument(
        "-e", "--example", action="store_true", help="Run the example instead"
    )
    args = parser.parse_args()

    try:
        puzzle_file = (
            f"{int(args.day):02d}_{int(args.part):d}"
            + ("_e" if args.example else "")
            + ".txt"
        )
        puzzle = (Path(__file__).parent / "inputs" / puzzle_file).read_text()
    except FileNotFoundError:
        print(
            f"Puzzle input not found for day {args.day} part {args.part}",
            file=sys.stderr,
        )
        exit(1)

    if args.day == "1" and args.part == "1":
        aoclib.day01_part1(puzzle)
    else:
        print("unimplemented!", file=sys.stderr)


if __name__ == "__main__":
    main()
