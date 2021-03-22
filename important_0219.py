def heapify(nums,i, n):
    l = 2*i+1
    while l<n:
        if l+1<n and nums[l+1]>nums[i]:
            l += 1
        if nums[i]>nums[l]:
            break
        nums[i], nums[l] = nums[l], nums[i]
        i, l = l, 2*l+1

def heapsort(nums):
    n = len(nums)
    for i in range(n-1, -1, -1):
        heapify(nums, i, n)
    for i in range(n-1, 0, -1):
        nums[i], nums[0] = nums[0], nums[i]
        heapify(nums, 0, i)

def twoSum(nums, target):
    d = {}
    for i, item in enumerate(nums):
        if item not in d:
            d[target-item] = i
        else:
            return d[item], i
    return -1, -1

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def addTwoNumbers(L1, L2):
    carry = 0
    root = n = ListNode(0)
    while L1 or L2 or carry:
        v1 = v2 = 0
        if l1:
            v1 = l1.val
            l1 = l1.next
        if l2:
            v2 = l2.val
            l2 = l2.next
        carry, val = divmod(v1+v2+carry, 10)
        n.next = ListNode(val)
    return root.next

def addTwoNumbers_(l1, l2):
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
        n.next = ListNode(val)
    return root.next

def lengthOfLongestSubstring(nums):
    start = maxlen = 0
    d = {}
    for i, item in enumerate(nums):
        if item in d and d[item]>=start:
            start = d[item] + 1
        else:
            maxlen = max(maxlen, i-start+1)
        d[item] = i
    return maxlen

def lengthOfLongestSubstring_(s):
    start = maxlen = 0
    d = {}
    for i, item in enumerate(s):
        if item in d and d[item]>=start:
            start = d[item]+1
        else:
            maxlen = max(maxlen, i-start+1)
        d[item] = i
    return maxlen

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
        if len_max>end-start:
            start = i-(len_max-1)//2
            end = i+len_max//2
    return s[start: end]

def longestPalindrome_(s):
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
        if len_max>end-start:
            start = i-(len_max-1)//2
            end = i+len_max//2
    return s[start: end]

def reverse(x):
    if x<0:
        ss = 0-int(''.join([item for item in str(x)][::-1]))
        if ss<-2**31:
            return 0
        else:
            return ss
    else:
        ss = int(''.join([item for item in str(x)][::-1]))
        if ss>2**31:
            return 0
        else:
            return ss

 def myAtoi(s):
    s = s.strip()
    flag = 1
    res = 0
    i = 0
    number = '0123456789'
    if not s or len(s)==0:
        return 0
    if s[0] == '-':
        flag = -1
        i += 1
    elif s[0] == '+':
        i += 1
    while i<len(s):
        if s[i] in number:
            res = res*10 + int(s[i])
        else:
            break
        i += 1
    if flag * res > 2**31:
        return 2**31
    if flag * res < -2**31:
        return -2**31
    return flag*res

def myAtoi_(s):
    s = s.trip()
    flag = 1
    res = 0
    i = 0
    number = '1234567890'
    if not s or len(s)==0:
        return 0
    if s[0]=='-':
        flag = -1
        i += 1
    elif s[0]=='+':
        i += 1
    while i < len(s):
        if s[i] in number:
            res = res*10 + int(s[i])
        else:
            break
        i += 1
    if flag * res > 2**31:
        return 2**31
    elif flag * res < -2**31:
        return -2**31
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
    if tmp == x_copy:
        return True
    else:
        return False

def isPalindrome_(x):
    if x<0:
        return False
    x_copy = x
    tmp = 0
    while x>0:
        tmp *= 10
        tmp += x%10
        x = x//10
    if tmp == x_copy:
        return True
    else:
        return False
    
def maxArea(nums):
    maxarea = 0
    l = 0
    r = len(nums)-1
    while l<=r:
        maxarea = max(maxarea, min(nums[l], nums[r]) * (r-l))
        if nums[l] < nums[r]:
            l += 1
        else:
            r -= 1
    return maxarea

def maxArea_(nums):
    maxarea = 0
    l, r = 0, len(nums)-1
    while l<=r:
        maxarea = max(maxarea, min(nums[l], nums[r])*(r-l))
        if nums[l] < nums[r]:
            l += 1
        else:
            r -= 1
    return maxarea

