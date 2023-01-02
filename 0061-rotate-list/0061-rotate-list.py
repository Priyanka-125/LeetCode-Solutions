# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        l=1
        if not head or not head.next: return head
        temp=head
        while temp.next:
            temp=temp.next
            l=l+1
        temp.next=head
        curr=head
        for x in range( l- (k%l)-1 ):
            curr = curr.next
        newhead=curr.next
        curr.next=None
        return newhead
        
        