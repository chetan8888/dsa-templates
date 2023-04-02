class Node:
    def __init__(self,start,end):
        self.start = start
        self.end = end
        self.total = 0
        self.left = None
        self.right = None

class SegmentTree():
    def __init__(self,arr):
        self.root = self.create_tree(arr,0,len(arr)-1)

    def create_tree(self,arr,left,right):
        if left > right:
            return None
        if left == right:
            node = Node(left,right)
            node.total = arr[left]
            return node

        root = Node(left,right)
        mid = (right+left)//2
        root.left = self.create_tree(arr,left,mid)
        root.right = self.create_tree(arr,mid+1,right)

        root.total = root.left.total + root.right.total
        return root

    def update(self,root,i,value):
        if root is None:
            return 0

        # Base Case (Leaf Node)
        if root.start == root.end:
            root.total = value
            return root.val

        mid = (root.start + root.end)//2
        if i <= mid:
            self.update(root.left,i,value)
        else:
            self.update(root.right,i,value)

        leftval = 0
        rightval = 0
        if root.left is not None:
            leftval = root.left.total
        if root.right is not None:
            rightval = root.right.total

        # Propagate changes to parent nodes
        root.total = leftval + rightval
        return root.total

    def sumrange(self,root,start,end):
        if root is None:
            return -1

        if start == root.start and end == root.end:
            return root.total

        mid = (root.start + root.end)//2
        if end <= mid:
            return self.sumrange(root.left,start,end)
        elif end >= mid+1:
            return self.sumrange(root.right,start,end)
        else:
            # Interval is split in both left and right subtree
            return self.sumrange(root.left,start,mid) + self.sumrange(root.right,mid+1,end)