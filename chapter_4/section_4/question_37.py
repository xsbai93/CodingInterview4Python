# coding=utf-8
"""
 序列化二叉树
 层序遍历， 带上none， 逗号分割成字符串。
反序列化时分割字符串成list。就变成基本的层序遍历恢复二叉树的题了。
"""

from collections import deque

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Tree(object):
    """
    非二叉搜索树，建树的时候values中的顺序需要注意
    之后有时间会改成二叉搜索树
    """
    def __init__(self):
        self.root = None

    def construct_tree(self, values=None):
        # 结点值不存在的话，values中用None表示
        if not values:
            return None
        self.root = TreeNode(values[0])
        queue = deque([self.root])
        leng = len(values)
        nums = 1
        while nums < leng:
            node = queue.popleft()
            if node:
                node.left = TreeNode(values[nums]) if values[nums] else None
                queue.append(node.left)
                if nums + 1 < leng:
                    node.right = TreeNode(values[nums + 1]) if values[nums + 1] else None
                    queue.append(node.right)
                    nums += 1
                nums += 1

    def bfs(self):
        ret = []
        queue = deque([self.root])
        while queue:
            node = queue.popleft()
            if node:
                ret.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
        return ret


class Solution:
    def __init__(self):
        self.sIndex = 0

    def recursionSerialize(self, root):
        series = ''
        if root == None:
            series += ',$'
        else:
            series += (',' + str(root.val))
            series += self.recursionSerialize(root.left)
            series += self.recursionSerialize(root.right)
        return series

    def Serialize(self, root):
        return self.recursionSerialize(root)[1:]

    def getValue(self, s, sIndex):  # 处理超过10的数字，将数字字符转变为数字
        val = 0
        while ord(s[sIndex]) <= ord('9') and ord(s[sIndex]) >= ord('0'):
            val = val * 10 + int(s[sIndex])
            sIndex += 1
        return val, sIndex - 1

    def Deserialize(self, s):
        if self.sIndex < len(s):
            if s[self.sIndex] == ',':
                self.sIndex += 1
            if s[self.sIndex] == '$':
                return None
            val, self.sIndex = self.getValue(s, self.sIndex)
            treeNode = TreeNode(val)
            self.sIndex += 1
            treeNode.left = self.Deserialize(s)
            self.sIndex += 1
            treeNode.right = self.Deserialize(s)
            return treeNode


if __name__ == '__main__':
    r = Tree()
    r.construct_tree([5, 3, 6, 2, 4, None, 7, 1])
    series = Solution().Serialize(r.root)
    print(series)
