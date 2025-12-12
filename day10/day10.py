from itertools import combinations
import re


def parse_machine(line: str) -> tuple[list[int], list[list[int]]]:

    bracket_part = re.search(r"\[(.*?)\]", line).group(1)
    target = [1 if ch == "#" else 0 for ch in bracket_part]
    buttons = []

    for match in re.finditer(r"\(([^)]+)\)", line):
        nums = list(map(int, match.group(1).split(",")))
        vec = [0] * len(target)
        for idx in nums:
            vec[idx] = 1
        buttons.append(vec)

    return target, buttons


def xor_vecs(vecs: list[list[int]]) -> list[int]:
    res = vecs[0][:]
    for v in vecs[1:]:
        for i, _ in enumerate(v):
            res[i] ^= v[i]
    return res


def min_presses(target: list[int], buttons: list[list[int]]) -> int:
    m = len(buttons)

    for k in range(1, m + 1):
        for combo in combinations(range(m), k):
            chosen = [buttons[i] for i in combo]
            if xor_vecs(chosen) == target:
                return k
    return 0


with open("day10_input.txt") as f:
    data = f.read()

total = 0
for line in data.strip().splitlines():
    target, buttons = parse_machine(line)
    total += min_presses(target, buttons)

print("Part 1: ", total)