def longesetCommonPrefix(strs):
    if len(strs)==0:
        return ""
    str0 = strs[0]
    Min = len(str0)
    for i in range(1, len(strs)):
        j = 0
        while j<Min and j<len(strs[i]) and strs[i][j]==str0[j]:
            j += 1
        Min = min(Min, j)
    return str0[:Min]

def longestCommonPrefix_(strs):
    if len(strs)==0:
        return ""
    str0 = strs[0]
    Min = len(str0)
    for i in range(1, len(strs)):
        j = 0
        if j<len(str0) and j<len(str[i][j]) and strs[i][j]==str0[j]:
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
            s = nums[i]+nums[l]+nums[r]
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
                r -= 1
    return res

def threeSum(nums):
    res = []
    nums.sort()
    for i in range(len(nums)-2):
        if i>0 and nums[i]==nums[i-1]:
            continue
        l, r = i+1, len(nums)-1
        while l<r:
            s = nums[i] + nuns[l] + nums[r]
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
                r -= 1
    return res

def threeSum_(nums):
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
                res.append((nums[i]+nums[l]+nums[r]))
                while l<r and nums[l]==nums[l+1]:
                    l += 1
                while l<r and nums[r]==nums[r-1]:
                    r -= 1
                l += 1
                r -= 1
    return res

def threeSumClosest(nums, target):
    nums.sort()
    res = nums[0]+nums[1]+nums[2]
    for i in range(len(nums)-2):
        l, r = i+1, len(nums)-1
        while l<r:
            s = nums[i]+nums[l]+nums[r]
            if s==res:
                return res
            if abs(s-target) < abs(res-target):
                res = s
            if s < target:
                l += 1
            elif s > target:
                r -= 1
    return res

def threeSumClosest(nums, target):
    nums.sort()
    res = nums[0]+nums[1]+nums[2]
    for i in range(len(nums)-2):
        l, r = i+1, len(nums)-1
        while l<r:
            s = nums[i]+nums[l]+nums[r]
            if s == target:
                return s 
            if abs(s-target) < abs(res-target):
                res = s
            if res < target:
                l += 1
            elif res > target:
                r -= 1
    return res

def fourSum(nums, target):
    nums.sort()
    res = []
    findNSum(nums, target, 4, [], res)
    return res
def findNSum(nums, target, n, path, res):
    if len(nums)<n or n<2:
        return
    if n==2:
        l, r = 0, len(nums)-1
        while l<r:
            if nums[l]+nums[r]=target:
                res.append(path+[nums[l]+nums[r]])
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
        for i in range(len(nums)-n-1):
            if target<nums[i]*n or target>nums[-1]*n:
                break
            if i==0 or i>0 and nums[i-1]!=nums[i]:
                findNSum(nums[i+1:], target-nums[i], n-1, path+[nums[i]], res)
            
def fourSum(nums, target):
    nums.sort()
    res = []
    findNSum(nums, target, 4, [], res)
    return res

def findNSum(nums, target, n, path, res):
    if len(nums)<n or n<2:
        return
    if n==2:
        l, r = 0, len(nums)-1
        while l<r:
            if nums[l]+nums[r]==target:
                res.append(path+[nums[l]+nums[r]])
                while l<r and nums[l]==nums[l+1]:
                    l += 1
                while l<r and nums[r]==nums[r-1]:
                    r -= 1
                l += 1
                r -= 1
            elif nums[l]+nums[r]<target:
                l += 1
            else:
                r -= 1
    else:
        for i in range(len(nums)-n+1):
            if target<numns[i]*n or target>nums[-1]*n:
                break
            if i==0 or i>0 and nums[i-1]!=nums[i]:
                findNSum(nums[i+1:], target-nums[i], n-1, path+[nums[i]], res)
    return 

def removeNthFromEnd(head, n):
    fast = slow = head
    for i in range(n):
        fast = fast.next
    if not fast:
        return slow.next
    while fast.next:
        fast = fast.next
        slow = slow.next
    slow.next = slow.next.next
    return head

def removeNthNode_(head, n):
    fast = slow = head
    for i in range(n):
        fast = fast.next
    if not fast.next:
        return slow.next
    while fast.next:
        fast = fast.next
        slow = slow.next
    slow.next = slow.next.next
    return head

