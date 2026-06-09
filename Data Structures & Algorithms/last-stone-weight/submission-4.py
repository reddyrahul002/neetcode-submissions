import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones=[-i for i in stones]
        heapq.heapify(stones)
        while len(stones)>1:
            heap_lar=-heapq.heappop(stones)
            heap_smal=-heapq.heappop(stones)

            if heap_lar!=heap_smal:
                heapq.heappush(stones,-(heap_lar-heap_smal))
        return -stones[0] if stones else 0




            
