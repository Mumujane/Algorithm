"""
No.3 Longest Substring without Repeating Characters

    题目大意：给出一个字符串，找到最长的没有重复字符的子字符串，并返回该子字符串的长度。
例如：
Given "abcabcbb", the answer is "abc", which the length is 3.
Given "bbbbb", the answer is "b", with the length of 1.
Given "pwwkew", the answer is "wke", with the length of 3.
Note that the answer must be a substring,
"pwke" is a subsequence and not a substring.

# """
# def findsrt(str):
#     new_srt = []
#     for s in str:
#
#
class Mysolution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :param s: str
        :return: int
        """
        max_len = 0
        if(len(s) == 1 or len(s) == 0 ):
            max_len = len(s)

        for i in range(0, len(s)-1):
            print(i)
            for j in range(i+1, len(s)):
                print("---%d"%j)
                if s[j] in s[i:j]:
                    if j-i > max_len:
                        right = j
                        left = i
                        max_len = right-left
                    break
                elif j == len(s) -1:
                    if max_len < j-i +1:
                        max_len = j- i +1
        return max_len

    def lengthOfLongestSubstringUp(self, s):
        """
        :param s: str
        :return: int
        """
        indexDict = {}
        maxLength = currMax = 0

        for i in range(len(s)):
            if s[i] in indexDict and i - indexDict[s[i]] -1 <= currMax:
                if maxLength < currMax:
                    maxLength = currMax
                currMax = i - indexDict[s[i]] - 1
            currMax = currMax +1
            indexDict[s[i]] = i
        return maxLength if currMax < maxLength else currMax


solution = Mysolution()
num1 = solution.lengthOfLongestSubstring("abcabcbb")
print(num1)

# num2 = solution.lengthOfLongestSubstringUp("abcabcbb")
# print(num2)

