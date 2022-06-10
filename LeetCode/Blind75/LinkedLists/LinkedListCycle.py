# LEETCODE 141: Find Cycle in Linked List
# https://leetcode.com/problems/linked-list-cycle/

# Floyd's Cycle Alg
# TIME: O(n)
# SPACE: O(1)
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head is None:
            return False
        slow = head
        fast = head.next
        while slow != fast:
            if fast is None or fast.next is None:
                return False
            slow = slow.next
            fast = fast.next.next
        return True


# Hash Table
# TIME: O(n)
# SPACE: O(n)
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        nodes_seen = set()
        while head is not None:
            if head in nodes_seen:
                return True
            nodes_seen.add(head)
            head = head.next
        return False
