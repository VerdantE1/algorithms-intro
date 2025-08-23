# 暴力解法 O(n^2)
def max_sub_array_sum_brute_force(arr):
    max_sum = float('-inf')
    for i in range(len(arr)):
        cur_sum = 0
        for j in range(i,len(arr)):
            cur_sum += arr[j]
            max_sum = max(max_sum,cur_sum)
    return max_sum


if __name__ == "__main__":
    arr = [-2,1,-3,4,-1,2,1,-5,4]
    max_sum_brute = max_sub_array_sum_brute_force(arr)
    print("Max sub array sum is:",max_sum_brute)
