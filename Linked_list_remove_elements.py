# Remove Linked List Elements

# Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def removeElements(self, head, val):
        prehead = ListNode(-1)
        prev_node = prehead
        current_node = head
        prev_node.next = current_node
        while current_node:
            if current_node.val == val:
                prev_node.next = current_node.next
                # current_node = current_node.next
            else:    
                prev_node = current_node
                # current_node = current_node.next
            current_node = current_node.next
        else:
            return prehead.next