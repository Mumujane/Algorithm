"""快速排序"""
"""
一、快速排序

1.介绍
快速排序由C. A. R. Hoare在1962年提出。它的基本思想是:通过一趟排序将要排序的数据分割成独立的两部分，
其中一部分的所有数据都比另外一部分的所有数据都要小，然后再按此方法对这两部分数据分别进行快速排序，整个排序过程可以递归进行，
以此达到整个数据变成有序序列。

2.步骤及流程图

(1)从数列中挑出一个元素，称“基准”

(2)重新排序数列，所有元素比基准值小的摆放在基准前面，所有元素比基准值大的摆在基准的后面（相同的数可以到任一边）。
在这个分区退出之后，该基准就处于数列的中间位置。这个称为分区（partition）操作。

(3)递归地（recursive）把小于基准值元素的子数列和大于基准值元素的子数列排序。
"""
import random

def qsort(list, low, high):
    if low >= high:
        return
    first = low
    last = high

    key = list[first]
    while last > first:
        while last > first and list[last]>= key:
            last -= 1
        list[first] = list[last]
        while last > first and list[first] <= key:
            first +=1
        list[last] = list[first]
    list[first] = key

    qsort(list, low, first -1)
    qsort(list, first+1, high)

my_list = []
for i in  range(8):
    my_list.append(random.randint(1,300))

qsort(my_list, 0 , len(my_list) -1)
print(my_list)


"""
快速排序 
"""

def quicksort(array):
    if len(array)<2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i> pivot]
    return quicksort(less)+[pivot] + quicksort(greater)

print(quicksort([10, 5, 2, 3]))
