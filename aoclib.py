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
