# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def merge(self,list1,list2):
        dummy=ListNode(0)
        tail=dummy
        while list1 and list2:
            if list1.val<list2.val:
                tail.next=list1
                list1=list1.next
                tail=tail.next
            else:
                tail.next=list2
                list2=list2.next
                tail=tail.next
            
        if list1:
            tail.next=list1
            tail=tail.next
        else:
            tail.next=list2
            tail=tail.next
        return dummy.next
            

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        if not lists:
            return None
        ans=None
        for list in lists:
            ans=self.merge(ans,list)
        return ans


        

            
        