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
    max_sum_kadane = max_sub_array_sum_kadane(arr)
    print("Max sub array sum by kadane is:",max_sum_kadane)