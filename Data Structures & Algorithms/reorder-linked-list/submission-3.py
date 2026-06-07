# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Task1
        fast=head
        slow=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        second=slow.next
        slow.next=None
        # Task2
        prev=None
        while second:
            nxt=second.next
            second.next=prev
            prev=second
            second=nxt
        # Task3
        first=head
        second=prev
        while first and second:
            temp1=first.next
            temp2=second.next

            first.next=second
            second.next=temp1

            first=temp1
            second=temp2


        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        