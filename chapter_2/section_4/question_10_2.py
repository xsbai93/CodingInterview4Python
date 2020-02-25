# coding=utf-8
"""
青蛙跳台阶问题
一只青蛙一次可以跳上1级台阶，也可以跳上2级台阶。求该青蛙跳上一个 n 级的台阶总共有多少种跳法。
答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。
"""
"""
因为0个台阶也有一种走法,所以f(0)=1
f(0)=1,f(1)=1,f(n)=f(n-1)+f(n-2)
"""

def numWays(n: int) -> int:
    dp = {}
    dp[0] = 1
    dp[1] = 1
    if n > 1:
        for i in range(2,n+1):
            dp[i] = dp[i-1] + dp[i-2]
            
    return dp[n]%1000000007

if __name__ == '__main__':
    num = 10
    print(numWays(num))