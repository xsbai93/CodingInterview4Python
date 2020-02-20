# coding=utf-8
"""
问题：二叉树的下一个节点
首先这道题给出的是中序遍历这个二叉树，那么就是左根右。我们在求一个结点的下一个结点，那么这个时候我们需要分情况讨论：
1、如果该结点有右子树，则该结点的下一个结点为该结点的右子树的最左结点。
2、如果该结点没有右子树，则又分两种情况讨论：
    情况一：如果该结点为该结点的父结点的左孩子，则该结点的父结点pNode.next则为下一个结点。
    情况二：如果该结点为该结点的父结点的右孩子，则该结点的父结点的父结点的父结点，直到其中的一个父结点是这个父结点的左孩子，则该父结点的父结点为下一个结点。
"""


def GetNext(pNode):
    """
    这里需要注意的是pNode.next是pNode结点的父结点
    1、如果有右子树，那么下一个结点就是右子树最左边的节点。
    2、如果没有右子树，分两种情况，如果该结点的为父结点的左孩子，则该结点的父节点pNode.next则为该结点的下一个结点。
    第二种情况则是如果该结点的为父节点的右孩子，则向上找父节点，直到父节点为该父节点的左孩子，则该父节点的父节点为下一个结点。

    """
    if not pNode:
            return None
        if not pNode.left and not pNode.right and not pNode.next:
            return None
        # 是否有右孩子
        if pNode.right:
            res = pNode.right
            while res.left:
                res = res.left
            return res
        # 如果没有右孩子但是有父节点
        while pNode.next:
            father = pNode.next
            if father.left == pNode:
                return father
            pNode = father
        return None


class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None



if __name__ == '__main__':
    TreeLink = TreeLinkNode()
    # 构建二叉树见ds4py.tree
    print(GetNext(pre, tin))
