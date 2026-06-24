class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        newInterval=intervals[0]
        result=[]
        for start,end in intervals[1:]:
            if start >  newInterval[1]:
                result.append(newInterval)
                newInterval=[start,end]
            else:
                newInterval = [min(start,newInterval[0]),max(end,newInterval[1])]
        result.append(newInterval)
        return result