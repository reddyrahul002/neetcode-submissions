import heapq
from collections import deque, Counter
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        count=Counter(tasks)
        mxheap=[-value for value in count.values()]
        heapq.heapify(mxheap)
        
        time=0
        q=deque()

        while mxheap or q:

            time+=1

            if mxheap:
                cnt = 1 + heapq.heappop(mxheap)
                if cnt:
                    q.append((cnt,time+n))
            
            if q and q[0][1]==time:
                heapq.heappush(mxheap,q.popleft()[0])
        return time
        
    





