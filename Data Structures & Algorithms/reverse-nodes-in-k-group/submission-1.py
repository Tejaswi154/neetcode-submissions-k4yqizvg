# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy=ListNode(0)
        tail=dummy
        curr=head
        while curr:
            count=0
            temp=curr
            stack=[]
            while temp and count<k:
                stack.append(temp)
                temp=temp.next
                count+=1
            if count==k:
                while stack:
                    node=stack.pop()
                    tail.next=node
                    tail=tail.next
                tail.next=None   
                curr=temp
            else:
                tail.next=curr
                break
        
        return dummy.next
            

            

        




        