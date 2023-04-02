from collections import deque


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

def inorder(root):
    if root == None:
        return
    inorder(root.left)
    print(root.data)
    inorder(root.right)

def postorder(root):
    if root == None:
        return
    postorder(root.left)
    postorder(root.right)
    print(root.data)

def height(root):
    if root == None:
        return 0
    return 1 + max(height(root.left),height(root.right))

# nodes at level k;
def k_nodes(root,k):
    q = deque()
    q.append(root)
    level = 0
    while len(q):
        if level == k:
            break
        n = len(q)
        for i in range(n):
            cn = q[0]
            if cn.left != None:
                q.append(cn.left)
            if cn.right != None:
                q.append(cn.right)
            q.popleft()
        level += 1
    res = []
    for x in q:
        res.append(x.data)
    return res

def serialize_preorder(root,res):
    if root == None:
        res.append(-1)
        return
    res.append(root.data)
    serialize_preorder(root.left,res)
    serialize_preorder(root.right,res)

# Serailizing using preorder traversal
def serialize(root,res):
    serialize_preorder(root,res)
    return res

# Given a list of values deserialize it to form the tree and return the root
deserialize_index = 0
def deserialize(arr):
    global deserialize_index
    if deserialize_index == len(arr):
        return None
    if arr[deserialize_index] == -1:
        deserialize_index += 1
        return None
    
    root = Node(arr[deserialize_index])
    deserialize_index += 1
    root.left = deserialize(arr)
    root.right = deserialize(arr)
    return root


# Center of an undirected tree - Keep removing all the leaf nodes until you are left with either 1 or 2 nodes (they are center) - peeling onion concept (https://www.youtube.com/watch?v=nzF_9bjDzdc&list=PLDV1Zeh2NRsDGO4--qE8yH72HFL1Km93P&index=10&ab_channel=WilliamFiset)
    

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
# preorder(root)
# inorder(root)
# postorder(root)
# print(height(root))
# print(k_nodes(root,1))
res = serialize(root,[])
print(res)
myroot = deserialize(res)
preorder(myroot)
# print(deserialize_index)