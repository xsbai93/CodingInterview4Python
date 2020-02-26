# coding=utf-8
"""
滑动窗口的最大值
"""

from collections import deque
def maxSlidingWindow(nums, k):
    if not nums :
        return []
    result = []
    deque_ = []
    for i in range(len(nums)):
        while deque_ and nums[deque_[-1]] < nums[i]:
            deque_.pop()
        deque_.append(i)
        if deque_[0] == (i - k):
            deque_.pop(0)
        if i >= k-1:
            result.append(nums[deque_[0]])
    return result

if __name__ == '__main__':
    nums = [1,3,-1,-3,5,3,6,7]
    k = 3
    print(maxSlidingWindow(nums, k))
