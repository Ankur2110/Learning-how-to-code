# Remove Duplicates

# Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well. 

# Example 1:

#     Input: head = [1,1,2]
#     Output: [1,2]

# Example 2:

#     Input: head = [1,1,2,3,3]
#     Output: [1,2,3]



class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def deleteDuplicates(self, head):
        if head == None:
            return head
        current_node = head
        prev_node = None
        seen = set()
        while current_node:
            if current_node.val not in seen:
                seen.add(current_node.val)
                prev_node = current_node
            else:
                prev_node.next = current_node.next
            current_node = current_node.next
        return head
            
            
            
            
            
                
                
                