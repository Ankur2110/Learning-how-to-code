import queue_using_linked_lists as queue

class BSTNode:
    def __init__(self, data):
        self.data = data
        self.leftchild = None
        self.rightchild = None

    
def insert(rootnode, nodevalue):
    if rootnode is None:
        print("Creating new node with value:", nodevalue)
        return BSTNode(nodevalue)
    elif rootnode.data is None:
        rootnode.data = nodevalue
        return rootnode
    elif nodevalue < rootnode.data:
        print("Inserting", nodevalue, "into left subtree of", rootnode.data)
        rootnode.leftchild = insert(rootnode.leftchild, nodevalue)
    else:
        print("Inserting", nodevalue, "into right subtree of", rootnode.data)
        rootnode.rightchild = insert(rootnode.rightchild, nodevalue)
    return rootnode


def postorderTraversal(rootnode):
    if not rootnode:
        return
    postorderTraversal(rootnode.leftchild)
    postorderTraversal(rootnode.rightchild)
    print(rootnode.data)


def preOrderTraversal(rootnode):
    if not rootnode:
        return
    else:
        print (rootnode.data)
        preOrderTraversal(rootnode.leftChild)
        preOrderTraversal(rootnode.rightChild)



def inOrderTraversal(rootnode):
    if not rootnode:
        return
    else:
        inOrderTraversal(rootnode.leftChild)
        print (rootnode.data)
        inOrderTraversal(rootnode.rightChild)


def levelordertraversal(rootnode):
    if not rootnode:
        return
    custom_queue = queue.queue()
    custom_queue.enqueue(rootnode)
    while not custom_queue.isempty():
        root = custom_queue.dequeue()
        print (root.value.data)
        if root.value.leftChild:
            custom_queue.enqueue(root.value.leftchild)
        if root.value.rightChild:
            custom_queue.enqueue(root.value.rightchild)

def search(rootnode, search_value):
    if not rootnode:
        return False
    if rootnode.data == search_value:
        return True
    elif search_value < rootnode.data:
        return search(rootnode.leftchild, search_value)
    else:
        return search(rootnode.rightchild, search_value)
    return False

    



BST = BSTNode(25)

insert(BST, 45)
insert(BST, 55)
insert(BST, 60)

print(search(BST,55))