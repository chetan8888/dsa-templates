# from threading import Thread
# import random

# global value
# value = 1000

# def printer():
#     global value
#     while value > 0:
#         if value % 5 == 0:
#             print(value)
#         value -= 1

# def modifier():
#     global value
#     while value > 0:
#         value = random.randint(0, 1000)

# t1 = Thread(target=printer)
# t2 = Thread(target=modifier)

# t1.start()
# t2.start()

# t2.join()   
# t1.join()

import random
from threading import Thread

class RaceCondition:
    def __init__(self):
        self.randInt = 0
        self.random = random.Random()

    def printer(self):
        for i in range(1000000):
            if self.randInt % 5 == 0:
                if self.randInt % 5 == 0:
                    print(self.randInt)

    def modifier(self):
        for i in range(1000000):
            self.randInt = self.random.randint(0, 1000)

    def runTest(self):
        thread1 = Thread(target=self.printer)
        thread2 = Thread(target=self.modifier)

        thread1.start()
        thread2.start()

        thread1.join()
        thread2.join()

if __name__ == "__main__":
    raceCondition = RaceCondition()
    raceCondition.runTest()
