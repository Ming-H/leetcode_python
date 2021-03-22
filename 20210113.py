def bubble_sort(nums):
    for i in range(len(nums)-1):
        for j in range(len(nums)-1-i):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    return nums
    
def insert_sort(nums):
    for i in range(1, len(nums)):
        tmp = nums[i]
        j = i-1
        while j>=0 and nums[j]>tmp:
            nums[j+1] = nums[j]
            j -= 1
        nums[j+1] = tmp
    return nums
    
def partition(nums, low, high):
    pivot = nums[low]
    while low<high:
        while low<high and nums[high]>pivot:
            high -= 1
        while low<high and nums[low]<pivot:
            low += 1
        nums[low], nums[high] = nums[high], nums[low]
    nums[low] = pivot
    return low
    
def quick_sort(nums, low, high):
    if low < high:
        index = partition(nums, low, high)
        quick_sort(nums, low, index-1)
        quick_sort(nums, index+1, high)
    return nums
    
def merge(a, b):
    L = []
    i, j = 0, 0
    while i<len(a) and i<len(b):
        if a[i]<b[j]:
            L.append(a[i])
            i += 1
        else:
            L.append(b[j])
            j += 1
    if len(a) == i:
        L.extend(b[j:])
    else:
        L.extend(a[i:])
    return L
          
def merge_sort(nums):
    if len(nums)<=1:
        return nums
    middle = len(nums)//2
    left = merge_sort(nums[:middle])
    right = merge_sort(nums[middle:])
    return merge(left, right)
    
def heapify(nums, i, n):
    l = 2*i+1
    while l<n:
        if l+1<n and nums[l+1]>nums[l]:
            l += 1
        if nums[i] > nums[l]:
            break
        nums[i], nums[l] = nums[l], nums[i]
        i, l = l, 2*l+1
    
def heap_sort(nums):
    n = len(nums)
    for i in range(n-1, -1, -1):
        heapify(nums, i, n)
    for i in range(n-1, 0, -1):
        nums[i], nums[0] = nums[0], nums[i]
        heapify(num, 0, i)
    
def twoSum(nums, target):
    d = {}
    for i, item in enumerate(nums):
        if item not in d:
            d[target-item] = i
        else:
            return d[item], i
    return -1, -1
    
def addTwoNumber(l1, l2):
    carry = 0
    root = n = ListNode(0)
    while l1 or l2 or carry:
        v1 = v2 = 0
        if l1:
            v1 = l1.val
            l1 = l1.next
        if l2:
            v2 = l2.val
            l2 = l2.next
        carry, val = divmod(v1+v2+carry, 10)
        n.next = ListNode[val]
        n = n.next
    return root.next
    
def lengthoflongestSubstring(s):
    start = maxlen = 0
    d = {}
    for i, item in enumerate(s):
        if item in d and d[item]>=start:
            start = d[item]+1
        else:
            maxlen = max(maxlen, i-start+1)
        d[item] = i
    return maxlen
    
def findMedianSortedArrays(A,B):
    m, n = len(A), len(B)
    if m>n:
        A, B, m, n = B, A, n, m
    if n == 0:
        raise ValueError
    imin, imax = 0, m
    while imin <= imax:
        i = (imin+imax)//2
        j = (m+n+1)//2 + 1
        if i<m and B[j-1]>A[i]:
            imin = i + 1
        elif i>0 and A[i-1]>B[j]:
            imax = i - 1
        else:
            if i==0:
                max_of_left = B[j-1]
            elif j==0:
                max_of_right = A[i-1]
            else:
                max_of_left = max(A[i-1], B[j-1])
            if (m+n)%2==1:
                return max_of_left
            if i==m:
                min_of_right = B[j]
            elif j==n:
                min_of_right = A[i]
            else:
                min_of_right = min(A[i], B[j])
            return (max_of_left + min_of_right)/2.0
                
