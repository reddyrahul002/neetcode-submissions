# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()      
        list3 = dummy  
        head1=list1
        head2=list2
        while head1 and head2:
            if head2.val<=head1.val:
                list3.next=head2
                head2=head2.next
            else:
                list3.next=head1
                head1=head1.next
            list3=list3.next
        list3.next = head1 if head1 else head2
        return dummy.next
        
            

            
            

            


