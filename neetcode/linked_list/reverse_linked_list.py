# Given the head of a singly linked list, reverse the list, and return the
# reversed list.

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
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None 
        curr = head 

        while curr:
            temp = curr.next # Store.
            curr.next = prev # Flip the arrow.
            prev = curr # Update what we keep track of.
            curr = temp # Advance pointer.

        return prev

    def reverseListV2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.reverseListV2Helper(head, None)

    def reverseListV2Helper(self, head: Optional[ListNode], accumulator: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return accumulator
        else:
            return self.reverseListV2Helper(head.next, ListNode(head.val, accumulator))

s = Solution()

# A -> B -> C 

l1 = ListNode('A', ListNode('B', ListNode('C', None)))
l2 = ListNode('C', ListNode('B', ListNode('A', None)))

assert s.reverseList(l1) == l2

l3 = ListNode('A', ListNode('B', ListNode('C', None)))
l4 = ListNode('C', ListNode('B', ListNode('A', None)))

assert s.reverseListV2(l3) == l4

print('ALL TESTS PASS')