def longestPalindrome(s):
    if len(s)<1:
        return ""
    def expand(s, l, r):
        while l>=0 and r<len(s) and s[l]==s[r]:
            l -= 1
            r += 1
        return r-l+1
    start, end = 0, 0
    for i in range(len(s)):
        len1 = expand(s, i, i)
        len2 = expand(s, i, i+1)
        len_max = max(len1, len2)
        if len_max > end-start:
            start = i - (len_max-1)//2
            end = i + len_max//2
    return s[start: end]
    
def reverse(x):
    if x<0:
        ss = 0 - int(''.join([item for item in str(x)[1:]][::-1]))
        if ss < -2**(31):
            return 0
        else:
            return ss
    else:
        ss = int(''.join([item for item in str(x)][::-1]))
        if ss > 2**31:
            return 0
        else:
            return ss
            
def myAtoi(str):
    str = str.strip()
    flag = 1
    res = 0
    i = 0
    num = '0123456789'
    if not str or len(str)==0:
        return 0
    if str[0] == '-':
        flag = -1
        i += 1
    elif str[0] == '+':
        i += 1
    while i<len(str):
        if str[i] in num:
            res = res * 10 + int(str[i])
        else:
            break
        i += 1
    if flag * res > 2**31:
        return 2**31
    elif flag * res < -2**31:
        return -2**31
    else:
        return flag * res
        
def isPalindrome(x):
    if x<0:
        return False
    x_copy = x
    tmp = 0
    while x>0:
        tmp *= 10
        tmp += x%10
        x = x//10
    if tmp == copy:
        return True
    else:
        return False
        
def maxArea(nums):
    maxarea = 0
    l, r = 0, len(nums)-1
    while l<=r:
        maxarea = max(maxarea, min(nums[l], nums[r])*(r-l))
        if nums[l] < nums[r]:
            l += 1
        else:
            r -= 1
    return maxarea
    
def longestCommonPrefix(strs):
    if len(strs) == 0:
        return ""
    str0 = strs[0]
    Min = len(str0)
    for i in range(1, len(strs)):
        j = 0
        while j<Min and j<len(strs[i]) and strs[i][j]==str0[j]:
            j += 1
        Min = min(Min, j)
    return str0[:Min]
    
def threeSum(nums):
    res = []
    nums.sort()
    for i in range(len(nums)-2):
        if i>0 and nums[i]==nums[i-1]:
            continue
        l, r = i+1, len(nums)-1
        while l<r:
            s = nums[i] + nums[l] + nums[r]
            if s<0:
                l += 1
            elif s>0:
                r -= 1
            else:
                res.append((nums[i], nums[l], nums[r]))
                while l<r and nums[l]==nums[l+1]:
                    l += 1
                while l<r and nums[r]==nums[r-1]:
                    r -= 1
                l += 1
                r --= 1
    return res
             
def threeSumCloest(nums, target):
    nums.sort()
    res = nums[0] + nums[1] + nums[2]
    for i in range(len(nums)-2):
        j, k = i+1, len(nums)-1
        while j<k:
            cur_sum = nums[i] + nums[j] + nums[k]
            if cur_sum == target:
                return cur_sum
            if abs(cur_sum-target) < abs(res-target):
                res = cur_sum
            if cur_sum < res:
                l += 1
            elif cur_sum > res:
                r -= 1
    return res
    
def foursum(nums, target):
    nums.sort()
    res = []
    findNsum(nums, target, 4, [], res)
    return res54
    
def findNsum(nums, target, N, path, res):
    if len(nums) < N or N<2:
        return
    if N == 2:
        l, r = 0, len(nums)-1
        while l<r:
            if nums[l] + nums[r] == target:
                res.append(path+[nums[l], nums[r]])
                while l<r and nums[l]==nums[l+1]:
                    l += 1
                while l<r and nums[r]==nums[r-1]:
                    r -= 1
                l += 1
                r -= 1
            elif nums[l] + nums[r] < target:
                l += 1
            else:
                r -= 1
    else:
        for i in range(0, len(nums)-N+1):
            if target < nums[i]*N or target >nums[-1]*N:
                break
            if i==0 or i>0 and nums[i-1]!=nums[i]:
                findNsum(nums[i+1:],
                    target-nums[i], N-1, path+[nums[i]], res)
    return
    
