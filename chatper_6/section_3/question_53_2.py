# coding=utf-8
"""
在排序数组中查找数字
单次二分查找确定左右边界
"""

def search(nums, target):
    if not nums: return 0

    # 采用一次性查找左右边界
    left = 0
    right = len(nums)
    while left < right:
        mid = (left + right) >> 1
        if nums[mid] == target:
            i = j = mid
            while i>=0 and nums[i] == target:
                i -= 1
            while j<=len(nums)-1 and nums[j] == target:
                j += 1
            # (j-1) - (i+1) +1
            return j-i-1 
        elif nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid
    return 0  

if __name__ == '__main__':
    nums = [5,7,7,8,8,10]
    target = 8
    print(search(nums,target))
