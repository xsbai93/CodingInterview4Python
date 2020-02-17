# coding=utf-8
"""
问题：从尾到头打印链表
方法1:用一个list把链表中的元素依次压入，然后对链表进行翻转。
方法2.考虑栈的特性：先进后出
方法3.递归，依次滑动链表指针，让最前的元素保持在最后。
"""

def printListFromTailToHead1(listNode):
    if not listNode:
        return []
    result=[]
    while listNode:
        result.append(listNode.val)
        listNode=listNode.next
    result.reverse()
    return result


def printListFromTailToHead2(listNode):
    if not listNode:
        return []
    res=[]
    result=[]
    while listNode:
        res.append(listNode.val)
        listNode=listNode.next
    while res:
        result.append(res.pop())
    return result


def printListFromTailToHead3(listNode):
    if not listNode:
        return []
    return printListFromTailToHead3(listNode.next)+[listNode.val]
    
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
#定义链表
class LinkList:
    def __init__(self):
        self.head=None
 
    def initList(self, data):
        # 创建头结点
        self.head = ListNode(data[0])
        r=self.head
        p = self.head
        # 逐个为 data 内的数据创建结点, 建立链表
        for i in data[1:]:
            node = ListNode(i)
            p.next = node
            p = p.next
        return r

    def printlist(self,head):
        if head == None: return
        node = head
        while node != None :
            print(node.val,end=' ')
            node = node.next


if __name__ == '__main__':
    l=[1, 2, 3, 4]
    link=LinkList()
    l=link.initList(l)
    print(printListFromTailToHead1(l))
    print(printListFromTailToHead2(l))
    print(printListFromTailToHead3(l))
