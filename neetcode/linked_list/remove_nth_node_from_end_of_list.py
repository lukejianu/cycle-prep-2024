# Given the head of a linked list, remove the nth node from the end of the list
# and return its head.

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __eq__(self, other):
        if isinstance(other, ListNode):
            return self.val == other.val and self.next == other.next
        return False

    def __ne__(self, other):
        if isinstance(other, ListNode):
            return self.val != other.val
        return True

    def __str__(self):
        result = []
        curr = self
        while curr:
            result.append(curr.val)
            curr = curr.next
        return str(result)

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Initialize pointers.
        slow = fast = dummy = ListNode('dummy', head)

        # Create a gap of n between the pointers.
        gap = 0
        while gap < n:
            fast = fast.next
            gap += 1

        # Move both pointers until the fast is at the last node.
        while fast.next:
            slow = slow.next
            fast = fast.next

        # Since:
        # - the fast is at the last node.
        # - the fast and slow are n apart.
        # We know the slow is at the (n + 1)th node from the end.
        slow.next = slow.next.next

        return dummy.next

#     ^
# A B C D

s = Solution()

l1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, None)))))
l2 = ListNode(1, ListNode(2, ListNode(3, ListNode(5, None))))
assert s.removeNthFromEnd(l1, 2) == l2

l3 = ListNode(1, None)
l4 = None
assert s.removeNthFromEnd(l3, 1) == l4
print('ALL TESTS PASS')

