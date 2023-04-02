import heapq

li = []
heapq.heapify(li)
heapq.heappush(li,3)
heapq.heappush(li,1)
heapq.heappush(li,2)
print(heapq.heappop(li))
print(heapq.heappop(li))
print(heapq.heappop(li))
try:
    heapq.heappop(li)
except:
    print("no")
