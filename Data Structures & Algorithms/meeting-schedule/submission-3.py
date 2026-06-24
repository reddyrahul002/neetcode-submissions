"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:


        intervals.sort(key=lambda x:x.start)
        if intervals:
            new_interval =intervals[0]
        else:
            return True
        for x in intervals[1:]:

            if x.start >= new_interval.end:
                new_interval = x
            else:
                return False
        
        return True
