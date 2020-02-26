# coding=utf-8
"""
股票的最大利润
擂台法
"""


def maxProfit(prices):
    if not prices:
        return 0
    preMin,ans = prices[0],0
    for i in range(1,len(prices)):
        ans = max(ans,prices[i]-preMin)
        preMin = min(preMin,prices[i])
    return ans

if __name__ == '__main__':
    nums = [7,1,5,3,6,4]
    print(maxProfit(nums))
