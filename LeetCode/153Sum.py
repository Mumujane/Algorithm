"""
Given an array nums of n integers, are there elements a, b, c in nums
such that a + b + c = 0?

Find all unique triplets in the array which gives the sum of zero.

Note:
The solution set must not contain duplicate triplets.
Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]

"""


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) < 3:
            return []
        nums.sort()

        res = set()
        for i, v in enumerate(nums[:-2]):
            if i >= 1 and v == nums[i-1]:
                continue
            d = {}
            for x in nums[i+1:]:
                if x not in d:
                    d[-v-x] = 1
                else:
                    res.add((v, -v-x, x))
        return map(list, res)


print("---"*10)
solution = Solution()
# python3需要将map之转为list对象才能打印，print(list(map))
print(list(solution.threeSum([-1,0,1,2,-1,-4])))

"""
补充知识:
Enumerate

主要是用在循环里，是一个能返回元组的迭代器，元组的内容是循环的对象的索引，和循环对象的值
enumerate 是一个会返回元组迭代器的内置函数，这些元组包含列表的索引和值。
当你需要在循环中获取可迭代对象的每个元素及其索引时，将经常用到该函数。
letters = ['a', 'b', 'c', 'd', 'e']
for i, letter in enumerate(letters):
    print(i, letter)

这段代码将输出：
0 a
1 b
2 c
3 d
4 e

"""