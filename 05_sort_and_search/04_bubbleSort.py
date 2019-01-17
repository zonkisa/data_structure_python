# coding: utf-8
# 其为 1/2n^2 - 1/2n。 这仍然是 O(n^2)比较
# 最低效的排序方法，因为它必须在最终位置被知道之前交换项
# 如果发现列表已排序，可以修改冒泡排序提前停止。
# 这意味着对于只需要遍历几次列表，冒泡排序具有识别排序列表和停止的优点, 短冒泡排序


def bubbleSort(alist):
    for passnum in range(len(alist)-1, 0, -1):
        for i in range(passnum):
            if alist[i] > alist[i+1]:
                tmp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = tmp


def shortBubbleSort(alist):
    exchanges = True
    passnum = len(alist) - 1
    while passnum > 0 and exchanges:
        exchanges = False
        for i in range(passnum):
            if alist[i] > alist[i+1]:
                exchanges = True
                tmp = alist[i]
                alist[i] = alist[i + 1]
                alist[i + 1] = tmp

        passnum -= 1


alist = [20, 30, 40, 90, 50, 60, 70, 80, 100, 110]
shortBubbleSort(alist)
print alist

















