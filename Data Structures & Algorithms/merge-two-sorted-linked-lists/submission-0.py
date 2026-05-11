# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # when the output list is empty, create this dummy node as a start (the real head is the next node of this dummy node)
        # so we don't need to worry about inserting into an empty list (it's a common practice)
        dummy = ListNode()
        tail = dummy

        # list1 and list2 are the heads of each Linked List
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        # if one of them is null, add another's head directly and all of its remaining nodes
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2
        
        return dummy.next


        