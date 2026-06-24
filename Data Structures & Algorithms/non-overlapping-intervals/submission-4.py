class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        count=0
        intervals.sort()
        newintervals=intervals[0]
        for start,end in intervals[1:]:
            if start >= newintervals[1]:
                newintervals=[start,end]
            else:
                count+=1
                newintervals=[newintervals[0],min(end,newintervals[1])]
        return count


            
        