# coding=utf-8
"""
平衡二叉树
输入一棵二叉树的根节点，判断该树是不是平衡二叉树
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


def bfs(tree):
    if not tree:
        return None
    stack = [tree]
    ret = []
    while stack:
        node = stack.pop(0)
        ret.append(node.val)
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
    return ret

def maxDepth(root):
    return 0 if(root == None) else (max(maxDepth(root.left), maxDepth(root.right)) + 1)

def isBalanced(root):
    return True if(root == None) else ((isBalanced(root.left) and isBalanced(root.right)) if(abs(maxDepth(root.left) - maxDepth(root.right)) <= 1) else False)

if __name__ == '__main__':
    t = Tree()
    t.construct_tree([3,9,20,None,None,15,7])
    print(t.bfs())
    print(isBalanced(t.root))
