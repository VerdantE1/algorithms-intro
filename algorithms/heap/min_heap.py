class min_Heap:
    def __init__(self,A):
        self.A = A
        self.heapsize = len(A)

    @staticmethod
    def LEFT(i):
        return 2*i + 1

    @staticmethod

    def RIGHT(i):
        return 2*i + 2
    
    @staticmethod
    def PARENT(i):
        return (i-1)//2
    
    # 假定i可能会影响最小根堆性质,同时以LEFT(i)或RIGHT(i)为根的子树均为最小根堆
    def MIN_HEAPIFY(self,i):
        smallest = i
        left = self.LEFT(i)
        right = self.RIGHT(i)

        if left < self.heapsize and self.A[left] < self.A[smallest]:
            smallest = left
        if right < self.heapsize and self.A[right] < self.A[smallest]:
            smallest = right
        if smallest != i:
            self.A[i],self.A[smallest] = self.A[smallest],self.A[i]
            self.MIN_HEAPIFY(smallest)
    
    # 依靠MIN_HEAPIFY自底向上增量法建堆.使用MIN_HEAPIFY保证左孩子右孩子均为堆结构
    def BUILD_MIN_HEAP(self,A):
        # 显然,[i//2+1,len(A))均是叶子结点，符合堆定义，故只用建立从heapsize//2...1依次建立
        for i in range(self.heapsize//2,-1,-1):
            self.MIN_HEAPIFY(i)

    def HEAP_SORT(self):
        self.BUILD_MIN_HEAP(self.A)
        for i in range(self.heapsize-1,0,-1):
            self.A[0],self.A[i] = self.A[i],self.A[0]
            self.heapsize -= 1
            self.MIN_HEAPIFY(0)
        return self.A
