# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True

        slow_p = head
        fast_p = head
        while fast_p and fast_p.next:
            slow_p = slow_p.next
            fast_p = fast_p.next.next

        prev = None
        current = slow_p
        while current:
            next_node = current.next  
            current.next = prev       
            prev = current
            current = next_node
        
        first_half = head
        second_half = prev
        
        while second_half: 
            if first_half.val != second_half.val:
                return False 
            
            first_half = first_half.next
            second_half = second_half.next
            
        return True 