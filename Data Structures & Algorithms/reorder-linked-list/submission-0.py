# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return
        
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next


        prev = None
        curr = slow.next
        slow.next = None
        while curr:
            temp  = curr.next
            curr.next = prev
            prev = curr
            curr = temp


        s = head
        while s and prev:
            temp = s.next
            temp2 = prev.next
            s.next = prev
            prev.next = temp
            prev = temp2
            s = temp

        return

