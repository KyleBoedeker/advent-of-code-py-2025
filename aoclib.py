import itertools
import math
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
        start = match.group(1)
        # Must be at _least_ one digit for start half
        half_pattern = start[: len(start) // 2] if len(start) > 1 else start
        stop = match.group(2)
        while True:
            # Next pattern is beyond range
            if int(half_pattern + half_pattern) > int(stop):
                break
            # Next pattern is within range
            if int(start) <= int(half_pattern + half_pattern):
                sum_of_invalid_ids += int(half_pattern + half_pattern)

            # Calculate next pattern
            half_pattern = str(int(half_pattern) + 1)

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


def day05_part1(puzzle: str) -> None:
    lines = iter(puzzle.splitlines())
    ranges = []
    for line in lines:
        if m := re.match(r"(\d+)-(\d+)", line):
            # Generate the ranges for inclusive matching (add one to end)
            ranges.append(range(int(m.group(1)), int(m.group(2)) + 1))
        else:
            break  # empty line delineates input sections

    num_fresh_ingredients = 0
    # How many ingredients are in any of the ranges?
    for line in lines:
        if any(int(line) in r for r in ranges):
            num_fresh_ingredients += 1

    print("Number of fresh ingredients:", num_fresh_ingredients)


def day05_part2(puzzle: str) -> None:
    lines = iter(puzzle.splitlines())
    ranges = []
    for line in lines:
        if m := re.match(r"(\d+)-(\d+)", line):
            ranges.append(range(int(m.group(1)), int(m.group(2))))
        else:
            break  # empty line delineates input sections

    ranges = sorted(ranges, key=lambda r: r.start)
    pruned_ranges = []
    cur_start, cur_stop = ranges[0].start, ranges[0].stop

    for r in ranges[1:]:
        # Touching or overlap
        if r.start <= cur_stop:
            cur_stop = max(cur_stop, r.stop)
        else:
            pruned_ranges.append(range(cur_start, cur_stop))
            cur_start, cur_stop = r.start, r.stop

    # Don't forget the final range
    pruned_ranges.append(range(cur_start, cur_stop))

    # Don't forget to add one for each range to account for inclusive ends on ranges
    print("Number of fresh ingredient IDs:", sum(len(r) for r in pruned_ranges) + len(pruned_ranges))


def day06_part1(puzzle: str) -> None:
    lines = iter(puzzle.splitlines())

    # Abuse the fact the for loop will preserve this on last iter
    line = ""
    psets = []
    for line_idx, line in enumerate(lines):
        match_idx = None
        for match_idx, match in enumerate(re.finditer(r"\d+", line)):
            # Handle initializing the list of each column's values
            if line_idx == 0:
                psets.append([])
            psets[match_idx].append(int(match[0]))

        # No numbers were found on this line past here - must be the math operations
        if match_idx is None:
            break

    sum_of_solutions = 0
    for idx, op in enumerate(line.split()):
        if op == "*":
            sum_of_solutions += math.prod(psets[idx])
        elif op == "+":
            sum_of_solutions += sum(psets[idx])

    print("Grand total (sum of solutions): ", sum_of_solutions)


def day06_part2(puzzle: str) -> None:
    lines = puzzle.splitlines()

    ops = [c for c in lines[-1] if c in ["+", "*"]]

    # Build up offsets for start of a single math problem
    offsets = [idx for idx, c in enumerate(lines[-1]) if c in ["+", "*"]]
    # Append a final offset to get the rightmost number
    # Note: I'm uusing max to avoid strip-trailing-whitespace-on-save issue
    offsets.append(max(len(line) for line in lines) + 1)

    sum_of_solutions = 0

    # Column offsets for each puzzle
    for op, (start, end) in zip(ops, itertools.pairwise(offsets)):
        # Numbers are vertical - some questionable logic here:
        nums = []
        for col in range(start, end - 1):
            num = int("".join([l[col] for l in lines[:-1] if l[col] != " "]))
            nums.append(num)
        if op == "*":
            sum_of_solutions += math.prod(nums)
        elif op == "+":
            sum_of_solutions += sum(nums)

    print("Grand total (sum of solutions): ", sum_of_solutions)


def day07_part1(puzzle: str) -> None:
    raise NotImplementedError("not implemented")


def day07_part2(puzzle: str) -> None:
    raise NotImplementedError("not implemented")


def day08_part1(puzzle: str) -> None:
    raise NotImplementedError("not implemented")


def day08_part2(puzzle: str) -> None:
    raise NotImplementedError("not implemented")


def day09_part1(puzzle: str) -> None:
    raise NotImplementedError("not implemented")


def day09_part2(puzzle: str) -> None:
    raise NotImplementedError("not implemented")


def day10_part1(puzzle: str) -> None:
    raise NotImplementedError("not implemented")


def day10_part2(puzzle: str) -> None:
    raise NotImplementedError("not implemented")


def day11_part1(puzzle: str) -> None:
    raise NotImplementedError("not implemented")


def day11_part2(puzzle: str) -> None:
    raise NotImplementedError("not implemented")


def day12_part1(puzzle: str) -> None:
    raise NotImplementedError("not implemented")


def day12_part2(puzzle: str) -> None:
    raise NotImplementedError("not implemented")
