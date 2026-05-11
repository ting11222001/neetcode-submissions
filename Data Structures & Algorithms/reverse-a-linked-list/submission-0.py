# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # "Define a method called reverseList that takes in the head of a singly linked list (which might be None) 
        # and returns the head of the reversed linked list (also possibly None)."
        prev = None
        curr = head

        while curr != None:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        return prev  # prev becomes the current head

            
        