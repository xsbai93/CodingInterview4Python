# coding=utf-8
"""
数据流中的中位数
"""
import heapq
class MedianFinder:

    def __init__(self):
        # 初始化大顶堆和小顶堆
        self.max_heap = []
        self.min_heap = []

    def addNum(self, num):
        if len(self.max_heap) == len(self.min_heap):# 先加到大顶堆，再把大堆顶元素加到小顶堆
            heapq.heappush(self.min_heap, -heapq.heappushpop(self.max_heap, -num))
        else:  # 先加到小顶堆，再把小堆顶元素加到大顶堆
            heapq.heappush(self.max_heap, -heapq.heappushpop(self.min_heap, num))

    def findMedian(self):
        if len(self.min_heap) == len(self.max_heap):
            return (-self.max_heap[0] + self.min_heap[0]) / 2
        else:
            return self.min_heap[0]

if __name__ == '__main__':
    m = MedianFinder()
    test = [1, 2, -2, 3, 6, 0, -2]
    for i in test:
        m.addNum(i)
    print(m.findMedian())
