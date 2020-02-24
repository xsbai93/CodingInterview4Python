# coding=utf-8
"""
机器人的运动范围

用回溯法解决
把方格看成一个m*n的矩阵，从(0,0)开始移动。
当准备进入坐标(i,j)是，通过检查坐标的数位来判断机器人能否进入。如果能进入的话，接着判断四个相邻的格子。
"""

def judge(threshold, i, j):
    # sum(map(int, str(i) + str(j)))这一句简直精髓! 直接得到坐标位置的 位和! i,j是超过1位的数也可以完美解决!
    if sum(map(int, str(i) + str(j))) <= threshold:
        return True
    else:
        return False

def findgrid(threshold, rows, cols, matrix, i, j):
    count = 0
    if i<rows and j<cols and i>=0 and j>=0 and judge(threshold, i, j) and matrix[i][j] == 0: # matrix[i][j]==0表示没走过这一格
        matrix[i][j] = 1  # 表示已经走过了
        count = 1 + findgrid(threshold, rows, cols, matrix, i, j+1) \
        + self.findgrid(threshold, rows, cols, matrix, i, j-1) \
        + self.findgrid(threshold, rows, cols, matrix, i+1, j) \
        + self.findgrid(threshold, rows, cols, matrix, i-1, j)
    return count

def movingCount(threshold, rows, cols):
    matrix = [[0 for i in range(cols)] for j in range(rows)]
    count = findgrid(threshold, rows, cols, matrix, 0, 0)
    return count
 

if __name__ == '__main__':
    count = movingCount(9, 12, 12)
    print(count)
