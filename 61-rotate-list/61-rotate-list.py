# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 0:
            return head
        
        counter = head
        listLength = 1
        while counter.next:
          listLength += 1
          counter = counter.next

        counter.next = head

        k = k%listLength # edge case
        newEnd = head
        for _ in range(listLength - k - 1):
          newEnd = newEnd.next
        newStart = newEnd.next
        newEnd.next = None
        return newStart