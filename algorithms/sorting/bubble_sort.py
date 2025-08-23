
# 循环不变量从空集开始
def bubble_sort(A,l,r):
    for i in range(l,r):  # 确定第i个元素的位置
        for j in range(r,i,-1):
            if A[j] < A[j-1]:
                A[j],A[j-1] = A[j-1],A[j]   # 交换位置
            else:
                continue

def bubble_sort_recursive(A, l, r):
    if l >= r:
        return
    # 每次递归，把A[l...r]区间的最大值“冒泡”到A[r]
    for j in range(l, r):
        if A[j] > A[j+1]:
            A[j], A[j+1] = A[j+1], A[j]
    bubble_sort_recursive(A, l, r-1)

if __name__ == "__main__":
    W = [5, 2, 9, 1, 5, 6]
    bubble_sort_recursive(W, 0, len(W) - 1)
    print(W)  # 输出排序后的数组