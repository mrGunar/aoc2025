from copy import deepcopy

data = []

with open("day4_input.txt") as f:
    for line in f.readlines():
        data.append(list(line.strip()))


part1 = 0
part2 = 0


def is_nei_below_four(field: list[list[str]], i: int, j: int) -> bool:
    checks = [
        (-1, -1),
        (-1, 0),
        (-1, 1),
        (0, -1),
        (0, 1),
        (1, -1),
        (1, 0),
        (1, 1),
    ]
    count = 0

    for dx, dy in checks:
        if 0 <= i + dx < len(field) and 0 <= j + dy < len(field[0]):
            if field[i + dx][j + dy] == "@":
                count += 1
    return count < 4


while 1:
    data_copy = deepcopy(data)
    round_count = 0
    for i, row in enumerate(data):
        for j, val in enumerate(row):
            if val == "@" and is_nei_below_four(data, i, j):
                round_count += 1
                data_copy[i][j] = "."
    if round_count == 0:
        break
    part1 = part1 or round_count
    part2 += round_count
    data = data_copy


print("Part 1: ", part1)
print("Part 2: ", part2)
