"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        

        old_new={None:None}

        current=head
        while current:
            old_new[current]=Node(current.val)
            current=current.next
        
        current=head
        while current:
           old_new[current].random = old_new[current.random]
           old_new[current].next = old_new[current.next]
           current=current.next

        return old_new[head]
        

            