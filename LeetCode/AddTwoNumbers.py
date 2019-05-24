"""
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order and each of their nodes contain a single digit.
 Add the two numbers and return it as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.

大意: 给出两个链表，存储非负数，
两个链表都是按倒序方式存储数字（个位，十位，百位 ……）要求将两个链表相加并以链表形式返回。

例如：
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.

知识:

① 什么是链表？
举个例子：在我们存储一大波数据时，我们很多时候是使用数组，但是当我们执行插入操作的时候就非常麻烦，
有一堆数据1,2,3,5,6,7我们要在3和5之间插入4,如果用数组，我们会怎么做？
当然是将5之后的数据往后退一位，然后再插入4,这样非常麻烦，效率也非常低，
但是如果用链表，我就直接在3和5之间插入4就行。

② 链表基本操作？
初始化链表、链表长度、插入、删除、新增、查找、逆序。具体就不展开了~

"""




























