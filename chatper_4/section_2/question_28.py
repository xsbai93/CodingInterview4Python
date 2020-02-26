# coding=utf-8
"""
对称的二叉树
如果一棵二叉树和它的镜像一样，那么它是对称的。对于一棵二叉树 t1 和它的镜像 t2 有如下特点：

根节点相同
t1 左子树等于 t2 的右子树
t2 左子树等于 t1 的右子树
因此我们递归调用判断以上三点是否满足即可。
"""
from collections import deque


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Tree(object):
    def __init__(self):
        self.root = None

    def construct_tree(self, values=None):
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


def isSymmetric(root) :
    def isMirror(t1, t2):
        if not t1 and not t2: return True # 如果都为空，则是对称的
        if not t1 or not t2: return False # 如果其中一个为空另一个不是，则不是对称的
        return t1.val == t2.val and isMirror(t1.right,t2.left) and isMirror(t1.left,t2.right)

    return isMirror(root,root)




if __name__ == '__main__':
    t = Tree()
    t.construct_tree([1, 2, 2, 5, 3, 3, 5])
    print(t.bfs())
    print(isSymmetric(t.root))
