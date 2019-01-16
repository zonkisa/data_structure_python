# coding:utf-8
# 有序列表条件下
# 可以使用列表的有序性质来消除剩余项的一半
# 最大比较数相对于列表中的项是对数的。 因此，二分查找是 O(log n)

# 可以排序一次，然后查找多次，排序的成本就不那么重要。
# 然而，对于大型列表，一次排序可能是非常昂贵，从一开始就执行顺序查找可能是最好的选择。

def binarySearch(alist, item):
    left = 0
    right = len(alist) - 1
    mark = False

    while left <= right and not mark:
        midpoint = (left + right)//2
        if alist[midpoint] == item:
            mark = True
        else:
            if item < alist[midpoint]:
                right = midpoint - 1
            else:
                left = midpoint + 1

    return mark


testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
print binarySearch(testlist, 3)
print binarySearch(testlist, 13)


# 递归调用二分查找函数
# 切片创建部分列表,Python中的 slice 运算符实际上是 O(k),
# 即使用 slice 的二分查找将不会在严格的对数时间执行
# 这可以通过传递列表连同开始和结束的索引来纠正

def recursiveBinarySearch(alist, item):
    if len(alist) == 0:
        return False
    else:
        midpoint = len(alist)//2
        if alist[midpoint] == item:
            return True
        else:
            if item < alist[midpoint]:
                return recursiveBinarySearch(alist[:midpoint], item)
            else:
                return recursiveBinarySearch(alist[midpoint+1:], item)


print recursiveBinarySearch(testlist, 3)
print recursiveBinarySearch(testlist, 13)

