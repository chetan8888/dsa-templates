# De Bruijn Sequence
# Given an integer n and a set of characters A of size k, find a minimum length string S such that every possible string on A of length n appears exactly once as a substring in S.
# For Theory and Algorithm: https://www.youtube.com/watch?v=VZvU1_oPjg0
# https://www.geeksforgeeks.org/de-bruijn-sequence-set-1/#
# Leetcode: https://leetcode.com/problems/cracking-the-safe/description/

def de_bruijn(n, k):
    totalStrings = k ** n
    deBruijnSequence = "0" * n
    visited = set()
    visited.add("0"*n)

    def dfs(currString, visited):
        nonlocal deBruijnSequence
        if len(visited) == totalStrings:
            return True
    
        for character in range(k):
            newString = currString[1:] + str(character)
            if newString not in visited:
                deBruijnSequence += str(character)
                visited.add(newString)
                if dfs(newString, visited):
                    return True
                deBruijnSequence = deBruijnSequence[:-1]
                visited.discard(newString)

        return False

    dfs("0" * n, visited)
    return deBruijnSequence

print(de_bruijn(2, 2))