from collections import defaultdict

class CountSquares:
    def __init__(self):
        self.point_count = defaultdict(int)     # tracks duplicates
        self.points = set()                      # unique points

    def add(self, point: List[int]) -> None:
        self.point_count[tuple(point)] += 1
        self.points.add(tuple(point))

    def count(self, point: List[int]) -> int:
        res = 0
        px, py = point

        for x, y in self.points:
            # diagonal opposite must differ in both x and y (no diagonals, axis-aligned only)
            if px == x or py == y:              # skip same row or same col
                continue
            if abs(px - x) != abs(py - y):     # must form a square not rectangle
                continue
            # other two corners are (px,y) and (x,py)
            res += self.point_count[(x, y)] * \
                   self.point_count[(px, y)] * \
                   self.point_count[(x, py)]

        return res