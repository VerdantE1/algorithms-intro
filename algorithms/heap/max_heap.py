class max_Heap:
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

    def MAX_HEAPIFY(self,i):
        largest = i
        left = self.LEFT(i)
        right = self.RIGHT(i)

        if left < self.heapsize and self.A[left] > self.A[largest]:
            largest = left
        if right < self.heapsize and self.A[right] > self.A[largest]:
            largest = right
        if largest != i:
            self.A[i],self.A[largest] = self.A[largest],self.A[i]
            self.MAX_HEAPIFY(largest)

    def BUILD_MAX_HEAP(self,A):
        for i in range(self.heapsize//2,-1,-1):
            self.MAX_HEAPIFY(i)

    def HEAP_SORT(self):
        self.BUILD_MAX_HEAP(self.A)
        for i in range(self.heapsize-1,0,-1):
            self.A[0],self.A[i] = self.A[i],self.A[0]
            self.heapsize -= 1
            self.MAX_HEAPIFY(0)
        return self.A


if __name__ == "__main__":
    A = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    max_heap = max_Heap(A)
    print("Original array:", max_heap.A)
    print("Sorted array:", max_heap.HEAP_SORT())