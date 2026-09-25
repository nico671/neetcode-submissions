# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # curr keeps track of the reversed part 
        curr = None
        while head:
            tmp = head.next
            head.next = curr
            curr = head
            head = tmp
        return curr