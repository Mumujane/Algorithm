"""
    插入排序
        Insertion Sort）的算法描述是一种简单直观的排序算法。
        它的工作原理是通过构建有序序列，对于未排序数据，在已排序序列中从后向前扫描，找到相应位置并插入。
        在从后向前扫描过程中，需要反复把已排序元素逐步向后挪位，为最新元素提供插入空间。

2.步骤

(1)从第一个元素开始，该元素可以认为已经被排序

(2)取出下一个元素，在已经排序的元素序列中从后向前扫描

(3)如果该元素（已排序）大于新元素，将该元素移到下一位置

(4)重复步骤3，直到找到已排序的元素小于或者等于新元素的位置

(5)将新元素插入到该位置中

(6)重复步骤2


"""
import random

def insert_sort(lists):
    count = len(lists)
    for i in range(1, count):
        key = lists[i]
        j = i-1
        while j >= 0:
            if lists[j] > key:
                lists[j+1] = lists[j]
                lists[j] = key
            j -= 1
    return lists

my_list = []
for i in range(10):
    my_list.append(random.randint(1,300))
insert_sort(my_list)
print(my_list)

