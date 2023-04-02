# def f(grants, newbudget):
#     n = len(grants)
#     grants.sort()
#     sum = 0
#     for i in range(n):
#         cap = (newbudget-sum)/(n-i)
#         if grants[i] >= cap:
#             return cap
#         sum += grants[i]

# grants = [2,100,50,120,1000]
# newbudget = 190
# print(f(grants, newbudget))

# def f(price):
#     n = len(price)
#     profit = [[0 for j in range(n)] for i in range(n)]

#     for i in range(n):
#         profit[i][i] = price[i]
    
#     for i in range(n-1):
#         profit[i][i+1] = max(price[i] + 2*price[i+1], 2*price[i] + price[i+1])
    
#     print(profit)
    
#     for gap in range(3,n+1):
#         for start in range(n-gap+1):
#             end = start + gap - 1
#             len1 = end-start
#             len2 = len1+1
#             print(start,end,len1,len2)
#             profit[start][end] = profit[start+1][end-1] + max(len1*price[start] + len2*price[end], len2*price[start] + len1*price[end])
#     print(profit)
#     return profit[0][n-1]

# price = [2,4,6,2,5]
# print(f(price))

def f(num):
    x = pow(2,5)
    print(x)
    i = 0
    while (num & x) == 0:
        x = x >> 1
        i += 1
        print(x)
    return i

bs = '000101'
print(f(int(bs,2)))