class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        odd_head,even_head=head,head.next
        odd_tail,even_tail=odd_head,even_head
        while even_tail is not None and even_tail.next is not None:
            odd_tail.next=even_tail.next
            odd_tail=odd_tail.next
            even_tail.next=odd_tail.next
            even_tail=even_tail.next

        odd_tail.next=even_head
        
        return odd_head
