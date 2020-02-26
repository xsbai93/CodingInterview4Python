# coding=utf-8
"""
链表中环的入口结点
一个链表中包含环，请找出该链表的环的入口结点
"""


def EntryNodeOfLoop(pHead):
    if not pHead or not pHead.next or not pHead.next.next:
        return None
    slow = pHead.next
    fast = slow.next
    # 找到相遇点
    while fast != slow and fast.next:
        slow = slow.next
        fast = fast.next.next
    if slow == fast:
        # 慢指针回到表头，快指针留在相遇点，二者同步往前直到相遇在入口结点
        slow = pHead
        while slow != fast:
            fast = fast.next
            slow = slow.next
        return slow
    return None

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


if __name__ == '__main__':
    
    a,b,c,d,e,f,g = ListNode(1),ListNode(2),ListNode(3),ListNode(4),ListNode(5), ListNode(6),ListNode(7)
    a.next, b.next,c.next,d.next ,e.next,f.next = b,c,d,e,f,c
    linkhead = a
    print(EntryNodeOfLoop(linkhead).val)
