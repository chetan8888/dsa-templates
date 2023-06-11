# to build a monotonously increasing/decreasing array, use stack

# from itertools import accumulate
# a = [4,7,3]
# print(list(accumulate(a)))
# print(list(accumulate(a, min)))
# print(list(accumulate(a, max)))

# curr.next, curr, prev = prev, curr.next, curr for reversing a linked list

# from collections import Counter
# a = [10,10,30,40,50,60,70]
# freq = dict(Counter(a))

# Think about sliding window, stack, queues for questions involving subarrays

# For Linked List questions, think about reversing the list or part of the list to solve it in constant space complexity

# a = [3,5,7]
# b = [1,2]
# b.append(a) //append by reference
# b.append(a[:])  //append by value

# Whenever prefixes of strings are involved, it is usually a natural fit for a trie

# from bisect import bisect_left, bisect_right, insort
# a = [1,4,4,6,8,9]
# print(bisect_left(a,10))
# print(bisect_right(a,4))

# insort(a, 7)
# print(a)

# Use a dummy node in cases where starting point is None. This will remove few is None conditions

# Prime numbers upto a given number
# https://www.geeksforgeeks.org/sieve-of-eratosthenes/

# Store arr as key in dict
# dic[tuple(arr)] = value

# always use while not pq.empty() for PriorityQueue, while pq: will always be true

# For a 2d matrix, simply starting from the leftmost cell and traversing the right and down edges will cover all the edges. This is particulkarly useful when you need the model the matrix as an undirected graph.