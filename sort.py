# -*- encoding=UTF-8 -*-
import random
import sys

def random_int_list(start, stop, length):
    # 随机数组生成
    start, stop = (int(start), int(stop)) if start <= stop else (int(stop), int(start))
    length = int(abs(length)) if length else 0
    random_list = []
    for i in range(length):
        random_list.append(random.randint(start, stop))
    return random_list

def insert_sort(a):
    # 插入排序
    count = len(a)
    for i in range(1, count):
        key = a[i]
        j = i - 1
        while j >= 0:
            if a[j] > key:
                a[j + 1] = a[j]
                a[j] = key
            j -= 1
    return a

def merge(nums, first, middle, last):
    # 归并排序,切片边界,左闭右开并且是了0为开始
    lnums = nums[first:middle+1]
    rnums = nums[middle+1:last+1]
    lnums.append(sys.maxint)
    rnums.append(sys.maxint)
    l = 0
    r = 0
    for i in range(first, last+1):
        if lnums[l] < rnums[r]:
            nums[i] = lnums[l]
            l += 1
        else:
            nums[i] = rnums[r]
            r += 1
def merge_sort(nums, first, last):
    # merge_sort函数中传递的是下标，不是元素个数
    if first < last:
        middle = (first + last) / 2
        merge_sort(nums, first, middle)
        merge_sort(nums, middle+1, last)
        merge(nums, first, middle, last)

def select_sort(a):
    ''''' 选择排序
    每一趟从待排序的数据元素中选出最小（或最大）的一个元素，
    顺序放在已排好序的数列的最后，直到全部待排序的数据元素排完。
    选择排序是不稳定的排序方法。
    '''
    a_len=len(a)
    for i in range(a_len):#在0-n-1上依次选择相应大小的元素
        min_index = i#记录最小元素的下标
        for j in range(i+1, a_len):#查找最小值
            if(a[j] < a[min_index]):
                min_index = j
        if min_index != i:#找到最小元素进行交换
            a[i],a[min_index] = a[min_index],a[i]

def shell_sort(a):
    # shell排序
    a_len=len(a)
    gap = a_len / 2 #增量
    while gap > 0:
        for i in range(a_len):#对同一个组进行选择排序
            m=i
            j = i + 1
            while j < a_len:
                if a[j] < a[m]:
                    m = j
                j += gap #j增加gap
            if m != i:
                a[m],a[i] = a[i],a[m]
        gap /= 2

def partition1(A, p, r):

    x = A[r]
    i = p - 1
    j = p
    while j < r:
        if A[j] < x:
            i += 1
            A[i], A[j] = A[j], A[i]
        j += 1
    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1

def partition2(A, p, r):

    i = p
    j = r
    x = A[p]
    while i == x and i < j:
        j -= 1
        A[i] = A[j]
        while A[i] <= x and i < j:
            i += 1
    A[j] = A[i]
    A[i] = x
    return i

# quick sort
def quick_sort(A, p, r):

    if p < r:
        q = partition2(A, p, r)
        quick_sort(A, p, q - 1)
        quick_sort(A, q + 1, r)

if __name__ == '__main__':
    nums = random_int_list(1,20,5)
    print 'nums is:\n',nums
    insert_sort(nums)
    print 'insert sort:\n',nums
    print 'merge_sort:\n',nums
    print 'select_sort:\n',nums
    print 'shell_sort:\n',nums
    print 'quick_sort:\n',nums