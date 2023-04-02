# def f(terrains, crowns):
#     nr = len(terrains)
#     nc = len(terrains[0])
#     direction = [[0,1],[1,0],[0,-1],[-1,0]]
#     visited = set()
#     result = 0

#     def dfs(r,c,letter):
#         nonlocal visited
#         visited.add((r,c))
#         curr_size = 1
#         curr_sum = crowns[r][c]

#         for d in direction:
#             cr = r + d[0]
#             cc = c + d[1]
#             if cr>=0 and cr<nr and cc>=0 and cc<nc and (cr,cc) not in visited and terrains[cr][cc]==letter:
#                 [new_size, new_sum] = dfs(cr,cc,letter)
#                 curr_size += new_size
#                 curr_sum += new_sum
        
#         return [curr_size, curr_sum]

    

#     for r in range(nr):
#         for c in range(nc):
#             if (r,c) not in visited:
#                 [curr_size, curr_sum] = dfs(r,c,terrains[r][c])
#                 result += curr_size*curr_sum
    
#     return result

# terrains = [['S','S','S','L','L'],
#             ['S','W','W','W','L'],
#             ['L','W','K','W','L'],
#             ['F','W','W','F','F'],
#             ['F','F','F','F','L']]

# crowns = [[0,0,0,0,0],
#           [1,0,1,1,0],
#           [1,0,0,0,1],
#           [0,0,0,1,0,],
#           [0,0,1,1,0,]]

# print(f(terrains,crowns))

# d = {}
# a = (1,3)
# d[a] = 1
# print(d[(1,3)])

# def f(tileColors, size):
#     def check(arr):
#         for i in range(1,size):
#             if arr[i] == arr[i-1]:
#                 return False
#         return True

#     n = len(tileColors)
#     count = 0
#     for i in range(n-size+1):
#         if check(tileColors[i:i+size]):
#             count += 1
    
#     for i in range(size-1,0,-1):
#         arr = tileColors[-i:] + tileColors[:size-i]
#         if check(arr):
#             count += 1

#     return count

# tileColors = [0,1,0,1,0,1]
# size = 3
# print(f(tileColors,size))

# def f(matrix):
#     nr = len(matrix)
#     nc = len(matrix[0])

#     def valid(r,c):
#         if 0 <= r < nr and 0 <= c < nc:
#             return True
#         return False

#     def getLength(r,c):
#         length = 1
#         count = 1
#         while True:
#             for cr,cc in [[r-count,c-count],[r-count,c+count],[r+count,c+count],[r+count,c-count]]:
#                 if not valid(cr,cc):
#                     return length
#                 if matrix[cr][cc] == 0:
#                     return length
#             length += 1
#             count += 1
#         return length

#     maxLength = 0
#     arr = []
#     for r in range(nr):
#         for c in range(nc):
#             if matrix[r][c] == 1:
#                 length = getLength(r,c)
#                 if length == maxLength:
#                     arr.append([r,c])
#                 elif length > maxLength:
#                     maxLength = length
#                     arr = [[r,c]]
#     arr.sort()
#     return arr[0]

# matrix = [
#     [1,0,1,0,0,0,1],
#     [0,1,0,1,0,1,0],
#     [1,0,1,0,1,0,1],
#     [0,1,0,1,0,1,0],
#     [1,0,1,0,0,0,1]
# ]
# print(f(matrix))

# from collections import Counter
# def f(a,b,queries):
#     result = []
#     da = Counter(a)
#     db = Counter(b)

#     def getcount(x):
#         count = 0
#         if len(da) < len(db):
#             for k in da:
#                 if x-k in db:
#                     count += da[k]*db[x-k]
#         else:
#             for k in db:
#                 if x-k in da:
#                     count += db[k]*da[x-k]
#         return count

#     for q in queries:
#         if len(q) == 3:
#             _,i,x = q

#             key = b[i]
#             val = db[b[i]]

#             b[i] += x
#             del db[key]

