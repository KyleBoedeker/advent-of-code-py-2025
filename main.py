import argparse
import sys
import time
from pathlib import Path

import aoclib


def main(args: argparse.Namespace) -> None:
    puzzle_file = f"day{int(args.day):02d}"
    puzzle_file += "_example.txt" if args.example else "_input.txt"

    try:
        puzzle = (Path(__file__).parent / "inputs" / puzzle_file).read_text()
    except FileNotFoundError:
        print(
            f"Puzzle input not found for Day {args.day} Part {args.part}",
            f"Please create the file: input/{puzzle_file}",
            sep="\n",
            file=sys.stderr,
        )
        sys.exit(1)

    t_start = time.time()

    if args.day == "1" and args.part == "1":
        aoclib.day01_part1(puzzle)
    elif args.day == "1" and args.part == "2":
        aoclib.day01_part2(puzzle)
    elif args.day == "2" and args.part == "1":
        aoclib.day02_part1(puzzle)
    elif args.day == "2" and args.part == "2":
        aoclib.day02_part2(puzzle)
    elif args.day == "3" and args.part == "1":
        aoclib.day03_part1(puzzle)
    elif args.day == "3" and args.part == "2":
        aoclib.day03_part2(puzzle)
    else:
        print("unimplemented!", file=sys.stderr)

    if args.profile:
        print(f"Solution ran in {time.time() - t_start:.3f} seconds.", file=sys.stderr)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="Advent of Code Solver",
        description="Solves advent of code puzzles",
    )

    parser.add_argument("day", choices=list(map(str, range(1, 13))), help="Puzzle to solve: ex: '3'")
    parser.add_argument("part", choices=["1", "2"], help="Puzzle part to solve (either 1 or 2)")
    parser.add_argument("-e", "--example", action="store_true", help="Run the example instead")
    parser.add_argument("-p", "--profile", action="store_true", help="Print performance information")
    args = parser.parse_args()
    main(args)
