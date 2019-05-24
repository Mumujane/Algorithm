"""
No.4 Median of Two Sorted Arrays

There are two sorted arrays nums1 and nums2 of size m and n respectively.
Find the median of the two sorted arrays.
The overall run time complexity should be O(log (m+n))..


题目大意：给出两个有序的数字列表，长度分别为m,n。找到这两个列表中的中间值。


eg:

#例子一：总长度为奇数
nums1 = [1, 3]
nums2 = [2]
The median is 2.0
#例子二：总长度为偶数
nums1 = [1, 2]
nums2 = [3, 4]
The median is (2 + 3)/2 = 2.5


"""

class mysolution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """

        :param nums1:
        :param nums2:
        :return: float
        """

        nums3 = [0] * (len(nums1) + len(nums2))
        l_i, r_i, i = 0,0,0
        while(l_i < len(nums1)) and (r_i < len(nums2)):
            if nums1[l_i] < nums2[r_i]:
                nums3[i] = nums1[l_i]
                l_i += 1

            else:
                nums3[i] = nums2[r_i]
                r_i += 1
            i += 1


        if l_i != len(nums1):
            nums3[i:] = nums1[l_i:]
        else:
            nums3[i:] = nums2[r_i:]

        len_3 = len(nums3)

        if len_3 %2 != 0:
            return float(nums3[(len_3 -1)//2])

        return (nums3[len_3[len_3//2 -1]+nums3[len]])
































