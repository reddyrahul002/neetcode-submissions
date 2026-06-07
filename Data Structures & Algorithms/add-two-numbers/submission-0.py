# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head1=l1
        head2=l2
        head3=ListNode(0)
        l3=head3
        carry=0
        while l1 or l2:

            sum1=l1.val if l1 else 0
            sum2=l2.val if l2 else 0
            sum = sum1+sum2+carry
            carry=sum//10
            s=ListNode(sum%10)
            l3.next=s
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            l3=s
            
        if carry > 0:
            l3.next=ListNode(carry)
        return head3.next