def removeNthFromEnd(head, n):
    fast = slow = head
    for _ in range(n):
        fast = fast.next
    if not fast:
        return head.next
    while fast.next:
        fast = fast.next
        slow = slow.next
    slow.next = slow.next.next
    return head
    
def generateparenthesis(n):
    res = []
    def generate(A='', left=0, right=0):
        if len(A) == 2*n:
            res.append("".join(A))
            return
        if left < n:
            generate(A+'(', left+1, right)
        if right<left:
            generate(A+')', left right+1)
    generate()
    return res
        
def swapPairs(head):
    pre, pre.next = self, head
    while pre.next and pre.next.next:
        a, b = pre.next, pre.next.next
        pre.next, b.next, a.next = b, a, b.next
    return self.next
    
def search(nums, target):
    l, r = 0, len(nums)-1
    while l<=r:
        mid = (l+r)//2
        if nums[mid] == target:
            return mid
        if nums[l] <= nums[mid]:
            if nums[l] <= target <= nums[mid]:
                r = mid - 1
            else:
                l = mid + 1
        else:
            if nums[mid] <= target <= nums[r]:
                l = mid + 1
            else:
                r = mid - 1
    return -1
    
def extreme_insertion_index(nums, target, flag):
    l, r = 0, len(nums)
    while l<r:
        mid = (l+r)//2
        if nums[mid] > target or (flag and nums[mid]==target):
            r = mid
        else:
            l = mid + 1
    return l
def search(nums, target):
    left = extreme_insertion_index(nums, target, True)
    if left == len(nums) or nums[left] != target:
        reurn [-1, -1]
    return [left, extreme_insertion_index(nums, target, False)]
    
def combinationSum(nums, target):
    res = []
    nums.sort()
    dfs(nums, target, 0, [], res)
    return res
def dfs(nums, target, index, path, res):
    if target<0:
        return
    if target==0:
        res.append(path)
        return
    for i in range(index, len(nums)):
        dfs(nums, target-nums[i], i, path+[nums[i]], res)
        
def combinationSum(nums, target):
    nums.sort()
    res = []
    dfs(nums, target, 0, [], res)
    return res
def dfs(nums, target, index, path, res):
    if target<0:
        return
    if target==0:
        res.append(path)
        return
    for i in range(index, len(nums)):
        if i>index and nums[i]==nums[i-1]:
            continue
        dfs(nums, target-nums[i], i+1, path+[nums[i]], res)
    
def permute(nums):
    res = []
    dfs(nums, [], res)
    return res
def dfs(nums, path, res):
    if not nums:
        res.append(path)
    for i in range(len(nums)):
        dfs(nums[:i]+nums[i+1:], path+nums[i], res)

def permute(nums):
    res = []
    nums.sort()
    dfs(nums, None, [], res)
    return res
def dfs(nums, pre, path, res):
    if len(nums)==0:
        res.append(list(path))
    pre = None
    for i in range(len(nums)):
        if nums[i]==pre:
            continue
        path.append(nums[i])
        dfs(nums[:i]+nums[i+1:], nums[i], path, res)
        path.pop()
        pre = nums[i]
    
def premute(nums):
    res = []
    nums.sort()
    dfs(nums, None, [], res)
    return res
def dfs(nums,pre, path, res):
    if len(nums)==0:
        res.append(list(path))
    pre = None
    for i in range(len(nums)):
        if nums[i]==pre:
            continue
        path.append(nums[i])
        dfs(nums[:i]+nums[i+1:], nums[i], path, res)
        path.pop()
        pre = nums[i]
        
def rotate(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(i):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for row in matrix:
        row = row[::-1]


















    
    
