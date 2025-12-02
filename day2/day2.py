part1_res = 0
part2_res = 0

with open("day2_input.txt") as f:
    data = f.read().strip().split(",")


def check_invalid_id_part1(num: str):
    if str(n)[: len(str(n)) // 2] == str(n)[len(str(n)) // 2 :]:
        yield n


def check_invalid_id_part2(num: str):
    len_of_number = len(num)

    nums = []
    for i in range(1, len_of_number // 2 + 1):
        for k in range(0, len(num), i):
            n = num[k : k + i]
            nums.append(n)
        if all(nums[0] == k for k in nums):
            return int(num)
        nums.clear()
    return 0


for line in data:
    first, last = list(map(int, line.split("-")))
    for n in range(first, last + 1):
        for num in check_invalid_id_part1(str(n)):
            part1_res += num

        part2_res += check_invalid_id_part2(str(n))

print("Part 1: ", part1_res)
print("Part 2: ", part2_res)
