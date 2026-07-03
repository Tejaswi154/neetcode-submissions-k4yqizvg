# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        ar=[]
        current=head
        while current:
            ar.append(current)
            current=current.next
        left,right=0,len(ar)-1
        while(left<right):
            ar[left].next=ar[right]
            
            left+=1
            ar[right].next=ar[left]
            right-=1
            if left==right:
                break
        ar[left].next=None
        



        