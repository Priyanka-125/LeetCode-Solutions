# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        lenA=1
        lenB=1
        tempA=headA
        tempB=headB
        while headA:
            headA=headA.next
            lenA=lenA+1
        while headB:
            headB=headB.next
            lenB=lenB+1
        diff=0
        if lenA>lenB:
            diff=lenA-lenB
            while diff:
                tempA=tempA.next
                diff=diff-1
        else:
            diff=lenB-lenA
            while diff:
                tempB=tempB.next
                diff=diff-1
        while tempA and tempB:
            if tempA==tempB:
                return tempA
            else:
                tempA=tempA.next
                tempB=tempB.next
        
        