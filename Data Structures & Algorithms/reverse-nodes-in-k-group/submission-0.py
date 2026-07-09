# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        ar=[]
        if not head:
            return None
        curr=head
        while curr:
            ar.append(curr)
            curr=curr.next
        for i in range(0,len(ar),k):
            if i+k<=len(ar):
                ar[i:i+k]=ar[i:i+k][::-1]
        dummy=ListNode(0)
        for i in range(len(ar)-1):
           ar[i].next=ar[i+1]
        ar[-1].next=None
        return ar[0]





        