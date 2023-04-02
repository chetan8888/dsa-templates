class Node:
    def __init__(self,x):
        self.data = x
        self.left = None
        self.right = None

def preorder(root):
    if root == None:
        return
    print(root.data)
    preorder(root.left)
    preorder(root.right)

def search(root,x):
    cn = root
    while True:
        if cn == None:
            return None
        if cn.data == x:
            return cn
        elif cn.data < x:
            cn = cn.right
        else:
            cn = cn.left

def find_insert_position(root,x):
    while True:
        if root == None:
            return None
        elif root.data < x:
            if root.right == None:
                return root
            else:
                root = root.right
        elif root.data > x:
            if root.left == None:
                return root
            else:
                root = root.left

def insert(root,x):
    node = find_insert_position(root,x)
    if node != None:
        if x < node.data:
            node.left = Node(x)
        else:
            node.right = Node(x)
    else:
        root = Node(x)

def successor(root):
    """
    One step right and then always left
    """
    root = root.right
    while root.left:
        root = root.left
    return root.val

def predecessor(root):
    """
    One step left and then always right
    """
    root = root.left
    while root.right:
        root = root.right
    return root.val
    
def deleteNode(root,key):
    if not root:
        return None
    
    # delete from the right subtree
    if key > root.val:
        root.right = deleteNode(root.right, key)
    # delete from the left subtree
    elif key < root.val:
        root.left = deleteNode(root.left, key)
    # delete the current node
    else:
        # the node is a leaf
        if not (root.left or root.right):
            root = None
        # the node is not a leaf and has a right child
        elif root.right:
            root.val = successor(root)
            root.right = deleteNode(root.right, root.val)
        # the node is not a leaf, has no right child, and has a left child    
        else:
            root.val = predecessor(root)
            root.left = deleteNode(root.left, root.val)
                    
    return root

# BST from preorder
# https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/solutions/
    

root = Node(5)
root.left = Node(2)
root.right = Node(6)
root.left.left = Node(1)
root.left.right = Node(3)

# node = search(root,6)
# if node == None:
#     print(-1)
# else:
#     print(node.data)

# node = find_insert_position(root,4)
# if node == None:
#     print(-1)
# else:
#     print(node.data)

# insert(root,4)
# preorder(root)
# print(check_bst(root))

a = [2,4]
b = [5,4]
c = a + b
print(c)

