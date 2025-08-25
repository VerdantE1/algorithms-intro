from min_heap import min_Heap

class minPriority_Queue:
    def __init__(self,A):
        self.heap = min_Heap(A)
        self.heap.BUILD_MIN_HEAP(A)
    
    def MINIMUM(self):
        return self.heap.A[0] if self.heap.heapsize > 0 else Exception("heap underflow")    

    def EXTRACT_MIN(self):
        min_elem = self.heap.A[0]
        self.heap.A[0] = self.heap.A[self.heap.heapsize - 1]
        self.heap.heapsize -= 1
        self.heap.MIN_HEAPIFY(0)
        return min_elem
    
    def DECREASE_KEY(self,i,key):
        if key > self.heap.A[i]:
            raise Exception("new key is larger than current key")
        self.heap.A[i] = key
        while(i > 0 and self.heap.A[i] < self.heap.A[self.heap.PARENT(i)]):
            self.heap.A[i],self.heap.A[self.heap.PARENT(i)] = self.heap.A[self.heap.PARENT(i)],self.heap.A[i]
            i = self.heap.PARENT(i)
    
    def INSERT(self,key):
        self.heap.heapsize += 1
        self.heap.A.append(float('inf')) # 先插入一个极大值 in order to pass the guard clause
        self.DECREASE_KEY(self.heap.heapsize - 1,key)

    def DELETE(self,i):
        self.heap.A[i] = self.heap.A[self.heap.heapsize - 1]
        self.heap.heapsize -= 1
        self.heap.MIN_HEAPIFY(i)
        

if __name__ == "__main__": 
    pq = minPriority_Queue([3, 1, 4, 1, 5, 9, 2, 6, 5])
    print(pq.MINIMUM())  # 1
    print(pq.EXTRACT_MIN())  # 1
    pq.INSERT(0)
    print(pq.MINIMUM())  # 0