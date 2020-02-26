# coding=utf-8
"""
把数字翻译成字符串
动态规划
"""

def translateNum(num):
    str_num = str(num)
    n = len(str_num)
    dp = [1 for _ in range(n + 1)] 
    for i in range(2, n + 1):
        if str_num[i - 2] == '1' or \
        (str_num[i - 2] == '2' and str_num[i - 1] < '6'):
            dp[i] = dp[i - 2] + dp[i - 1]
        else:
            dp[i] = dp[i - 1]
    return dp[n]

if __name__ == '__main__':
    n = 12258
    print(translateNum(n))