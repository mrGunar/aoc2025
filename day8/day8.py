from __future__ import annotations
from dataclasses import dataclass
import math

TOTAL_NUMBER = 1000


@dataclass
class Box:
    x: int
    y: int
    z: int


class UnionFind:
    """Disjoint Set Union - DSU."""

    def __init__(self, n: int):
        """
        parent: Each element - its own parent/root
        size: Each circuit starts with size 1 (just itself)
        components: (For the part 2)
        """
        self.parent = list(range(n))
        self.size = [1] * n
        self.components = n

    def find(self, x):
        """Find the root of the box in the curcuit."""
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        """Connect two circuits."""
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return

        if self.size[root_x] < self.size[root_y]:
            root_x, root_y = root_y, root_x

        self.parent[root_y] = root_x
        self.size[root_x] += self.size[root_y]
        self.components -= 1


def line_distance(box1: Box, box2: Box) -> float:
    return round(
        (
            abs(box1.x - box2.x) ** 2
            + abs(box1.y - box2.y) ** 2
            + abs(box1.z - box2.z) ** 2
        )
        ** 0.5,
        2,
    )


with open("day8_input.txt") as f:
    boxes = [Box(*map(int, l.strip().split(","))) for l in f]


edges = []
n = len(boxes)

for i in range(n):
    for j in range(i + 1, n):
        dist = line_distance(boxes[i], boxes[j])
        edges.append((dist, i, j))
edges.sort(key=lambda x: x[0])

# Part 1
uf = UnionFind(n)

for _, i, j in edges[:TOTAL_NUMBER]:
    uf.union(i, j)

circuits = {uf.find(i) for i in range(n)}
top_sizes = sorted([uf.size[c] for c in circuits], reverse=True)[:3]
print("Part 1: ", math.prod(top_sizes))


# Part 2
uf = UnionFind(n)
for _, i, j in edges:
    uf.union(i, j)
    if uf.components == 1:
        print("Part 2: ", boxes[i].x * boxes[j].x)
        break
