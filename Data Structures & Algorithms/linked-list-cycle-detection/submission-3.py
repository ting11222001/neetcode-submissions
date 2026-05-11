# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # slow and fast pointers
        # if there's a cycle, s and f pointers will eventually meet
        slow, fast = head, head

        while fast and fast.next:  # the fast reaches the end of a linked list faster than the slow
            if slow.next == fast.next.next:
                return True
            slow = slow.next
            fast = fast.next.next

        return False