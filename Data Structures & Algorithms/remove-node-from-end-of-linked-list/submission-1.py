# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        N=0
        current=head
        while current:
            N+=1
    
            current=current.next
        index=N-n
       
        current=head
        i=0
        if index==0:
            return head.next
        while  i<index-1:
            current=current.next
            i+=1
        current.next=current.next.next
        return head
        




            

        