#             if b[i] in db:
#                 db[b[i]] += val
#             else:
#                 db[b[i]] = val
#         else:
#             _,x = q
#             result.append(getcount(x))
#     return result

# a = [1,2,3]
# b = [1,4]
# queries = [[1,5],[0,0,2],[1,5]]
# print(f(a,b,queries))

# def f(arr, target):
#     n = len(target)
#     m = pow(10,9) + 7
#     nw = len(arr[0])

#     memo = {}

#     def find(ti, j):
#         count = 0
#         if ti >= n:
#             return 1
#         if j >= nw:
#             return 0

#         for word in arr:
#             for i in range(j, nw):
#                 if word[i] == target[ti]:
#                     if (i+1, ti+1) not in memo:
#                         memo[(i+1, ti+1)] = find(i+1, ti+1)
#                     count += memo[(i+1, ti+1)]
#         # memo[(t)]
#         return count%m

#     return find(0,0)

# arr = ['adc','efg']
# target = 'ac'
# print(f(arr, target))

# from math import ceil
# def f(n,initialEnergy, th):
#     return ceil((sum(initialEnergy) - th)/len(initialEnergy))


# def f(initialEnergy, th):
#     ans = 0

#     def check(barrier):
#         total = 0
#         for e in initialEnergy:
#             total += max(0, e-barrier)
#         if total >= th:
#             return True
#         return False

#     low = 0
#     high = max(initialEnergy)
#     while low <= high:
#         mid = low + (high-low)//2
#         if check(mid):
#             ans = mid
#             low = mid + 1
#         else:
#             high = mid - 1
#     return ans

# # initialEnergy = [4,8,7,1,2]
# # n = 5
# # th = 9
# initialEnergy = [5,2,13,10]
# n = 5
# th = 8
# print(f(initialEnergy,th))

# def f(num):
#     binary = bin(num)
#     s = ''
#     for i in range(2,len(binary)):
#         s += str(1 - int(binary[i]))
    
#     return int(s,2)

# print(f(50))

# def func(threshold,points):
    
#     def f(i,count,minval,maxval):
#         if maxval-minval >= threshold:
#             return count
#         if i >= len(points):
#             return float('inf')
        
#         minval = min(minval, points[i])
#         maxval = max(maxval, points[i])

#         return min(f(i+1,count+1,minval,maxval), f(i+2,count+1,minval,maxval))
    
#     return f(0,0,float('inf'),-float('inf'))

# threshold = 402
# points = [25,162,206,224,264,288,334,364,367,389,405,454,478,479,482,509,517,545,578,626,657,692,705,720,734,747]
# print(func(threshold,points))

# def f(matrix):
#     shapes = {}
#     for i in range(len(matrix)):
#         for j in range(len(matrix[0])):
#             if matrix[i][j] == 0:
#                 count = 0
#                 valid = True

#                 while valid:
#                     count += 1
#                     for ci,cj in [[i-count,j-count], [i-count,j+count], [i+count,j-count], [i+count,j+count]]:
#                         if ci < 0 or ci >= len(matrix) or cj < 0 or cj > len(matrix[0]):
#                             valid = False
#                             break
                
#                 if count not in shapes:
#                     shapes[count] = []
#                 shapes[count].append([i,j])

#     arr = list(shapes.items())
#     arr.sort(reverse = True)

#     temp = arr[0][1]
#     temp.sort()
#     return temp[0]

# matrix = [
#     [1,0,1],
#     [0,1,0],
#     [1,0,1]
#     ]
# matrix = [[1]]
# print(f(matrix))

# def func(arr):
#     def f(arr):
#         count = 0
#         for i in range(1,len(arr)):
#             if arr[i] <= arr[i-1]:
#                 count += arr[i-1]+1 - arr[i]
#                 arr[i] = arr[i-1] + 1
#             else:
#                 count += (arr[i]-1 - arr[i-1])*i
#         return count

