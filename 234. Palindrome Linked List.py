# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow=head
        fast=head

        while fast and fast.next and fast.next.next:
            slow=slow.next
            fast=fast.next.next
        
        first_tail=slow
        second_head=slow.next
        prev=None
        cur=second_head
        while cur:
            nxt=cur.next
            cur.next=prev
            prev=cur
            cur=nxt
        h1=head
        h2=prev
        while h2:
            if h1.val!=h2.val:
                return False
            h1=h1.next
            h2=h2.next
        return True
