# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        cur = head

        while cur.next:
            if cur.next.val > cur.val:
                cur = cur.next
            else:
                return True
            
        return cur.next is not None
        