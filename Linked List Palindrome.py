# Palindrome Linked List

# Given the head of a singly linked list, return true if it is a palindrome or false otherwise.



class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def isPalindrome(self, head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        prev = None
        while slow:
            nxt = slow.next
            slow.next = prev
            prev = slow
            slow = nxt
        
        while prev:
            if prev.val != head.val:
                return False
            head = head.next
            prev = prev.next
        return True
            
            