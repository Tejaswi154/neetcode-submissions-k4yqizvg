"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        curr=head
        OldtoNew={}
        while curr:
            copy=Node(curr.val)
            OldtoNew[curr]=copy
            curr=curr.next
        curr=head
        while curr:
            copy=OldtoNew[curr]
            copy.next=OldtoNew.get(curr.next)
            copy.random=OldtoNew.get(curr.random)
            curr=curr.next
        return OldtoNew.get(head)


        