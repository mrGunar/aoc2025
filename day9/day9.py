from __future__ import annotations
from dataclasses import dataclass
from itertools import permutations


@dataclass(frozen=True)
class Point:
    x: int
    y: int

    def area_with(self, other: Point) -> int:
        return (self.x - other.x + 1) * (self.y - other.y + 1)

    def __gt__(self, other: Point) -> bool:
        return (self.x, self.y) > (other.x, other.y)


def largest_red_rectangle(lines: list[Point]) -> int:
    return max([p2.area_with(p1) for (p2, p1) in permutations(lines, 2) if p2 > p1])


with open("day9_input.txt") as f:
    lines = [Point(*(map(int, line.strip().split(",")))) for line in f]
result = largest_red_rectangle(lines)
print("Part 1: ", result)