#     count = f(arr)
#     temp = []
#     for i in range(len(arr)-1,-1,-1):
#         temp.append(arr[i])
    
#     count = min(count, f(temp))
#     return count

# arr = [1,4,3,2]
# print(func(arr))


# [
#     [71,44,11,51],
#     [81,53,24,82],
#     [95,61,31,12],
#     [76,34,88,34]
# ]



# [
#     [7, 4, 1], 
#     [8, 5, 2], 
#     [9, 6, 3]]

# [
#     [7,8,9],
#     [4,5,6],
#     [1,2,3]
# ]

# [
#     [7,8,9],
#     [4,5,6],
#     [1,2,3]
# ]

# def f(a, q):
#     n = len(a)

#     def rotate(a):
#         m = [[-1 for j in range(n)] for i in range(n)]
#         r = 0
#         c = 0

#         for j in range(n):
#             for i in range(n-1,-1,-1):
#                 m[r][c] = a[i][j]
#                 c += 1
#                 if c == n:
#                     r += 1
#                     c = 0
#         return m
    
#     def maindiag(a):
#         def func(a,k):
#             r1, c1 = k, 0
#             r2, c2 = 0, k

#             while r1 > r2:
#                 a[r1][c1], a[r2][c2] = a[r2][c2], a[r1][c1]
#                 r1 -= 1
#                 c1 += 1
#                 r2 += 1
#                 c2 -= 1
#             return a
        
#         def func2(a,k):
#             r1, c1 = n-1, k
#             r2, c2 = k, n-1

#             while r1 > r2:
#                 a[r1][c1], a[r2][c2] = a[r2][c2], a[r1][c1]
#                 r1 -= 1
#                 c1 += 1
#                 r2 += 1
#                 c2 -= 1
#             return a


#         for k in range(n):
#             a = func(a,k)
        
#         for k in range(1,n):
#             a = func2(a,k)
        
#         return a

#     def antidiag(a):
#         def func(a,k):
#             r1, c1 = 0, n-k-1
#             r2, c2 = k, n-1

#             while r1 < r2:
#                 a[r1][c1], a[r2][c2] = a[r2][c2], a[r1][c1]
#                 r1 += 1
#                 c1 += 1
#                 r2 -= 1
#                 c2 -= 1
#             return a
        
#         def func2(a,k):
#             r1, c1 = k, 0
#             r2, c2 = n-1, n-k-1

#             while r1 < r2:
#                 a[r1][c1], a[r2][c2] = a[r2][c2], a[r1][c1]
#                 r1 += 1
#                 c1 += 1
#                 r2 -= 1
#                 c2 -= 1
#             return a
            
#         for k in range(n):
#             a = func(a,k)
        
#         for k in range(1,n):
#             a = func2(a,k)
        
#         return a

#     for x in q:
#         if x == 0:
#             a = rotate(a)
#         elif x == 1:
#             a = maindiag(a)
#         else:
#             a = antidiag(a)
    
#     return a

# a = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]
# q = [0,1,2]

# a = [
#     [11,2,9,1],
#     [17,4,0,32],
#     [1,7,10,6],
#     [80,3,5,14]
# ]
# q = [0,1,2,0]

# [
#     [80, 1, 17, 11], 
#     [3, 7, 4, 2], 
#     [5, 10, 0, 9], 
#     [14, 6, 32, 1]
# ]

# [
#     [80, 3, 5, 14], 
#     [1, 7, 10, 32], 
#     [17, 4, 0, 6], 
#     [11, 9, 2, 1]
# ]

# a = [
#     [42,42,54,11,80],
#     [66,62,51,10,26],
#     [73,31,4,25,12],
#     [10,24,32,88,97],
#     [36,39,88,32,20]
# ]

# q = [2,0,1,2,0,1,0,1,0,2,1,0,2,1,0]

# print(f(a,q))

# def f(nums, k):
#     n = len(nums)
#     prefix = [nums[0]]
#     for i in range(1,n):
#         prefix.append(prefix[-1] + nums[i])
    
