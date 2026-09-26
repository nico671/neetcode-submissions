# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        elif not list2:
            return list1
        if list1.val <= list2.val:
            res_head = list1
            list1 = list1.next
        else:
            res_head = list2
            list2 = list2.next
        res = res_head
        while list1 and list2:
            if list1.val <= list2.val:
                res_head.next = list1
                list1 = list1.next
            else:
                res_head.next = list2
                list2 = list2.next

            res_head = res_head.next

        if list1:
            res_head.next = list1
        else:
            res_head.next = list2
        return res