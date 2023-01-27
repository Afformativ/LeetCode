# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
     def middleNode(self, head: ListNode) -> ListNode:
        slow = fast = head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        return slow


#Second
class Solution:
     def middleNode(self, head: ListNode) -> ListNode:
        arr=[]
        node=head
        while node is not None:
          arr.append(node)
          node=node.next
        return arr[len(arr)//2]
