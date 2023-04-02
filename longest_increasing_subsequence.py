def lis(nums):
    sub = []

    def bin_search(sub,num):
        low = 0
        high = len(sub)-1
        while low <= high:
            mid = low + (high-low)//2
            if sub[mid] == num:
                return mid
            elif sub[mid] > num:
                if mid == 0:
                    return 0
                if sub[mid-1] < num:
                    return mid
                else:
                    high = mid - 1
            else:
                low = mid + 1
        return low

    for num in nums:
        if not len(sub):
            sub.append(num)
        else:
            if num > sub[-1]:
                sub.append(num)
            else:
                i = bin_search(sub,num)
                sub[i] = num
    return len(sub)