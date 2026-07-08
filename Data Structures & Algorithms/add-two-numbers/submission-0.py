# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def list_to_num(head):
            num=0
            place=1
            while head:
                num+=head.val*place
                place*=10
                head=head.next
            return num
        num1=list_to_num(l1)
        num2=list_to_num(l2)
        number=num1+num2
        dummy=ListNode(0)
        curr=dummy
        if number==0:
            return ListNode(0)
        while(number):
            digit=number%10
            curr.next=ListNode(digit)
            curr=curr.next
            number=number//10
        return dummy.next

        
        

        