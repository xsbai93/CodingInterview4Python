# coding=utf-8
"""
构建乘积数组
"""

def constructArr(A):
    if not A:
        return []
    prefix = [1]*len(A)
    prefix[0]=1
    for i in range(1,len(A)):
        prefix[i] = prefix[i-1]*A[i-1]
    cur_suffix = 1
    for i in range(len(A)-1,-1,-1):
        prefix[i] = prefix[i] * cur_suffix
        cur_suffix *= A[i]
    return prefix


if __name__ == '__main__':
    nums = [1,2,3,4,5]
    print(constructArr(nums))
