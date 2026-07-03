# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        ar=[]
        current=head
        while current:
            ar.append(current)
            current=current.next
        index=len(ar)-n
        ar.pop(index)
    

        if not ar:
            return None
        head=ar[0]
        for i in range(1,len(ar)):
            head.next=ar[i]
            head=head.next
        head.next=None
        return ar[0]




            

        