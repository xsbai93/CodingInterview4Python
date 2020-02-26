# coding=utf-8
"""
数组中除了两个只出现一次的数字外，其他数字都出现了3遍
"""


def singleNumber(nums):
    res = 0
    for i in range(32):
        cnt = 0  # 记录当前 bit 有多少个1
        bit = 1 << i  # 记录当前要操作的 bit
        for num in nums:
            if num & bit != 0:
                cnt += 1
        if cnt % 3 != 0:
            # 不等于0说明唯一出现的数字在这个 bit 上是1
            res |= bit

    return res - 2 ** 32 if res > 2 ** 31 - 1 else res

if __name__ == '__main__':
    test = [9,1,7,9,7,9,7]
    print(singleNumber(test))
