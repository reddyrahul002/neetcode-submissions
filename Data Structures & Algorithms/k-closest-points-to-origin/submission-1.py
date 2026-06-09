import math
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        dis=[(abs(math.sqrt( points[i][0]**2 + points[i][1]**2)),points[i]) for i in range(len(points))]
        heapq.heapify(dis)
        return [ heapq.heappop(dis)[1] for i in range(k) ]


            