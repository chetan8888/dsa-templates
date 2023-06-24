# Given a text and pattern, find all occurrences of pattern in text.
# Time Complexity: O(n + m)

def kmp(text, pattern):
    n = len(text)
    m = len(pattern)
    index = []
    lps = [0 for i in range(m)]

    def computeLPS(pattern):
        length = 0
        i = 1
        while i < m:
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length == 0:
                    i += 1
                else:
                    length = lps[length-1]
    computeLPS(pattern)
    print(lps)

    i = 0
    j = 0
    while i < n:
        if text[i] == pattern[j]:
            i += 1
            j += 1
        if j == m:
            index.append(i-j)
            j = lps[m-1]
        elif i < n and text[i] != pattern[j]:
            if j == 0:
                i += 1
            else:
                j = lps[j-1]
    return index

# print(kmp("abcabababa", "aba"))
print(kmp("abca", "abcaba"))

