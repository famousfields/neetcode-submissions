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

        oldToNew = {None : None}

        cur = head
        while cur:
            copy = Node(cur.val)#creates a new node with value of the current node (copy)
            oldToNew[cur] = copy # uses the current node as a key and maps it to copy
            cur = cur.next
        
        cur = head
        while cur:#assigning pointers
            copy = oldToNew[cur]
            copy.next = oldToNew[cur.next]
            copy.random = oldToNew[cur.random]
            cur = cur.next

        return oldToNew[head]