#     def check(start,end):
#         sum = prefix[end]
#         if start > 0:
#             sum -= prefix[start-1]

#         return sum%k == 0

#     count = 0
#     for start in range(n):
#         for end in range(start,n):
#             if check(start,end):
#                 count += 1
#     return count

# nums = [5,10,11,9,5]
# k = 5
# print(f(nums, k))

# def f(bags):
#     maxcount = 0
#     n = len(bags)
#     s = set(bags)

#     def getCount(start):
#         count = 0
#         curr = start

#         while curr in s:
#             count += 1
#             curr *= curr
#         return count

#     for i in range(n):
#         count = getCount(bags[i])
#         maxcount = max(maxcount, count)
    
#     if maxcount < 2:
#         return -1
#     return maxcount

# bags = [4,2,16]
# print(f(bags))


# def f(boot, process, powermax):
#     n = len(boot)
#     prefix = [0]
#     for i in range(n):
#         prefix.append(prefix[-1] + process[i])

#     def check(k):
#         for start in range(0,n-k+1):
#             sum = prefix[start+k] - prefix[start]
#             maxval = max(boot[start: start+k])

#             if maxval + sum*k <= powermax:
#                 return True
#         return False
#     for k in range(n,0,-1):
#         if check(k):
#             return k

# process = [4,1,4,5,3]
# boot = [8,8,10,9,12]
# powermax = 33

# print(f(boot,process,powermax))

# from collections import Counter
# def f(xCoordinate, yCoordinate):
#     maxX = 0
#     maxY = 0

# xCoords = [1,2,2,3]
# yCoords = [2,3,4,5]
# print(f(xCoords,yCoords))

# def f(inputArr):
#     maxChoc = 0
#     n = len(inputArr)

#     def func(i,choc,canPick):
#         nonlocal maxChoc
#         maxChoc = max(maxChoc, choc)

#         if canPick:
#             func(i+1)


#     return max(func(0,0,True), func(0,0,False))


# def f(p, cost, distance):
#     minCost = float('inf')
#     if p < 10:
#         return "NOT POSSIBLE"
    
#     n = len(cost)
    
#     def func(i, remaining, currCost):
#         if i == n:
#             minCost = min(minCost, currCost)
#             return
        
#         if remaining >= 10:
#             func(i+1, remaining-10, currCost)
        
#         if distance[i] >= 10:
#             func(i+1, distance[i]-10, currCost+cost[i])
            
#     func(0,p-10,0)

#     if minCost == float('inf'):
#         return "NOT POSSIBLE"
#     return minCost

# from collections import Counter
# def f(a,b,queries):
#     result = []
#     da = Counter(a)
#     db = Counter(b)
#     print(da,db)
#     for q in queries:
#         if q[0] == 0:
#             i = q[1]
#             x = q[2]
#             da[a[i]] = max(da[a[i]]-1,0)
#             a[i] = x
#             if x not in da:
#                 da[x] = 0
#             da[x] += 1
#         else:
#             x = q[1]
#             pairs = 0
#             for num in db:
#                 if x-num in da:
#                     pairs += da[x-num]*db[num]
#             result.append(pairs)
#         print(da,a,result)
#     return result

# def f(matrix):
#     nr = len(matrix)
#     nc = len(matrix[0])

#     def getCol(r,c):
#         ans = c
#         for col in range(c+1,nc):
#             if matrix[r][col] == '.':
#                 ans = col
#             else:
#                 return ans
#         return ans
    
#     def getRow(r,c):
#         ans = r
#         for row in range(r+1,nr):
#             if matrix[row][c] == '.':
#                 ans = row
#             else:
#                 return ans
#         return ans

#     for r in range(nr):
#         for c in range(nc-2,-1,-1):
#             col = getCol(r,c)
#             print(col)
#             if col != c:
#                 matrix[r][col] = '#'
#                 matrix[r][c] = '.'

