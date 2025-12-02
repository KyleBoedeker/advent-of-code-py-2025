import itertools
import re


def day01_part1(puzzle: str) -> None:
    dial_position = 50
    num_zeroes = 0

    for line in puzzle.splitlines():
        direction = -1 if line[0] == "L" else 1
        amount = int(line[1:])

        dial_position += direction * amount
        dial_position %= 100

        if dial_position == 0:
            num_zeroes += 1

    print("Actual password:", num_zeroes)


def day01_part2(puzzle: str) -> None:
    dial_position = 50
    num_zero_crossings = 0

    for line in puzzle.splitlines():
        direction = -1 if line[0] == "L" else 1
        amount = int(line[1:])

        for _ in range(amount):
            dial_position += direction
            dial_position %= 100
            if dial_position == 0:
                num_zero_crossings += 1

    print("Actual password:", num_zero_crossings)


def day02_part1(puzzle: str) -> None:
    sum_of_invalid_ids = 0
    for match in re.finditer(r"(\d+)-(\d+)", puzzle):
        for num in range(int(match.group(1)), int(match.group(2)) + 1):
            snum = str(num)
            if len(snum) % 2 == 1:
                continue
            midpoint = len(snum) // 2
            if snum[:midpoint] == snum[midpoint:]:
                sum_of_invalid_ids += num

    print("Sum of invalid IDs is:", sum_of_invalid_ids)


def day02_part2(puzzle: str) -> None:
    sum_of_invalid_ids = 0
    for match in re.finditer(r"(\d+)-(\d+)", puzzle):
        for num in range(int(match.group(1)), int(match.group(2)) + 1):
            snum = str(num)
            for slice_size in range(1, len(snum) // 2 + 1):
                try:
                    it = itertools.batched(snum, n=slice_size, strict=True)
                    first = next(it)
                    if all(b == first for b in it):
                        sum_of_invalid_ids += num
                        break
                except ValueError:
                    pass  # snum does not cleanly batch with slize_size

    print("Sum of invalid IDs is:", sum_of_invalid_ids)
