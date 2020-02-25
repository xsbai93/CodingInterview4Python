# coding=utf-8
"""
剪绳子
完全背包问题 处理。

dp[j] 表示长度为j的绳子，乘积的最大值
背包容量为n
注意：dp[0] = 1，因为求乘积的最大值，当i==j时，dp[0]要等于1
"""

def cuttingRope(n: int) -> int:
    dp = [0] * (n+1)
    dp[0] = 1

    for i in range(1, n): #注意这里是n 不是n+1
        for j in range(i, n+1):
            dp[j] = max(dp[j], dp[j-i]*i)
    
    return dp[n] % int(1e9+7)


if __name__ == '__main__':
    n = 10
    print(cuttingRope(n))
