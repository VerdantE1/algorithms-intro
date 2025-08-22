# 2.3-4 插入排序的递归实现

# 循环实现
def insert_sort(A):
    for i in range(1, len(A)):
        key = A[i]
        # 遍历子数组
        j = i-1
        while(j>=0 and A[j] >key):
            A[j+1] = A[j]
            j = j - 1
        A[j+1] = key # 插入到正确位置


def insert_sort_recursive(A, n=None):
    # 注意，此时我们处理的是A[0:n]，即前n个元素,A[0:n-1]是排序好的子数组
    if n is None:
        n = len(A)
    if n <= 1:
        return A
    insert_sort_recursive(A,n-1) # 排序A[0,n-1]
    i = n - 1
    key= A[i]
    j = i - 1
    while j>=0 and A[j] >= key:
        A[j+1] = A[j]
        j -= 1
    A[j+1] = key # 插入到正确位置 
    return A

# 测试
if __name__ == "__main__":
    A = [5, 2, 9, 1, 5, 6]
    print("原数组:", A)
    insert_sort_recursive(A)
    print("排序后:", A)