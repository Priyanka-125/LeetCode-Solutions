# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k==1:
            return head
        temp=head
        dummy=ListNode()
        l=0
        curr=head
        while temp:
            temp=temp.next
            l=l+1
        temp=dummy
        for i in range(l//k):
            prev=None
            for x in range(k):
                tail=curr.next
                curr.next=prev
                prev=curr
                curr=tail
                
            temp.next=prev
            for a in range(k):
                temp=temp.next 
        temp.next=curr
        return dummy.next