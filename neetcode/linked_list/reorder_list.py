# You are given the head of a singly linked-list. 
# The list can be represented as:

# L0 → L1 → … → Ln - 1 → Ln

# Reorder the list to be on the following form:

# L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …

# You may not modify the values in the list's nodes. Only nodes themselves may be changed.

from typing import Optional
from math import ceil

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
    def reorderList(self, head: Optional[ListNode]) -> None:
        n = self.length(head)
        if n <= 2:
            return

        indexToReverse = ceil(n // 2)

        curr = head 
        while curr and indexToReverse > 0: 
            curr = curr.next
            indexToReverse -= 1

        reversed = self.reverse(curr) 
        head = self.interleave(head, reversed, n)

    def length(self, node): 
        if not node:
            return 0
        if not isinstance(node, ListNode):
            assert False, 'Cannot check the length of non-ListNode object' 
        return 1 + self.length(node.next)

    def reverse(self, node):
        prev = None
        curr = node 
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev

    def interleave(self, l1, l2, n):
        tail = ListNode(0, None)
        dummy = ListNode(0, tail)
        first = True

        p1 = l1
        p2 = l2
        count = 0
        while count < n:
            if first:
                tail.next = p1
                p1 = p1.next
            else:
                tail.next = p2
                p2 = p2.next
            count += 1
            tail = tail.next
            first = not first

        return dummy.next.next

s = Solution()

l1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, None))))
l2 = ListNode(1, ListNode(4, ListNode(2, ListNode(3, None))))

s.reorderList(l1)
assert l1 == l2

print('ALL TESTS PASS')
