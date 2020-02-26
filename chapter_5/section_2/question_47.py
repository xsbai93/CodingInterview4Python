# coding=utf-8
"""
礼物的最大价值
动态规划
"""

def maxValue(grid):
    m, n = len(grid), len(grid[0])
    dp = [[None] * n for _ in range(m)]
    dp[0][0] = grid[0][0]
    # 第一行
    for col in range(1, n):
        dp[0][col] = dp[0][col-1] + grid[0][col]
    # 第一列
    for row in range(1, m):
        dp[row][0] = dp[row-1][0] + grid[row][0]
    # 其他部分
    for row in range(1, m):
        for col in range(1, n):
            dp[row][col] = grid[row][col] + max(dp[row-1][col], dp[row][col-1])
    return dp[m-1][n-1]



if __name__ == '__main__':
    grid = [[1,3,1],[1,5,1],[4,2,1]]
    print(maxValue(grid))
  
