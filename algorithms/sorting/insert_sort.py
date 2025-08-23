# 循环不变式:每次循环后A[0..j]是排序好的

def insert_sort(A):
    for i in range(0,len(A)):
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
        return 
    insert_sort_recursive(A,n-1) # 排序A[0,n-1]
    i = n - 1
    key= A[i]
    j = i - 1
    while j>=0 and A[j] >= key:
        A[j+1] = A[j]
        j -= 1
    A[j+1] = key # 插入到正确位置 



if __name__ == '__main__':
    W = [5, 2, 9, 1, 5, 6]
    insert_sort_recursive(W)
    print(W)  # [1, 2, 5, 5, 6, 9])