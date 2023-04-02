def get_lps(s):
    n = len(s)
    length = 0
    lps = [0 for i in range(n)]
    lps[0] = 1

    i = 1
    while i < n:
        if s[i] == s[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length == 0:
                i += 1
            else:
                length = lps[length - 1]
    return lps


s = 'ababab'
print(s)
print(get_lps(s))