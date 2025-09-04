import heapq
from collections import defaultdict
class MedianHeap:
    def __init__(self):
        self.smallest_heap = [] # 小顶堆
        self.largest_heap = [] # 大顶堆
        self.smallest_size = 0
        self.largest_size = 0
        self.median = None
        self.delayed = defaultdict(int) # 记录延迟删除的元素及其频次

    def prune(self,heap):
        while heap:
            value = heap[0] if heap is self.smallest_heap else -heap[0]
            if self.delayed[value] > 0:
                heapq.heappop(heap)
                self.delayed[value] -= 1
                if self.delayed[value] == 0:
                    del self.delayed[value]
            else:
                break
        
    def rebalance(self):
        if self.smallest_size - self.largest_size > 1:
            value = heapq.heappop(self.smallest_heap)
            self.smallest_size -= 1
            heapq.heappush(self.largest_heap,-value)
            self.largest_size += 1
            self.prune(self.smallest_heap)
        elif self.smallest_size - self.largest_size < 0:
            value = -heapq.heappop(self.largest_heap)
            self.largest_size -= 1
            heapq.heappush(self.smallest_heap,value)
            self.smallest_size += 1
            self.prune(self.largest_heap)
        
        # 更新中位数
        self.update_median()

    def update_median(self):
        if self.smallest_size > self.largest_size:
            self.median = self.smallest_heap[0]
        else:
            self.median = (self.smallest_heap[0] - self.largest_heap[0]) / 2

    def insert(self,num):
        if self.median is None:
            heapq.heappush(self.smallest_heap,num)
            self.smallest_size += 1
            self.median = num
            return

        if num >= self.median:
            heapq.heappush(self.smallest_heap,num)
            self.smallest_size += 1
        else:
            heapq.heappush(self.largest_heap,-num)
            self.largest_size += 1

        # 插入后可能会违反平衡条件
        self.rebalance()
        


    def remove(self,num):
        self.delayed[num] += 1
        if num >= self.median:
            self.smallest_size -= 1
            if num == self.smallest_heap[0]:
                self.prune(self.smallest_heap)
        else:
            self.largest_size -= 1
            if num == -self.largest_heap[0]:
                self.prune(self.largest_heap)
                
        self.rebalance()

    def query(self):
        return self.median
    
    
if __name__ == "__main__":
    median_heap = MedianHeap()
    nums = [1,3,-1,-3,5,3,6,7]
    for num in nums:
        median_heap.insert(num)
        print(f"插入元素{num}后中位数为:{median_heap.query()}")
