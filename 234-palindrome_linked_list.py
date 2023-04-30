# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        stack = []
        h = head
        while h != None:
            stack.append(h.val)
            h = h.next
        
        while head != None:
            if head.val != stack.pop():
                return False
            head = head.next
        return True
