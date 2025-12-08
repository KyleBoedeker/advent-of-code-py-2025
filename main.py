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

    try:
        sol = {
            "d01_p1": aoclib.day01_part1,
            "d01_p2": aoclib.day01_part2,
            "d02_p1": aoclib.day02_part1,
            "d02_p2": aoclib.day02_part2,
            "d03_p1": aoclib.day03_part1,
            "d03_p2": aoclib.day03_part2,
            "d04_p1": aoclib.day04_part1,
            "d04_p2": aoclib.day04_part2,
            "d05_p1": aoclib.day05_part1,
            "d05_p2": aoclib.day05_part2,
            "d06_p1": aoclib.day06_part1,
            "d06_p2": aoclib.day06_part2,
            "d07_p1": aoclib.day07_part1,
            "d07_p2": aoclib.day07_part2,
            "d08_p1": aoclib.day08_part1,
            "d08_p2": aoclib.day08_part2,
            "d09_p1": aoclib.day09_part1,
            "d09_p2": aoclib.day09_part2,
            "d10_p1": aoclib.day10_part1,
            "d10_p2": aoclib.day10_part2,
            "d11_p1": aoclib.day11_part1,
            "d11_p2": aoclib.day11_part2,
            "d12_p1": aoclib.day12_part1,
            "d12_p2": aoclib.day12_part2,
        }[f"d{int(args.day):02d}_p{args.part}"]

        sol(puzzle)

    except KeyError:
        print(f"d{int(args.day):02d}p{args.part}")
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