#     for c in range(nc):
#         for r in range(nr-2,-1,-1):
#             row = getRow(r,c)
#             if row != r:
#                 matrix[row][c] = '#'
#                 matrix[r][c] = '.'
#     return matrix

# matrix = [
#     ['.','#','.','.','.'],
#     ['.','.','.','.','.'],
#     ['#','.','#','#','.'],
#     ['#','.','.','.','#']
# ]
# print(f(matrix))

# a = [2,3]
# b = [1,2,2]
# q = [[1,4],[0,0,3],[1,5]]
# print(f(a,b,q))

# def f(arr):
#     count = 0
#     n = len(arr)
#     st = []

#     for i in range(n):
#         if (len(st) == 0 or st[-1] != arr[i]):
#             st.append(arr[i])
             
#         else:
#             count += 1
#             st.pop()
 
#     # Check who has won
#     if (count % 2 == 0):
#         print("Bob")
     
#     else :
#         print("Alice")

# arr = [1,2,2,3,3,1,1]
# print(f(arr))

# def f(panel, codes):
#     result = []
    
#     def check(index, pattern):
#         if index < len(panel):
#             if panel[index: index+len(pattern)] == pattern:
#                 return pattern
#         return "not found"

#     for code in codes:
#         for i in range(1,len(code)):
#             index = code[:i]
#             pattern = code[i:]
#             result.append(check(int(index), pattern))
#     return result

# panel = "2311453915"
# codes = ["0211", "639"]

# print(f(panel, codes))

# def f(text, width):
#     chars = []
#     for c in text:
#         if c in ['.', '?', '!']:
#             chars.append(c)
#     ci = 0
#     print(chars)

#     text = text.replace('.', ";")
#     text = text.replace('!', ";")
#     text = text.replace('?', ";")
#     arr = text.split(";")[:-1]
#     result = []

#     # print(text)

#     def process(sentence):
#         nonlocal ci
#         curr = ["  "]
#         sentence += ';'
#         words = sentence.split(" ")
#         # print(words)
#         available = width - 2

#         i = 0
#         while i < len(words):
#             word = words[i]
#             if available >= len(word):
#                 if ';' in word:
#                     word = word.replace(';', chars[ci])
#                     ci += 1
#                 curr.append(word)
#                 available -= (len(word)+1)
#                 i += 1
#             else:
#                 available = width
#                 result.append(curr[::])
#                 curr = []
#         result.append(curr[::])

#     for sentence in arr:
#         process(sentence)
        
#     final = []
#     s = '*'*width
#     final.append(s)
#     for sentence in result:
#         cs = " ".join(sentence)
#         cs += " "*(width-len(cs))
#         cs = '*' + cs + '*'
#         final.append(cs)
#     final.append(s)

#     return final


# text = "Hi! This is the article you have to format properly. Could you do that for me, please?"
# print(f(text, 16))


def solution(vulnerability):
    n = len(vulnerability)
    m = len(vulnerability[0])
    maxVulnerability = -float('inf')

    def getVul(rows):
        arr = vulnerability[rows[0]][::]
        for i in range(1, m-1):
            r = rows[i]
            for c in range(m):
                arr[c] = max(arr[c], vulnerability[r][c])
        return min(arr)

    def f(index, rows):
        nonlocal maxVulnerability

        if len(rows) == m-1:
            vul = getVul(rows)
            maxVulnerability = max(maxVulnerability, vul)
            return
        if len(rows) > m-1:
            return
        
        for i in range(index+1, n):
            f(i, rows)
            f(i, rows+[i])
    
    f(0, [])
    f(0, [0])
    return maxVulnerability

vulnerability = [
    [1,3,1],
    [3,1,1],
    [1,2,2],
    [1,1,3]
]

vulnerability = [
    [2,6,6],
    [8,10,9],
    [1,9,1],
    [10,3,2],
    [8,3,4]
]

vulnerability = [
    [5,1,3],
    [5,2,1],
    [3,2,1]
]

print(solution(vulnerability))