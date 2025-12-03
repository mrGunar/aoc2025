def find_max_number(number_as_string: str, size: int = 2) -> int:
    numbers = list(map(int, list(line)))
    num = []
    rest = []

    value_to_find = 9
    while value_to_find > 0:
        try:
            index_of_max = numbers.index(value_to_find)
        except ValueError:
            value_to_find -= 1
            continue

        if len(num) + 1 == size:
            num.append(max(rest))
            break
        if len(num) + len(rest) == size:
            num.extend(rest)
            break
        if index_of_max > len(numbers) - (size - len(num)):
            value_to_find -= 1
            continue

        # Here we have an index of the max value of the array

        rest = numbers[index_of_max + 1 :]
        num.append(numbers[index_of_max])
        if len(num) == size:
            break
        numbers = rest
        value_to_find = 9

    return int("".join(map(str, num)))


part1 = 0
part2 = 0

with open("day3_input.txt") as f:
    data = map(str.strip, f.readlines())


for line in data:
    part1 += find_max_number(line)
    part2 += find_max_number(line, size=12)

print("Part 1: ", part1)
print("Part 1: ", part2)
