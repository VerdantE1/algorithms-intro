# 允许空数组存在版本
def max_cross_sum(arr,l,mid,r):
    left_sum = float('-inf')
    right_sum = float('-inf')

    cross_sum = 0
    for i in range(mid,l-1,-1):
        cross_sum += arr[i]
        left_sum = max(left_sum,cross_sum)
    
    cross_sum = 0
    for i in range(mid+1,r+1):
        cross_sum += arr[i]
        right_sum = max(right_sum,cross_sum)
    return left_sum + right_sum

def max_sub_array_sum(arr,l,r):
    if(l>r):
        return 0
    if(l==r):
        return max(0,arr[l])

    mid = (l+r)//2
    larraySum = max_sub_array_sum(arr,l,mid)
    rarraySum = max_sub_array_sum(arr,mid+1,r)

    crossSum = max_cross_sum(arr,l,mid,r)
    return max(larraySum,rarraySum,crossSum,0)


if __name__ == "__main__":
    arr = [-2,1,-3,4,-1,2,1,-5,4]
    print(max_sub_array_sum(arr,0,len(arr)-1))

    arr = [-1,-2,-3,-4,-5]
    print(max_sub_array_sum(arr,0,len(arr)-1))