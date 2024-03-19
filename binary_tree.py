import queue_using_linked_lists as queue

class Treenode:

    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

    
newBT = Treenode("Drinks")
leftChild = Treenode("Hot")
rightChild = Treenode("Cold")
l_leftchild = Treenode("Tea")
r_leftchild = Treenode("coffee")
l_rightChild = Treenode("Pepsi")
r_rightChild = Treenode("Coca-cola")



newBT.leftChild = leftChild
newBT.rightChild = rightChild
leftChild.leftChild = l_leftchild
leftChild.rightChild = r_leftchild
rightChild.leftChild = l_rightChild
rightChild.rightChild = r_rightChild



def preOrderTraversal(rootnode):
    if not rootnode:
        return
    else:
        print (rootnode.data)
        preOrderTraversal(rootnode.leftChild)
        preOrderTraversal(rootnode.rightChild)


# preOrderTraversal(newBT)

def inOrderTraversal(rootnode):
    if not rootnode:
        return
    else:
        inOrderTraversal(rootnode.leftChild)
        print (rootnode.data)
        inOrderTraversal(rootnode.rightChild)

# inOrderTraversal(newBT)


def postOrderTraversal(rootnode):
    if not rootnode:
        return
    else:
        postOrderTraversal(rootnode.leftChild)
        postOrderTraversal(rootnode.rightChild)
        print(rootnode.data)

def levelOrderTraversal(rootnode):
    if not rootnode:
        return
    else:
        customqueue = queue.queue()
        customqueue.enqueue(rootnode)
        while not(customqueue.isempty()):
            root = customqueue.dequeue()
            print (root.value.data)
            if root.value.leftChild:
                customqueue.enqueue(root.value.leftChild)
            if root.value.rightChild:
                customqueue.enqueue(root.value.rightChild)



levelOrderTraversal(newBT)
