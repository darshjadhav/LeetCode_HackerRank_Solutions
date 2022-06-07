# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
        if not headA or not headB:
            return None
        
        currA, currB = headA, headB
        
        while currA and currB and currA != currB:
            currA = currA.next
            currB = currB.next

            if currA == currB:
                return currB
            
            if not currA:
                currA = headB
                
            if not currB:
                currB = headA
                
        return currA