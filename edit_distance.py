# Levenshtein Algorithm
# https://en.wikipedia.org/wiki/Levenshtein_distance
# lev(a,b) = |b| if |a| = 0
#            |a| if |b| = 0    
#            lev(a[1:],b[1:]) if a[0] = b[0]
#            1 + min(lev(a[1:],b), lev(a,b[1:]), lev(a[1:],b[1:])) otherwise


# Question : Edit Distance (https://leetcode.com/problems/edit-distance/description/)

# Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.

# You have the following three operations permitted on a word:

# Insert a character
# Delete a character
# Replace a character

# Note: To visualize the operations assume the insert and delete operations are always performed on the first string. This is because insert operation on one string is same as delete operation on the other string and vice versa. Replace operation is always performed on both the strings.

# Solution without cache
def minDistance(word1, word2):
    n1 = len(word1)
    n2 = len(word2)

    def recursiveFunc(index1,index2):
        # Base Case
        if index1 >= n1 and index2 >= n2:
            return 0

        # |a| = 0
        if index1 >= n1:
            return n2-index2
        # |b| = 0
        if index2 >= n2:
            return n1-index1
        
        if word1[index1] == word2[index2]:
            answer = recursiveFunc(index1+1,index2+1)
        else:
            # Insert a character
            answer = 1 + recursiveFunc(index1, index2+1)
            # Delete a character
            answer = min(answer, 1 + recursiveFunc(index1+1, index2))
            # Replace a character
            answer = min(answer, 1 + recursiveFunc(index1+1, index2+1))
        return answer
        
    return recursiveFunc(0,0)

word1 = "horse"
word2 = "ros"
print(minDistance(word1, word2))
# Output: 3


# Solution with cache
def minDistanceCache(word1, word2):
    n1 = len(word1)
    n2 = len(word2)

    cache = {}

    def recursiveFunc(index1,index2):
        nonlocal cache

        # To incorporate cache in any recursive function, simply create a key of all the parameters of that function. In python we can simply create a tuple of all the parameters and use it as a key.
        key = (index1, index2)
        if key in cache:
            return cache[key]

        if index1 >= n1 and index2 >= n2:
            return 0

        if index1 >= n1:
            return n2-index2
        if index2 >= n2:
            return n1-index1
        
        if word1[index1] == word2[index2]:
            answer = recursiveFunc(index1+1,index2+1)
        else:
            answer = 1 + recursiveFunc(index1, index2+1)
            answer = min(answer, 1 + recursiveFunc(index1+1, index2))
            answer = min(answer, 1 + recursiveFunc(index1+1, index2+1))

        cache[key] = answer

        return answer
    
    return recursiveFunc(0,0)

word1 = "horse"
word2 = "ros"
print(minDistanceCache(word1, word2))
# Output: 3