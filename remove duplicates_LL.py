# Remove Duplicates
# Write a function to remove duplicates from an unsorted linked list. Input 1 -> 2 -> 2 -> 3 -> 4 -> 4 -> 4 -> 5 Output 1 -> 2 -> 3 -> 4 -> 5 
#LL Coding question

from linkedlist import LinkedList

def remove_duplicates(ll):
    if ll.head == None:
            return ll
    else:
        seen= set()
        currentNode = ll.head
        prevNode = None
        while currentNode:
            if currentNode.value not in seen:
                seen.add(currentNode.value)
                prevNode = currentNode
                currentNode = currentNode.next
            else:
                prevNode.next = currentNode.next
                currentNode = currentNode.next
        return ll
        

       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
    
        
            