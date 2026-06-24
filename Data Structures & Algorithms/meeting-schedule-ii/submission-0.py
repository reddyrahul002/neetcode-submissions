"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        
        
        if not intervals:
            return 0
        
        starts = sorted(x.start for x in intervals)
        ends = sorted(x.end for x in intervals)

        room = 0
        max_rooms = 0
        i,j=0,0
        
        while i<len(starts):

            if starts[i]< ends[j]:
                room+=1
                i+=1
            else:
                room-=1
                j+=1

            max_rooms=max(max_rooms,room)
        return max_rooms
