## O(nlogn)找逆序对

def merge_sort_count_inversions(arr,l,r):
    if l >= r:
        return 0
    mid = (l + r) // 2
    count = merge_sort_count_inversions(arr, l, mid) + merge_sort_count_inversions(arr, mid + 1, r)

    res = []
    i,j=l,mid+1
    while i <= mid and j<= r:
        if (arr[j] < arr[i]):
            count += (mid + 1 - i)
            res.append(arr[j])
            j += 1
        else:
            res.append(arr[i])
            i += 1
    while i <= mid:
        res.append(arr[i])
        i += 1
    while j <= r:
        res.append(arr[j])
        j += 1
    
    for k in range(len(res)):
        arr[l + k] = res[k]
    return count



if __name__ == '__main__':
    arr = [2,3,8,6,1]
    inversions = merge_sort_count_inversions(arr, 0, len(arr) - 1)
    print(f"逆序对的数量: {inversions}")  # 输出逆序对的数量
    print(f"排序后的数组: {arr}")  # 输出排序后的数组