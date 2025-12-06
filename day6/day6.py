import operator
from functools import reduce

part1 = 0
part2 = 0

operation = {
    "*": operator.mul,
    "+": operator.add,
}

with open("day6_input.txt") as f:
    lines = [line.rstrip("\n") for line in f]


# Part 1
data_for_part1, operators = lines[:-1], lines[-1]
operators = [op for op in operators.split() if op]

data_for_part1 = [list(map(int, row.split())) for row in data_for_part1]

for col_values, op in zip(zip(*data_for_part1), operators):
    part1 += reduce(operation[op], col_values)

# Part 2
cur_operator = None
temp_res = 0
num_rows = len(lines) - 1
operators = list(lines[-1].strip())

for col in range(len(lines[0])):
    vert_line = [lines[row][col] for row in range(num_rows)]

    number_as_str = "".join(vert_line).strip()
    cur_operator = cur_operator or operators[col].strip()
    if number_as_str:
        number = int(number_as_str)
        temp_res = operation[cur_operator](temp_res, number) if temp_res else number
    else:
        cur_operator = None
        part2 += temp_res
        temp_res = 0
if temp_res:
    part2 += temp_res

print("Part 1: ", part1)
print("Part 2: ", part2)