def isValid(s):
    stack = []
    d = {')':'(', ']':'[', '}':'{'}
    for item in s:
        if item in d:
            top_element = stack.pop() if stack else '#'
            if top_element != d[item]:
                return False
        else:
            stack.append(item)
    return not stack

def isValid_(s):
    stack = []
    d = {'}':'{', ']':'[', ')':'('}
    for item in s:
        if item in d:
            top_element = stack.pop() if stack else '#'
            if top_element != d[item]:
                return False
        else:
            stack.append(item)
    return not stack

def mergeTwoList(l1, l2):
    if not l1:
        return l2
    if not l2:
        return l1
    dummy = ListNode(0)
    p = dummy
    while l1 and l2:
        if l1.val < l2.val:
            p.next = l1
            l1 = l1.next
        else:
            p.next = l2
            l2 = l2.next
    if l1:
        p.next = l1
    if l2:
        p.next = l2
    return dummy.next

def mergeTwoList_(l1, l2):
    if not l1:
        return l2
    if not l2:
        return l1
    dummy = ListNode(0)
    p = dummy
    while l1 and l2:
        if l1.val < l2.val:
            p.next = l1
            l1 = l1.next
        else:
            p.next = l2
            l2 = l2.next
        p = p.next
    if l1:
        p.next = l1
    if l2:
        p.next = l2
    return dummy.next

