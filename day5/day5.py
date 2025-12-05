part1 = 0
part2 = 0

with open("day5_input.txt") as f:
    ranges, ids = map(str.strip, f.read().split("\n\n"))

ids = map(int, ids.split("\n"))
ranges = [tuple(map(int, r.split("-"))) for r in ranges.split("\n")]
ranges.sort()

for idx in ids:
    for start, end in ranges:
        if idx in range(start, end + 1):
            part1 += 1
            break

marged_ranges = []
cur_start, cur_end = ranges[0]

for start, end in ranges[1:]:
    if start <= cur_end + 1:
        cur_end = max(cur_end, end)
    else:
        marged_ranges.append((cur_start, cur_end))
        cur_start, cur_end = start, end
marged_ranges.append((cur_start, cur_end))


for start, end in marged_ranges:
    part2 += end - start + 1


print("Part 1: ", part1)
print("Part 2: ", part2)
