"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # two passes
        # create a hashmap, and each pair is curr -> copy
        # then we link the copied nodes
        oldToCopy = { None: None }  # it's possible that the node and node.next are both null

        curr = head
        while curr:
            copy = Node(curr.val)   # create a copy node out of the old node
            oldToCopy[curr] = copy
            curr = curr.next

        curr = head
        while curr:
            copy = oldToCopy[curr]
            copy.next = oldToCopy[curr.next]  # curr.next and copy.next can be null, so oldToCopy needs to initialize { None: None } 
            copy.random = oldToCopy[curr.random]   # e.g. point the copy of the 3rd node's random to the copy of the 5th node
            curr = curr.next

        return oldToCopy[head]  # as we've copied every node in the hashmap
        