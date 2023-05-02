from threading import Condition

class BoundedBlockingQueue(object):

    def __init__(self, capacity: int):
        self.queue = [None for i in range(capacity)]
        self.capacity = capacity
        self.head = 0
        self.tail = 0
        self.qsize = 0
        self.condition = Condition()

    def enqueue(self, element: int) -> None:
        # with self.lock is equivalent to acquiring a lock at start of with block 
        # and releasing it at the end of with block
        with self.condition:
            while self.qsize >= self.capacity:
                self.condition.wait()

            if self.tail == self.capacity:
                self.tail = 0
            self.queue[self.tail] = element
            self.tail += 1
            self.qsize += 1
            self.condition.notify_all()


    def dequeue(self) -> int:
       with self.condition:
            while self.qsize == 0:
               self.condition.wait()

            if self.head == self.capacity:
                self.head = 0
            ans = self.queue[self.head]
            self.head += 1
            self.qsize -= 1
            self.condition.notify_all()
            return ans

    def size(self):
        return self.qsize

