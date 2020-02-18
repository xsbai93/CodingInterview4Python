# coding=utf-8
"""
问题：重建二叉树
递归实现思路：
1、先进行判空处理
2、因为前序遍历的顺序是：根节点--->左节点--->右节点，所以此二叉树的根节点为pre[0].
3、从1中已得知根节点为pre[0],则我们来看中序排列：
我们都知道中序排列的遍历顺序是：左节点--->根节点--->右节点，
那么我们可以从根节点着手，然后从中序遍历所得结果中获取此二叉树的左子树为[4,7,2]，右子树为[5,3,6,8]
4、需要注意的是：遍历左右子树时仍然采用前序遍历方法。
5、依次使用递归执行即可
"""


def reConstructBinaryTree(pre, tin):
    # write code here
    if len(pre) == 0:
        return None
    if len(pre) == 1:
        return TreeNode(pre[0])
    else:
        res = TreeNode(pre[0])
        res.left = reConstructBinaryTree(
            pre[1:tin.index(pre[0])+1], tin[:tin.index(pre[0])])
        res.right = reConstructBinaryTree(
            pre[tin.index(pre[0])+1:], tin[tin.index(pre[0])+1:])
    return res


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


if __name__ == '__main__':
    pre = [1, 2, 4, 7, 3, 5, 6, 8]
    tin = [4, 7, 2, 1, 5, 3, 8, 6]
    print(reConstructBinaryTree(pre, tin))
