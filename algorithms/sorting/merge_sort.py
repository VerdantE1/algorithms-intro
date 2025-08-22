"""
容易犯错的地方：
    Python没有const，无法固定l,r的改变，而l,r在逻辑上指的是数组范围，是不可改变的。
"""
def merge_sort(A:list,l,r):
    if l >= r:   # 非数组与只有一个
        return

    mid = (l+r) // 2
    merge_sort(A, l, mid)
    merge_sort(A,mid+1,r) # 处理右半部分

    result = []
    i,j = l,mid+1   # 一定不能改变l,r.要显式的创造指针
    while i<=mid and j <=r:
        if A[i] <= A[j]:
            result.append(A[i])
            i +=1
        else:
            result.append(A[j])
            j +=1
    while i<=mid:
        result.append(A[i])
        i+=1
    while j <= r:
        result.append(A[j])
        j+=1

    for k in range(0,len(result)):
        A[l+k] = result[k]



## Merge Sort Implementation
if __name__ == '__main__':
    W = [5, 2, 9, 1, 5, 6]
    sorted_W = merge_sort(W, 0, len(W) - 1)
    print(W)
