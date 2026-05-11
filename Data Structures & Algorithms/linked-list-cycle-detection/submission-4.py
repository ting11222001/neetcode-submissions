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

        while fast and fast.next:  # if I move the pointers first and then check, it should return the same results
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True

        return False