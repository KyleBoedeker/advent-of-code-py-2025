import re


def day01_part1(input: str):
    dial_position = 50
    num_zeroes = 0

    for line in input.splitlines():
        dir = -1 if line[0] == "L" else 1
        amt = int(line[1:])

        dial_position += dir * amt
        dial_position %= 100

        if dial_position == 0:
            num_zeroes += 1

    print("Actual password:", num_zeroes)


def day01_part2(input: str):
    dial_position = 50
    num_zero_crossings = 0

    for line in input.splitlines():
        dir = -1 if line[0] == "L" else 1
        amt = int(line[1:])

        for _ in range(amt):
            dial_position += dir
            dial_position %= 100
            if dial_position == 0:
                num_zero_crossings += 1

    print("Actual password:", num_zero_crossings)


def day02_is_invalid_id(num: str) -> bool:
    if len(num) % 2 == 1:
        return False
    midpoint = len(num) // 2
    return num[:midpoint] == num[midpoint:]


def day02_part1(input: str):
    sum_of_invalid_ids = 0
    for match in re.finditer(r"(\d+)-(\d+)", input):
        for num in range(int(match.group(1)), int(match.group(2)) + 1):
            if day02_is_invalid_id(str(num)):
                sum_of_invalid_ids += num

    print("Sum of invalid IDs is:", sum_of_invalid_ids)
