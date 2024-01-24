# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        res_arr = []
        len_count = 0

        while head:
            res_arr.append(head)
            head = head.next
            len_count += 1

        return res_arr[len_count//2]


        
