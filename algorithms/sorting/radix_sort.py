def radix_sort(A):
    def counting_sort(A, exp):
        B = [0] * len(A)
        C = [0] * 10
        for i in range(len(A)):
            index = (A[i] // exp) % 10
            C[index] += 1

        for i in range(1,10):
            C[i] += C[i-1]
        
        for i in range(len(A)-1,-1,-1):
            index = (A[i]//exp) %10
            B[C[index]-1] = A[i]
            C[index] -= 1
        
        for i in range(len(A)):
            A[i] = B[i]

    max1 = max(A)
    exp = 1
    while max1 // exp > 0:  # 当整除后大于0说明还可以表示
        counting_sort(A,exp)
        exp *= 10

if __name__ == "__main__":
    A = [170, 45, 75, 90, 802, 24, 2, 66]
    radix_sort(A)
    print("Sorted array is:", A)