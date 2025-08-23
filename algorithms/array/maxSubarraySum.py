'''
该问题是最大子数组之和，所以要找所有可能的子数组和。
解空间划分：
    一个数组的连续子数组可能在：
    1.完全落在左子数组区间内
    2.完全落在右子数组区间内
    3.以中点为跨界点，跨越左右子数组
'''

# 暴力解法 O(n^2)
def max_sub_array_sum_brute_force(arr):
    max_sum = float('-inf')
    for i in range(len(arr)):
        cur_sum = 0
        for j in range(i,len(arr)):
            cur_sum += arr[j]
            max_sum = max(max_sum,cur_sum)
    return max_sum


# 分治法 O(nlogn)
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
        return arr[l]

    mid = (l+r)//2
    larraySum = max_sub_array_sum(arr,l,mid)
    rarraySum = max_sub_array_sum(arr,mid+1,r)

    crossSum = max_cross_sum(arr,l,mid,r)
    return max(larraySum,rarraySum,crossSum)


# kadane
def max_sub_array_sum_kadane(arr):
    maxSum = arr[0] # 表示已经扩展过的A[0..i]的最大子数组和
    endHere = arr[0] # 当扩展新一个j+1时,若最大子数组和不是A[0..i]说明A[j+1]改变了最大子数组和。那么其情况是A[j+1]或以j为结尾的最大子数组和endhere[j] + A[j+1]

    for i in range(1,len(arr)):
        endHere = max(arr[i],endHere + arr[i])
        maxSum = max(maxSum,endHere)
    return maxSum 



if __name__ == "__main__":
    arr = [-2,1,-3,4,-1,2,1,-5,4]
    max_sum = max_sub_array_sum(arr,0,len(arr)-1)
    max_sum_brute = max_sub_array_sum_brute_force(arr)
    max_sum_kadane = max_sub_array_sum_kadane(arr)
    print("Max sub array sum is:",max_sum)
    print("Max sub array sum by brute force is:",max_sum_brute)
    print("Max sub array sum by kadane is:",max_sum_kadane)