#
# @lc app=leetcode id=220 lang=python3
#
# [220] Contains Duplicate III
#
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        # 检验数据合法性
        if k < 1 or t < 0:
            return False
        # 这里采用有序字典，它是dict的一个继承子类，按照元素输入顺序进行排序
        dic = collections.OrderedDict()
        for n in nums:
            # 注意判断t是否为0
            key = n if not t else n // t
            for m in (dic.get(key - 1), dic.get(key), dic.get(key + 1)):
                # 如果找到一个数满足条件一，返回
                if m is not None and abs(n - m) <= t:
                    return True
            if len(dic) == k:
                # 维持字典大小为k，如果超过，删除first；函数原型：dict.popitem(last=False)，不加参数表示随机从头尾删除一个
                dic.popitem(False)
            # 加入新数
            dic[key] = n
        return False
