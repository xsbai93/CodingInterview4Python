# coding=utf-8
"""
矩阵中的路径

用回溯法解决
首先，遍历这个矩阵，我们很容易就能找到与字符串str中第一个字符相同的矩阵元素ch。然后遍历ch的上下左右四个字符，如果有和字符串str中下一个字符相同的，就把那个字符当作下一个字符（下一次遍历的起点），如果没有，就需要回退到上一个字符，然后重新遍历。为了避免路径重叠，需要一个辅助矩阵来记录路径情况。
下面代码中，当矩阵坐标为（row，col）的格子和路径字符串中下标为pathLength的字符一样时，从4个相邻的格子（row，col-1）、（row-1，col）、（row，col+1）以及（row+1，col）中去定位路径字符串中下标为pathLength+1的字符。
如果4个相邻的格子都没有匹配字符串中下标为pathLength+1的字符，表明当前路径字符串中下标为pathLength的字符在矩阵中的定位不正确，我们需要回到前一个字符串（pathLength-1），然后重新定位。
一直重复这个过程，直到路径字符串上所有字符都在矩阵中找到格式的位置（此时str[pathLength] == ‘\0’）
"""
def hasPath(matrix, rows, cols, path):
    if not matrix and rows <= 0 and cols <= 0 and path == None:
        return False
    boolmatrix = [0] * (rows * cols)
    #boolmatrix = [ [0 for _ in range(cols)] for _ in range(rows)]    
    #也可以，后面都使用 矩阵boolmatrix[i][j]的形式
    pathLength = 0
    for row in range(rows):
        for col in range(cols):
            if hasPathCore(matrix, rows, cols, row, col, path, pathLength, boolmatrix):
                return True
    return False
    
def hasPathCore(matrix, rows, cols, row, col, path, pathLength, boolmatrix ):
    if len(path) == pathLength:
        return True
        
    hasNextPath = False
    if ( row >= 0 and row < rows and col >= 0 and col < cols and 
        matrix[row*cols + col] == path[pathLength] and not boolmatrix[row*cols + col] ):
        pathLength += 1
        boolmatrix[row*cols + col] = True
        #进行该值的上下左右的递归(周围是否存在下一个路径点)
        hasNextPath = (hasPathCore(matrix, rows, cols, row-1, col, path, pathLength, boolmatrix) 
                    or hasPathCore(matrix, rows, cols, row, col+1, path, pathLength, boolmatrix) 
                    or hasPathCore(matrix, rows, cols, row+1, col, path, pathLength, boolmatrix) 
                    or hasPathCore(matrix, rows, cols, row, col-1, path, pathLength, boolmatrix))
        #对标记矩阵进行布尔值标记
        if not hasNextPath:    #说明周围4个点都存在下一路径
            pathLength -= 1    #回到前一个字符
            boolmatrix[row*cols + col] = False    #将该点重新设为未标记
    return hasNextPath

if __name__ == '__main__':
    #数组以一维数组输入，通过行列判断
    matrix=['a','b','c','e','s','f','c','s','a','d','e','e']
    rows=3
    cols=4
    path="bcced"
    print(hasPath(matrix, rows, cols, path))
