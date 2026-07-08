# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        ar=[]
        for head in lists:
            curr=head
            while curr:
                ar.append(curr.val)
                curr=curr.next
        ar.sort()
        dummy=ListNode(0)
        curr=dummy
        for i in ar:
            curr.next=ListNode(i)
            curr=curr.next
        return dummy.next

            
        