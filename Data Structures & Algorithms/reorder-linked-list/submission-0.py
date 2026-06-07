# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast=head
        slow=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        
        second = slow.next
        slow.next=None
        
        prev=None
        current =second
        while current:
            next = current.next
            current.next=prev
            prev=current
            current=next
        
        second = prev
        first = head

        while first and second:
            temp1=first.next
            temp2=second.next

            first.next=second
            second.next=temp1
            
            first=temp1
            second=temp2
        
        # return head

        

            
 

        