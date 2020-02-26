# coding=utf-8
"""
0～n-1中缺失的数字
"""

def missingNumber(nums):
    for i in range(len(nums)):
        if nums[i] != i:
            return i
    return i + 1
    
if __name__ == '__main__':
    nums = [0,1,2,3,5,6,7]
    print(missingNumber(nums))
