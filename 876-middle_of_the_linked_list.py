# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        h = head
        while h != None:
            stack.append(h)
            h = h.next
        
        return stack[ceil((len(stack)+1)/2)-1]
