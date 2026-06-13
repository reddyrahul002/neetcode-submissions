class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        store={0:0,1:0}
        def mincost(x):
            if x in store:
                return store[x]
            store[x]=min(mincost(x-1)+cost[x-1],mincost(x-2)+cost[x-2])
            return store[x]
        
        return mincost(len(cost))


        