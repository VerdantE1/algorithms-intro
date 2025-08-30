## 此文件用于测试 STL 中的堆实现

import heapq


def heap_sort(iterable):
    h=[]
    for i in iterable:
        heapq.heappush(h,i)
    return [heapq.heappop(h) for _ in range(len(h))]

if __name__ == "__main__":
    A = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    heapq.heapify(A)
    print("Heapified array:", A)

    A = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    sorted_A = heap_sort(A)
    print("Sorted array:", sorted_A)