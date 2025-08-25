from max_heap import max_Heap

class maxPriority_Queue:
    def __init__(self,A):
        self.heap = max_Heap(A)
        self.heap.BUILD_MAX_HEAP(A)
    
    # 找到最大元素
    def MAXIMUM(self):
       if self.heap.heapsize < 1:
           raise Exception("heap underflow")
       return self.heap.A[0]

    # 提取最大元素
    def EXTRACT_MAX(self):
        if self.heap.heapsize < 1:
            raise Exception("heap underflow")
        max_elem = self.heap.A[0]
        self.heap.A[0] = self.heap.A[self.heap.heapsize - 1]
        self.heap.heapsize -= 1
        self.heap.MAX_HEAPIFY(0)
        return max_elem


    # 增大关键字
    def INCREASE_KEY(self,i,key):
        if key < self.heap.A[i]:
            raise Exception("new key is smaller than current key")
        self.heap.A[i] = key
        while(i > 0 and self.heap.A[i] > self.heap.A[self.heap.PARENT(i)]):
            self.heap.A[i],self.heap.A[self.heap.PARENT(i)] = self.heap.A[self.heap.PARENT(i)],self.heap.A[i]
            i = self.heap.PARENT(i)
        

    # 插入元素
    def INSERT(self,key):
        self.heap.heapsize += 1
        self.heap.A.append(float('-inf')) # 先插入一个极小值不影响堆性质
        self.INCREASE_KEY(self.heap.heapsize - 1,key)

    # 删除元素
    def DELETE(self,i):
        self.heap.A[i] = self.heap.A[self.heap.heapsize - 1]
        self.heap.heapsize -= 1

        # 若被删除节点的值大于父节点的值,则上浮
        if self.heap.A[i] > self.heap.A[self.heap.PARENT(i)]:
            self.INCREASE_KEY(i,self.heap.A[i])
        else:
            self.heap.MAX_HEAPIFY(i)

if __name__ == "__main__":
    pq = maxPriority_Queue([3, 1, 4, 1, 5, 9])
    print(pq.MAXIMUM())  # 9
    print(pq.EXTRACT_MAX())  # 9
    pq.INSERT(6)
    print(pq.MAXIMUM())  # 6