# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        arr1=""
        while l1:
            arr1=arr1+str(l1.val)
            l1=l1.next
        arr1=arr1[::-1]
        
        arr2=""
        while l2:
            arr2=arr2+str(l2.val)
            l2=l2.next
        arr2=arr2[::-1]
        
        sum1=0
        sum1=int(arr1)+int(arr2)
        sum1=str(sum1)
        sum1=sum1[::-1]
        
        dummy=ListNode(0)
        head=dummy
        for i in sum1:
            newnode=ListNode(i)
            head.next=newnode
            head=head.next
        return dummy.next
        