def generateParenthesis(n):
    def generate(A='', left=0, right=0):
        if len(A==2*n:
            res.append(''.join(A))
            return 
        if left < n:
            generate(A+'(', left+1, right)
        if right < left:
            generate(A+')', left, right+1)
    res = []
    generate()
    return res 

def generateParenthesis_(n):
    def generate(A='', left=0, right=0):
        if len(A)==2*n:
            res.append(''.join(A))
            return 
        if left < n:
            generate(A+'(', left+1, right)
        if right < left:
            generate(A+')', left, right+1)
    res = []
    generate()
    return res

def mergeKList(lists):
    n = len(lists)
    start = 1
    while start < n:
        for i in range(0, n-start, start*2):
            lists[i] = merge(lists[i], lists[i+start])
        start *= 2
    return lists[0] if n>0 else lists

def merge(l1, l2):
    head = point = ListNode(0)
    while l1 and l2:
        if l1.val < l2.val:
            point.next = l1
            l1 = l1.next
        else:
            point.next = l2
            l2 = l2.next
        point = point.next
    if not l1:
        point.next = l1
    if not l2:
        point.next = l2
    return head.next

def mergeKList_(lists):
    n = len(lists)
    start = 1
    while start < n:
        for i in range(0, n-start, start*2):
            lists[i] = merge(lists[i], lists[i+start])
        start *= 2
    return lists[0] if n>0 else lists

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def swapPairs(head):
    pre, pre.next = self, head
    while pre.next and pre.next.next:
        a = pre.next
        b = a.next
        pre.next, b.next, a.next = b, a, b.next
        pre = a
    return self.next

def swapPairs_(head):
    pre, pre.next = self, head
    while pre.next and pre.next.next:
        a = pre.next
        b = a.next
        pre.next, b.next, a.next = b, a, b.next
        pre = a
    return self.next

def reverseKGroup(head, k):
    dummy = jump = ListNode(0)
    dummy.next = l = r = head
    while True:
        count = 0
        while r and count<k:
            r = r.next
            count += 1
        if count == k:
            cur, pre = l, r
            for _ in range(k):
                cur.next, cur, pre = pre, cur.next, cur
            jump.next, jump, l = pre, l, r
        else:
            return dummy.next

def reverseKGroup(head, k):
    dummy = jump = ListNode(0)
    dummy.next = l = r = head
    while True:
        count = 0
        while r and count<r:
            r = r.next
            count += 1
        if count == k:
            cur, pre = l, r
            for _ in range(k):
                cur.next, cur, pre = pre, cur.next, cur
            jump.next, jump, l = pre, l, r
        else:
            return dummy.next

def removeDuplicates(nums):
    if len(nums)==0:
        return 0
    i = 0
    for j in range(1, len(nums)):
        if nums[j]!=nums[i]:
            i += 1
            nums[i] = nums[j]
    return i+1

def removeDeplicates_(nums):
    if len(nums)==0:
        return 0
    i = 0
    for j in range(1, len(nums)):
        if nums[j] != nums[i]:
            i += 1
            nums[i] = nums[j]
    return i+1

def removeElement(nums, val):
    i = 0
    n = len(nums)
    while i<n:
        if nums[i]==val:
            nums[i] = nums[n-1]
            n -= 1
        else:
            i += 1
    return i

def removeElement(nums, val):
    i = 0
    n = len(nums)
    while i<n:
        if nums[i]==val:
            nums[i] = nums[n-1]
            n -= 1
        else:
            i += 1
    return i

def strStr(haystack, needle):
    if needle == "":
        return 0
    for i in range(len(haystack)-len(needle)+1):
        for j in range(len(needle)):
            if haystack[i+j]!=needle[j]:
                break
            if j == len(needle)-1:
                return i
    return -1

def devide(dividend, divisor):
    positive = (dividend<0) is (divisor<0)
    dividend, divisor = abs(dividend), abs(divisor)
    res = 0
    while dividend >= divisor:
        temp, i = divisor, 1
        while dividend >= temp:
            dividend -= temp
            res += 1
            i <<= 1
            temp <<= 1
    if not positive:
        res *= -1
    return min(max(-2**31, res), 2**31)

def divide(dividend, divisor):
    positive = (dividend<0) is (divisor<0)
    dividend, divisor = abs(dividend), abs(divisor)
    res = 0
    while dividend>=divisor:
        temp, i = divisor, 1
        while dividend >= temp:
            dividend -= temp
            res += i
            i<<=1
            temp <<= 1
    if not positive:
        res *= -1
    return min(2**31, max(res, -2**31))

def findSubstring(s, words):
    if len(words)==0:
        return []
    d = {}
    for w in words:
        if w in d:
            d[w] += 1
        else:
            d[w] = 1
    res = []
    l = len(words[0])
    for k in range(l):
        left = k
        subd = {}
        count = 0
        for j in range(k, len(s)-l+1, l):
            tword = s[j:j+l]
            if tword in d:
                if tword in subd:
                    subd[tword] += 1
                else:
                    subd[tword] = 1
                count += 1
                while subd[tword] > d[tword]:
                    subd[s[left:left+l]] -= 1
                    left += 1
                    count -= 1
                if count == len(words):
                    res.append(left)
            else:
                left = j + l
                subd = {}
                count = 0
    return res

def findSubstring(s, words):
    if len(words)==0:
        return []
    d = {}
    for w in words:
        if w in d:
            d[w] += 1
        else:
            d[w] = 1
    res = []
    l = len(words[0])
    for k in range(l):
        left = k
        subd = {}
        count = 0
        for j in range(k, len(s)-l+1, l):
            tword = s[j:j+l]
            if tword in d:
                if tword in subd:
                    subd[tword] += 1
                else:
                    subd[tword] = 1
                count += 1
                while subd[tword] > d[tword]:
                    subd[s[left:left+l]] -= 1
                    left += l
                    count -= 1
                if count == len(words):
                    res.append(left)
            else:
                left = j + l
                subd = {}
                count = 0
    return res
                
def nextPermutation(nums):
    i = len(nums)-2
    while i>=0 and nums[i]>=nums[i+1]:
        i -= 1
    if i>=0:
        j = len(nums)-1
        while j>=0 and nums[j]<=nums[i]:
            j -= 1
        nums[i], nums[j] = nums[j], nums[i]
    l, r = i+1, len(nums)-1
    while l<r:
        nums[l], nums[r] = nums[r],nums[l]
        l += 1
        r -= 1

def nextPermutation_(nums):
    i = len(nums)-2
    while i>=0 and nums[i]>=nums[i+1]:
        i -= 1
    if i>=0:
        j = len(nums)-1
        while j>=0 and nums[j]<=nums[i]:
            j -= 1
        nums[i], nums[j] = nums[j], nums[i]
    l, r = i+1, len(nums)-1
    while l<r:
        nums[l], nums[r] = nums[r], nums[l]
        l += 1
        r -= 1

def search(nums, target):
    l, r = 0, len(nums)-1
    while l<=r:
        mid = l + (r-l)//2
        if nums[mid] == target:
            return mid
        if nums[l] <= nums[mid]:
            if nums[l] <= target <= nums[r]:
                r = mid -1
            else:
                l = mid + 1
        else:
            if nums[mid] <= target <= nums[r]:
                l = mid + 1
            else:
                r = mid - 1
    return -1

def search_(nums, target):
    l, r = 0, len(nums)-1
    while l<=r:
        mid = (l+r)//2
        if nums[mid]==target:
            return mid
        if nums[mid] >= nums[l]:
            if nums[l] <= target <= nums[mid]:
                l = mid + 1
            else:
                r = mid - 1 
        else:
            if nums[mid] <= target <= nums[r]:
                l = mid + 1
            else:
                r = mid - 1
    return -1

def search_range(nums, target):
    left = find(nums, target, True)
    if left==len(nums) or nums[left]!=target:
        return [-1, -1]
    return [left, find(nums, target, False)-1]

def find(nums, target, flag):
    l, r = 0, len(nums)
    while l<r:
        mid = (l+r)//2
        if nums[mid]>=target or (flag and target==nums[mid]):
            r = mid
        else:
            l = mid + 1
    return l

def search_range(nums, target):
    left = find(nums, target, True)
    if left == len(nums) or nums[left]!=target:
        return [-1, -1]
    return [left, find(nums, target, False)-1]

def find(nums, target, flag):
    l, r = 0, len(nums)
    while l<r:
        mid = (l+r)//2
        if nums[mid]>target or (nums[mid]==target and flag):
            r = mid
        else:
            l = mid + 1
    return l


def searchInsert(nums, target):
    l, r = 0, len(nums)-1
    while l<=r:
        mid = (l+r)//2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            r = mid + 1
        else:
            l = mid + 1
    return l

def searchIndex(nums, target):
    l, r = 0, len(nums)-1
    while l<=r:
        mid = (l+r)//2
        if nums[mid] == target:
            return mid
        if nums[mid] > target:
            r = mid - 1
        else:
            l = mid + 1
    return l

def combinationSum(nums, target):
    nums.sort()
    res = []
    dfs(nums, target, 0, [], res)
    return res

def dfs(nums, target, index, path, res):
    if target<0:
        return
    if target ==0:
        res.append(path)
        return 
    for i in range(index, len(nums)):
        dfs(nums, target-nums[i], path+[nums[i]], res)

def comnination_(nums, target):
    res = []
    nums.sort()
    dfs(nums, target, 0, [], res)
    return res

def dfs(nums, target, index, path, res):
    if target<0:
        return
    if target==0:
        res.append(path)
    for i in range(index, len(nums)):
        dfs(nums, target-nums[i], i, path+[nums[i]], res)

def conbination2(nums, target):
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

def conination2(nums, target):
    nums.sort()
    res = []
    dfs(nums, target, 0, [], res)
    return res

def dfs(nums, target, index, path, res):
    if index<0:
        return 
    if index==0:
        res.append(path)
        return 
    for i in range(index, len(nums)):
        if i>0 and nums[i]==nums[i-1]:
            continue
        dfs(nums, target-nums[i], i+1, path+[nums[i]], res)

def firstMissingPostive(nums):
    for i in range(len(nums)):
        while 0<=nums[i]-1<len(nums) and nums[nums[i]-1]!=nums[i]:
            tmp = nums[i]-1
            nums[i], nums[tmp] = nums[tmp], nums[i]
    for i in range(len(nums)):
        if nums[i]!=i+1:
            return i+1
    return len(nums)+1

def firstMissingPostive(nums):
    for i in range(len(nums)):
        while 0<=nums[i]-1<len(nums) and nums[nums[i]-1]!=nums[i]:
            tmp = nums[i]-1
            nums[i],nums[tmp]=nums[tmp], nums[i]
    for i in range(len(nums)):
        if nums[i] != i+1:
            return i+1
    return len(nums)+1

def trap(nums):
    if not nums or len(nums)<3:
        return 0
    res = 0
    l, r = 0, len(nums)-1
    l_max, r_max = nums[l], nums[r]
    while l<=r:
        if nums[l] < nums[r]:
            if nums[l] > l_max:
                l_max = nums[l]
            else:
                res += l_max - nums[l]
            l += 1
        else:
            if nums[r]>r_max:
                r_max = nums[r]
            else:
                res += r_max - nums[r]
            r -= 1
    return res

def trap(nums):
    if not nums or len(nums)<3:
        return 0
    res = 0
    left, right = 0, len(nums)-1
    l_max, r_max = nums[left], nums[right]
    while left <= right:
        if nums[left] < nums[right]:
            if nums[left] > l_max:
                l_max = nums[left]
            else:
                res += l_max-nums[left]
            left += 1
        else:
            if nums[right] > r_max:
                r_max = nums[right]
            else:
                res += r_max-nums[right]
            right -= 1
    return res

def jump2(nums):
    start, end = 0, 0
    step = 0
    while end < len(nums)-1:
        step += 1
        maxend = end +1
        for i in range(start, end+1):
            if i+nums[i]>=len(nums)-1:
                return step
            maxend = max(maxend, i+nums[i])
        start, end = end+1, maxend
    return step

def jump2(nums):
    start, end = 0, 0
    step = 0
    while end < len(nums)-1:
        step += 1
        maxend = end + 1
        for i in range(start, end+1):
            if i+nums[i]>=len(nums)-1:
                return step
            maxend = max(maxend, i+nums[i])
        start, end = end+1, maxend
    return step

def jump(nums):
    start, end = 0, 0
    step = 0
    while end < len(nums)-1:
        step += 1
        maxend = end + 1
        for i in range(start, end+1):
            if i+nums[i]>=len(nums)-1:
                return step
            maxend = max(maxend, i+nums[i])
        start, end = end+1, maxend
    return step

def jump(nums):
    start, end = 0, 0
    step = 0
    while end<len(nums)-1:
        step += 1
        maxend = end + 1
        for i in range(start, end+1):
            if i+nums[i]>=len(nums)-1:
                return step
            maxend = max(maxend, i+nums[i])
        start, end = end+1, maxend
    return step

def permute(nums):
    res = []
    dfs(nums, [], res)
    return res

def dfs(nums, path, res):
    if not nums:
        res.append(path)
    for i in range(len(nums)):
        dfs(nums[:i]+nums[i+1:], path+[nums[i]], res)

def permute(nums):
    res = []
    dfs(nums, [], res)
    return res

def dfs(nums, path, res):
    if not nums:
        res.append(path)
    for i in range(len(nums)):
        dfs(nums[:i]+nums[i+1:], [path+nums[i]], res)

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

def rotate(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(i):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for i in range(len(matrix)):
        maxtrix[i] = matrix[i][::-1]
    return matrix

def rotate(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(i):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for i in range(len(matrix)):
        matrix[i] = matrix[i][::-1]
    return matrix

def groupAnagrams(strs):
    ans = dict()
    for item in strs:
        count = [0]*26
        for c in item:
            count[ord(c)-ord('a')] += 1
        if tuple(count) not in ans:
            ans[tuple(count)] = [item]
        else:
            ans[tuple(count)].append(item)
    return ans.values()

def groupAnagrams(strs):
    ans = dict()
    for item in strs:
        count = [0]*26
        for c in item:
            count[ord(c)-ord('a')] += 1
        if tuple(count) not in ans:
            ans[tuple(count)] = [item]
        else:
            ans[tuple(count)].append(item)
    return ans.values()

def myPow(x, n):
    if n==0:
        return 1
    if n<0:
        x = 1/x
    n = abs(n)
    x0 = x*x
    return myPow(x0, n/2) if (n%2==0) else x * myPow(x0, n//2)

def myPow(x, n):
    if n==0:
        return 1
    if n<0:
        x = 1/x
    n = abs(n)
    x0 = x*x
    return mypow(x0, n//2) if n%2==0 else x*myPow(x0, n//2)

def maxSubarray(nums):
    curSum = maxSum = nums[0]
    for item in nums:
        curSum = max(item, curSum + item)
        maxSum = max(maxSum, curSum)
    return maxSum

def maxSubArray(nums):
    curSum = maxSum = nums[0]
    for item in nums:
        curSum = max(item, ite+curSum)
        maxSum = max(curSum, maxSum)
    return maxSum

def jump(nums):
    m = 0
    for i, item in enumerate(nums):
        if i>m:
            return False
        m = max(m, i+item)
    return True

def jump(nums):
    m = 0
    for i, item in enumerate(nums):
        if i>m:
            return False
        m = max(m, i+item)
    return True


def merge(nums):
    nums.sort(key=lambda x: x[0])
    res = []
    for item in nums:
        if not res or res[-1][-1]<item[0]:
            res.append(item)
        else:
            res[-1][-1] = max(res[-1][-1], item[-1])
    return res

def merge(nums):
    nums.sort(key=lambda x: x[0])
    res = []
    for item in nums:
        if not res or res[-1][-1]<item[0]:
            res.append(item)
        else:
            res[-1][-1] = max(res[-1][-1], item[-1])
    return res

def insert(nums, num):
    s, e = num[0], num[-1]
    left, right = [], []
    for item in nums:
        if item[-1] < s:
            left.append(item)
        elif item[0] > e:
            right.append(item)
        else:
            s = min(s, item[0])
            e = max(e, item[-1])
    return left + [s, e] + right

def lengthoflastword(s):
    return len(s.strip().split(' ')[-1])

def rotateRight(head, k):
    if not head:
        return None
    if head.next = None:
        return head
    pointer = head
    length = 1
    while pointer.next:
        pointer = pointer.next
        length += 1
    rotatetimes = int(k%length)
    if k==0 or rotatetimes==0:
        return head
    fast = head
    slow = head
    for i in range(rotatetimes):
        fast = fast.next
    while fast.next:
        fast = fast.next
        slow = slow.next
    tmp = slow.next
    slow.next = None
    fast.next = head
    head = tmp
    return head

def uniquePaths(m, n):
    if m==1 or n==1:
        return 1
    dp = [[1 for col in range(n)] for row in range(m)]
    for i in range(1,m):
        for j in range(1,n):
            dp[io][j] = dp[i][j-1] + dp[i-1][j]
    return dp[i][j]

def unique(m , n):
    if m==1 or n==1:
        return 1
    dp = [[1  for col in range(n)] for row in range(m)]
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i][j-1] + dp[i-1][j]
    return dp[i][j]

def unique(m, n):
    if m==1 or n==1:
        return 1
    dp = [[1 for col in range(n)] for row in range(m)]
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i-1]][j] + dp[i][j-1]
    return dp[i][j]

def unique_(nums):
    m,n = len(nuns), len(nunms[0])
    if nums[0][0] = 1:
        return 0
    nums[0][0] = 1

    for i in range(1, m):
        nums[i][0] = int(nums[i][0]==0 and nums[i-1][0]==1)
    for j in range(1, n):
        nums[0][j] = int(nums[0][j]==0 and nums[0][j-1]==1)

    for i in range(1,m):
        for j in range(1, n):
            if nums[i][j] ==0:
                nums[i][j] = nums[i-1][j] + nums[i][j-1]
            else:
                nums[i][j] = 0
    return nums[-1][-1]


def unique_(nums):
    m, n = len(nums), len(nums[0])
    if nums[0][0] == 1:
        return 0
    nums[0][0] = 1

    for i in range(1, m):
        nums[i][0] = int(nums[i][0]==0 and nums[i-1][0]==1)
    for j in range(1, n):
        nums[0][j] = int(nums[0][j]==0 and nums[0][j-1]==1)
    
    for i in range(1,m):
        for j in range(1, n):
            if nums[i][j] == 0:
                nums[i][j] = nums[i-1][j] + nums[i][j-1]
            else:
                nums[i][j] = 0
    return nums[-1][-1]


def minpathsum(nums):
    m, n = len(nums), len(nums[0])
    for j in range(1, n):
        nums[0][j] += nums[0][j-1]
    for i in range(1, m):
        nums[i][0] += nums[i-1][0]
    for i in range(1,m):
        for j in range(1, n):
            nums[i][j] += min(nums[i-1][j], nums[i][j-1])
    return nums[-1][-1]


def minPathSum(nums):
    m, n = len(nums), len(nums[0])
    for j in range(1, n):
        nums[0][j] += nums[0][j-1]
    for i in range(1, m):
        nums[i][0] = nums[i-1][0]
    for i in range(1, m):
        for j in range(1, n):
            nums[i][j] += min(nums[i-1][j], nums[i][j-1])
    return nums[-1][-1]


def plusOne(nums):
    res = 0
    while len(nums)>0:
        item = nums.pop(0)
        res *= 10
        res += item
    return [int(i) for i in str(res+1)]

def addBinary(a, b):
    if len(a)==0:
        return b
    if len(b)==0:
        return a
    if a[-1]=='1' and b[-1]=='1':
        return addBinary(addBinary(a[0:-1], b[0:-1]), '1') + '0'
    elif a[-1]=='0' and b[-1]=='0':
        return addBinary(a[0:-1], b[0:-1]) + '0'
    else:
        return addBinary(a[0:-1], b[0:-1]) + '1'

def mysqrt(x):
    l, r = 0, x
    while l<=r:
        mid = (l+r)//2
        if mid * mid <= x < (mid+1)*(mid+1):
            return mid
        elif x < mid*mid:
            r = mid
        else:
            l = mid  + 1

def mySqrt(x):
    l, r = 0, x
    while l<=r:
        mid = (l+r)//2
        if mid * mid <= x < (mid+1)*(mid+1):
            return mid
        elif x < mid*mid:
            r = mid
        else:
            l = mid + 1

def climb(n):
    if n==1:
        return 1
    a, b = 1, 2
    for _ in range(3, n+1):
        a, b = b, a+b
    return b

def climb(n):
    if n==1:
        return 1
    a, b  = 1, 2
    for _ in range(3, n+1):
        a, b = b, a+b
    return b


def simplifyPath(path):
    stack = []
    for item in path.split('/'):
        if item in ('', '.'):
            pass
        elif item == '..':
            if stack:
                stack.pop()
        else:
            stack.append(item)
    return '/' + '/'.join(stack)


def minEdistance(word1, word2):
    m, n = len(word1), len(word2)
    dp = [[0]*(n+1) for _ in range(m+1)]
    for i in range(m+1):
        dp[i][0] = i
    for j in range(n+1):
        dp[0][j] = j
    for i in range(1, m+1):
        for j in range(1, n+1):
            if word1[i-1]==word2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = min(dp[i-1][j-1]+1, dp[i-1][j]+1, dp[i][j-1]+1)
    return dp[m][n]

def minDistance_(word1, word2):
    m, n = len(word1), len(word2)
    dp = [[0]*(n+1) for _ in range(m+1)]
    for i in range(m+1):
        dp[i][0] = i
    for j in range(n+1):
        dp[0][j] = j
    for i in range(1, m+1):
        for j in range(1, n+1):
            if word1[i-1]==word2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = min(dp[i-1][j]+1, dp[i][j-1]+1, dp[i-1][j-1]+1)
    return dp[m][n]

def setZeros(matrix):
    is_col = False
    R = len(matrix)
    C = len(matrix[0])
    for i in range(R):
        for j in range(C):
            if matrix[i][j] == 0:
                if j == 0:
                    is_col = True
                else:
                    matrix[0][j] = 0
                    matrix[j][0] = 0
    for i in range(1,R):
        for j in range(1,C):
            if matrix[i][0]==0 or matrix[0][j]==0:
                matrix[i][j] = 0
    if matrix[0][0]==0:
        for j in range(C):
            matrix[0][j]=0
    if is_col:
        for i in range(R):
            matrix[i][0]=0

def setZeros_(matrix):
    is_col = False
    R = len(matrix)
    C = len(matrix[0])
    for i in range(R):
        for j in range(C):
            if matrix[i][j]==0:
                if j==0:
                    is_col=True
                else:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
    for i in range(1, R):
        for j in range(1,C):
            if matrix[i][0]==0 or matrix[0][j]==0:
                matrix[i][j]=0
    if matrix[0][0] == 0:
        for j in range(C):
            matrix[0][j]=0
    if is_col:
        for i in range(R):
            matrix[i][0] = 0

def searchMatrix(matrix, target):
    for item in matrix:
        if len(item)>0 and item[-1]>=target:
            left, right = 0, len(item)-1
            while left<=right:
                mid = (left+right)//2
                if item[mid]==target:
                    return True
                elif item[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            break
    return False


