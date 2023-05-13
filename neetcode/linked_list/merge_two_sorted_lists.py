# You are given the heads of two sorted linked lists list1 and list2.

# Merge the two lists in a one sorted list. The list should be made by splicing
# together the nodes of the first two lists.

# Return the head of the merged linked list.

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
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, None)
        tail = dummy

        p1 = list1
        p2 = list2
        while p1 or p2:
            if not p1: 
                tail.next = p2
                break
            if not p2: 
                tail.next = p1
                break
            if p1.val < p2.val:
                tail.next = p1
                p1 = p1.next
            else:
                tail.next = p2
                p2 = p2.next
            tail = tail.next

        return dummy.next

    def mergeTwoListsV2(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1: 
            return list2
        if not list2: 
            return list1
        if list1.val < list2.val:
            return ListNode(list1.val, self.mergeTwoListsV2(list1.next, list2))
        else: 
            return ListNode(list2.val, self.mergeTwoListsV2(list1, list2.next))


s = Solution()

# .
# 1 -> 3 -> 6
# .
# 2 -> 4 -> 5

# 
l1 = ListNode(1, ListNode(3, ListNode(6, None)))
l2 = ListNode(2, ListNode(4, ListNode(5, None)))

l3 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6, None))))))

assert s.mergeTwoLists(l1, l2) == l3

l4 = ListNode(1, ListNode(3, ListNode(6, None)))
l5 = ListNode(2, ListNode(4, ListNode(5, None)))

l6 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6, None))))))

assert s.mergeTwoListsV2(l4, l5) == l6

print('ALL TESTS PASS')

