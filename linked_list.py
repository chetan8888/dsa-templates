# Reverse a list

def reverseList(self, head):
    last = None
    while head:
        # keep the next node
        tmp = head.next
        # reverse the link
        head.next = last
        # update the last node and the current node
        last = head
        head = tmp
    
    return last