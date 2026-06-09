

import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k=k
        self.hep=nums
        heapq.heapify(self.hep)
        while len(self.hep) > k:        
            heapq.heappop(self.hep)
        
    def add(self, val: int) -> int:
        heapq.heappush(self.hep,val)
        if len(self.hep) > self.k:
            heapq.heappop(self.hep)

        return self.hep[0]
        



        
