# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        dummy = ListNode()
        dummy.next = head
        pre_k = dummy

        while True:

            find_k = pre_k
            for _ in range(k):
                find_k = find_k.next
                if not find_k:
                    return dummy.next

            post_k = find_k.next

            
            prev = post_k
            curr = pre_k.next

            while curr != post_k:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            temp = pre_k.next
            pre_k.next = find_k

            pre_k = temp