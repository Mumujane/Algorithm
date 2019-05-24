"""
判断一个整数列表，是否去掉其中某一个数据后，列表呈升序排列。
要求：
数据区间为：-100000<=num<=100000，且列表长度为：2<=len<=100000
遇到的问题：
在数据达到：5000的时候提示运行时间过长


"""
import numpy as np


def almostIncreasingSequence(sequence):
    list1 = sequence
    lon = len(list1)
    if lon == 2:
        return True
    if lon > 2 and lon <= 100000:
        for i in list1:
            if i >= -100000 and i <= 100000:
                continue
            else:
                print("the element of sequence should between -100000 and 100000")
        list2 = sorted(list1)
        for i in list1:  # 查询列表中，重复数据的情况
            b = list1.count(i)
            if b > 2:  # 如果重复次数超过2，则返回false
                return False
            if b == 2:  # 如果重复次数等于2，则判断两次出现的位置数据情况
                a = []
                for j in range(0, lon):
                    if list1[j] == i:
                        a.append(j)
                    a = sorted(a)
                if i < list1[a[1] - 1]:  # 如果index比较大的重复数据，比它前边的数据小，则删除该数据后，判断是否升序
                    del list1[a[1]]
                else:
                    del list1[a[0]]  # 否则删除index比较小的重复数据，再判断是否升序
                list2 = sorted(list1)
                for j in list2:
                    if list2.count(j) >= 2:
                        return False
                if list1 == list2:
                    return True
                else:
                    return False
        if list1 == list2:
            return True
        else:
            a = np.max(list1)  # 没有重复数据的情况下，判断列表最大值与列表最后一个值是否相等，如果不相等，则删除最后一项后，判断列表是否正序排列
            if a != list1[lon - 1]:
                list1.remove(a)
                list2 = sorted(list1)
                if list1 == list2:
                    return True
                else:
                    return False
            else:  # 如果最大值与列表最后一个元素相等，则找出列表中的最小值，删除它后，判断列表是否为升序，
                list1.remove(a)
                b = np.min(list1)
                list1.remove(b)
                list2 = sorted(list1)
                if list2 == list1:
                    return True
                else:
                    return False
    else:
        print("the length of sequence should between 2 and 100000")
