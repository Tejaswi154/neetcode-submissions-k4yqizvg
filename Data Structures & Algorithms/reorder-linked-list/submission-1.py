# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        slow,fast=head,head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        second=slow.next
        slow.next=None
        prev=None
        current=second
        while current is not None:
            next_node=current.next
            current.next=prev
            prev=current
            current=next_node
        
        left,right=head,prev
        while right:
            temp1=left.next
            temp2=right.next
            left.next=right
            right.next=temp1
            left=temp1
            right=temp2
        



        