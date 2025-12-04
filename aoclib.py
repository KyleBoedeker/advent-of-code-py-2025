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


def day03_part1(puzzle: str) -> None:
    total_joulage = 0

    for line in puzzle.splitlines():
        arr = [int(v) for v in line]
        max_idx = arr.index(max(arr[:-1]))
        max_after_pos = max(arr[max_idx + 1 :])
        total_joulage += int(arr[max_idx]) * 10 + int(max_after_pos)

    print("Total joulage of all batteries:", total_joulage)


def day03_part2(puzzle: str) -> None:
    total_joulage = 0

    for line in puzzle.splitlines():
        arr = [int(v) for v in line]
        val = 0
        prior_max_idx = 0
        for dig in range(-11, 1):
            subset = arr[prior_max_idx : (dig if dig < 0 else None)]
            max_idx = prior_max_idx + subset.index(max(subset))
            prior_max_idx = max_idx + 1
            d = int(arr[max_idx])
            val = 10 * val + int(d)

        total_joulage += val

    print("Total joulage of all batteries:", total_joulage)


def day04_part1(puzzle: str) -> None:
    forklift_accessable_papers = 0
    map = [[c for c in row] for row in puzzle.splitlines()]
    ncols, nrows = len(map), len(map[0])
    for col, row in itertools.product(range(ncols), range(nrows)):
        # Skip cells that aren't paper
        if map[col][row] != "@":
            continue

        # Count qty of adjacent paper rolls
        adjacent_paper_count = 0
        for col_ofs, row_ofs in itertools.product([-1, 0, 1], [-1, 0, 1]):
            if (col_ofs, row_ofs) == (0, 0):
                continue
            ncol, nrow = col + col_ofs, row + row_ofs
            # Bounds checking
            if ncol >= ncols or ncol < 0 or nrow >= nrows or nrow < 0:
                continue
            adjacent_paper_count += int(map[ncol][nrow] == "@")
            if adjacent_paper_count >= 4:
                break

        # Was the paper forklift accessable?
        if adjacent_paper_count < 4:
            forklift_accessable_papers += 1

    print("Number of rolls of paper accessable via forklift:", forklift_accessable_papers)


def day04_part2(puzzle: str) -> None:
    forklift_accessable_papers = 0
    prior_forklift_accessable_papers = None
    map = [[c for c in row] for row in puzzle.splitlines()]
    ncols, nrows = len(map), len(map[0])
    while prior_forklift_accessable_papers != forklift_accessable_papers:
        prior_forklift_accessable_papers = forklift_accessable_papers

        for col, row in itertools.product(range(ncols), range(nrows)):
            # Skip cells that aren't paper
            if map[col][row] != "@":
                continue

            # Count qty of adjacent paper rolls
            adjacent_paper_count = 0
            for col_ofs, row_ofs in itertools.product([-1, 0, 1], [-1, 0, 1]):
                if (col_ofs, row_ofs) == (0, 0):
                    continue
                ncol, nrow = col + col_ofs, row + row_ofs
                # Bounds checking
                if ncol >= ncols or ncol < 0 or nrow >= nrows or nrow < 0:
                    continue
                adjacent_paper_count += int(map[ncol][nrow] == "@")
                if adjacent_paper_count >= 4:
                    break

            # Was the paper forklift accessable?
            if adjacent_paper_count < 4:
                forklift_accessable_papers += 1
                map[col][row] = "."

    print("Number of rolls of paper accessable via forklift:", forklift_accessable_papers)
