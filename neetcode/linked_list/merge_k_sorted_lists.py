# You are given an array of k linked-lists lists, each linked-list is sorted in
# ascending order.

# Merge all the linked-lists into one sorted linked-list and return it.

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None

        # Runs log(k) times.
        while len(lists) > 1: 
            if len(lists) % 2 == 1:
                lists.append(None)
            wl_iter = iter(lists)
            lists = [self.mergeLists(l1, l2) for l1, l2 in zip(wl_iter, wl_iter)]
        
        return lists[0]

    def mergeLists(self, l1, l2):
        tail = ListNode('tail', None)
        dummy = ListNode('dummy', tail)

        p1 = l1
        p2 = l2
        while p1 and p2: 
            if p1.val < p2.val:
                tail.next = p1
                p1 = p1.next
            else: 
                tail.next = p2
                p2 = p2.next
            tail = tail.next

        if p1:
            tail.next = p1

        if p2:
            tail.next = p2

        return dummy.next.next

