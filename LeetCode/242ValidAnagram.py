"""
有效的字母异位词:字母一样, 顺序不一样
Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true

Example 2:

Input: s = "rat", t = "car"
Output: false

Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?

"""

# 解1: sort, 对任意进来的字母进行排序 O(NlogN) (快排)
# 解2: 数字母出现的个数, 使用map进行计数 {letter: count} 循环 O(n) *1 => O(n)
# 字典: python内部使用哈希表实现

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return sorted(s) == sorted(t)

    def isAnagram2(self, s, t):
        """

        :param s: str
        :param t: str
        :return: bool
        """
        dic1, dic2 = {}, {}
        for item in s:
            dic1[item] = dic1.get(item, 0) +1
        for item in t:
            dic2[item] = dic2.get(item, 0) +1
        return dic1 == dic2

    def isAnagram3(self, s, t):
        """

        :param s: str
        :param t: str
        :return: bool
        """
        dic1, dic2 = [0]*26, [0]*26
        for item in s:
            # 手写一个哈希函数, ord() 它以一个字符（长度为1的字符串）作为参数，返回对应的 ASCII 数值，或者 Unicode 数值，
            dic1[ord(item) - ord('a')] += 1
        for item in t:
            dic2[ord(item) - ord('a')] += 1

        return dic1 == dic2


if __name__ == '__main__':
    solution = Solution()
    isanagram1 = solution.isAnagram("anagram","anagram")
    print("是否相等方法1:%s"%isanagram1)

    isanagram2 = solution.isAnagram2("anagram", "anagran")
    print("是否相等方法2:%",isanagram2)

    isanagram3 = solution.isAnagram3("anagram", "anagram")
    print("是否相等方法3:%", isanagram3)
