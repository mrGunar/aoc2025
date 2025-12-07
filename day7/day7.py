with open("day7_input.txt") as f:
    field = [list(line.strip()) for line in f]

start_x, start_y = 0, 0
for y, value in enumerate(field[0]):
    if value == "S":
        start_x, start_y = 0, y
        field[0][y] = "."
        break


def part1():
    beams = [(start_x, start_y)]
    split_count = 0

    while beams:
        new_beams = []

        for beam_x, beam_y in beams:
            next_x = beam_x + 1

            if next_x >= len(field):
                break

            next_cell = field[next_x][beam_y]

            if next_cell == "^":
                split_count += 1

                left_y = beam_y - 1
                right_y = beam_y + 1

                if left_y >= 0:
                    new_beams.append((next_x, left_y))
                if right_y < len(field[0]):
                    new_beams.append((next_x, right_y))

            elif next_cell == ".":
                new_beams.append((next_x, beam_y))

        beams = list(set(new_beams))

    print("Part 1:", split_count)


def part2():
    cache = {}

    def count_timelines(x, y):
        if (x, y) in cache:
            return cache[(x, y)]

        if x >= len(field) - 1:
            cache[(x, y)] = 1
            return 1

        next_x = x + 1

        if field[next_x][y] == "^":
            left_count = 0
            right_count = 0

            left_y = y - 1
            if left_y >= 0:
                left_count = count_timelines(next_x, left_y)

            right_y = y + 1
            if right_y < len(field[0]):
                right_count = count_timelines(next_x, right_y)

            total = left_count + right_count
            cache[(x, y)] = total
            return total
        else:
            total = count_timelines(next_x, y)
            cache[(x, y)] = total
            return total

    result = count_timelines(start_x, start_y)
    print("Part 2:", result)


part1()
part2()
