# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        temp = head
        l1 = []
        l2=[]
        while temp:
            l1.append(temp.val)
            l2.append(temp.val)
            temp=temp.next
        if l1==l2[::-1]:
            return True
        return False
        