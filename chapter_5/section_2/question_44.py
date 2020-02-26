# coding=utf-8
"""
数字序列中某一位的数字
思路：对于第 n 位对应的数字，我们令这个数字对应的数为 target，然后分三步进行。

首先找到这个数字对应的数是几位数，用 digits 表示；
然后确定这个对应的数的数值 target；
最后确定返回值是 target 中的哪个数字。
"""


def findNthDigit(n):
    # 首先判断target是几位数，用digits表示
    base = 9
    digits = 1
    while n - base * digits > 0:
        n -= base * digits
        base *= 10
        digits += 1
    # 计算target的值
    idx = n % digits  # 注意由于上面的计算，n现在表示digits位数的第n个数字
    if idx == 0: 
        idx = digits
    number = 1
    for i in range(1,digits):
        number *= 10
    if idx == digits:
        number += n // digits - 1
    else:
        number += n // digits
    # 找到target中对应的数字
    for i in range(idx,digits):
        number //= 10
    return number % 10
    


if __name__ == '__main__':
    n=11
    print(findNthDigit(n))