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


# def insert(rootnode, nodevalue):
#     if rootnode is None:
#         rootnode = BSTNode(nodevalue)
#         print(rootnode.data)

#     elif nodevalue< rootnode.data:
#         insert(rootnode.leftchild, nodevalue)
#     else:
#         insert(rootnode.rightchild, nodevalue)
#     return rootnode

        

BST = BSTNode(None)

insert(BST, 45)
insert(BST, 55)
insert(BST, 60)

print(BST.rightchild.rightchild.data)