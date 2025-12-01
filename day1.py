start = 50
part1_times = 0
part2_times = 0

with open("day1_input.txt") as f:
    data = map(str.strip, f.readlines())

for line in data:
    direction, value = line[0], int(line[1:])
    if direction == "R":
        step = 1
    else:
        step = -1

    for _ in range(value):
        start = (start + step) % 100
        if start == 0:
            part2_times += 1

    if start == 0:
        part1_times += 1

print("Part 1: ", part1_times)
print("Part 2: ", part2_times)
