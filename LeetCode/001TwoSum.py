
"""
Given an array of integers, return indices of the two numbers
such that they add up to a specific target.
You may assume that each input would have exactly one solution,
 and you may not use the same element twice.

解释:

给出一个数字列表和一个目标值（target），

假设列表中有且仅有两个数相加等于目标值，我们要做的就是找到这两个数，并返回他们的索引值。

例如:

Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

"""

# 方法 一 暴力破解
def twoSum(lists, target):
    res = []
    for i in range(len(lists)):
        for j in range(i+1, len(lists)-1):
            if lists[i] + lists[j] == target:
                res.append(i)
                res.append(j)
                return res


print(twoSum([2, 7, 11, 15, 16], 18))
print("****"*10)

# 方法二

"""分析:
通过判断target与某一个元素的差值是否也在列表之中即可
"""

def towSumUp(nums, target):
    res = []
    for i in range(len(nums)):
        oneNum = nums[i]
        twoNum = target - oneNum
        if twoNum in nums:
            j = nums.index(twoNum)
            if i != j:
                res.append(i)
                res.append(j)
                return res


print(towSumUp([2, 7, 11, 15], 17))
print("****"*10)

# 方法三
"""
    分析:
    通过创建字典，将nums里的值和序号对应起来，
    并创建另一个字典存储目标值（Target）-nums的值，
    通过判断该值是否在nums内进行判断并返回其对应索引值，

"""

def twoSumUpPlus(nums, target):
    """
    :param nums: List[int]
    :param target: int
    :return: List[int]
    """

    num_dic = {nums[i]:i for i in range(len(nums))}
    print(num_dic)

    num_dic2 = {i:target-nums[i] for i in range(len(nums))}
    print(num_dic2)

    res = []

    for i in range(len(nums)):
        j = num_dic.get(num_dic2.get(i))
        if (j is not None) and (j != i):
            result = [i,j]
            break
    return result

print(twoSumUpPlus([2, 7, 11, 15, 1, 16], 17))
print("****"*10)

# 参考 使用Set
def twoSum2(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    n = len(nums)
    dd = {nums[i]:i for i in range(n)}
    print(dd)
    for i in range(n-1):
        cha = target - nums[i]
        if cha in dd and i != dd[cha]:
            return [i, dd[cha]]
    return 'null'

print("---"*10)
print(twoSum2([2, 7, 11, 15, 25, 1, 22, 4], 26))


#? 只输出一个解?