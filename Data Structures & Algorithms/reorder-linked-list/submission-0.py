# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find the middle node to divide the linked list into half
        slow, fast = head, head.next
        
        while fast and fast.next:   # as long as fast reaches the end of the linked list or out
            slow = slow.next
            fast = fast.next.next
        
        second = slow.next     # second means the head of the second half
        slow.next = None   # split the half
        
        # reverse the second half
        prev = None
        while second != None:
            temp = second.next
            second.next = prev
            prev = second
            second = temp

        # merge two halves
        # note that once the second half is reversed, the "second" pointer will be None
        # only prev will be at the head of the reversed second half
        second_half_head = prev   
        first_half_head = head
        # save the next nodes of both end into a tmp variable
        while second_half_head:
            temp1, temp2 = first_half_head.next, second_half_head.next
            first_half_head.next = second_half_head
            second_half_head.next = temp1
            first_half_head = temp1
            second_half_head = temp2

# I find this relatively easy to remember:
# so using "=" equals to using "becomes" e.g. temp1 "becomes" the first half head is the same as first_half_head = temp1
# also whenever the temp variable is used, it's first used to store the next link and then eventually it will be the new head
# refer to line 34 and line 37

        