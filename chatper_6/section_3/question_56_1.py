# coding=utf-8
"""
数组中除了两个只出现一次的数字外，其他数字都出现了两遍
按位异或，在得到的值中找到二进制最后一个1，然后把数组按照该位是0还是1分为两组
"""


def singleNumber(nums):
        single_number = 0
        for num in nums:
            single_number ^= num
        return single_number

if __name__ == '__main__':
    test = [1, 2, 3, 4, 3, 1, -1, -1]
    print(singleNumber(test))
