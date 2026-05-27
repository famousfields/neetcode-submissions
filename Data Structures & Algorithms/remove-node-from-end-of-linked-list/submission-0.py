# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 1,2,3,4 n = 2
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(next = head)
        
        cur = head
        i = 0
        for i in range(n):
            cur = cur.next

        prev = dummy
        while cur:
            cur = cur.next
            prev = prev.next
        prev.next = prev.next.next
        return dummy.next