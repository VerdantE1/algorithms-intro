def counting_sort(A,B,k):
    C = [0] * (k+1)
    for i in range(len(A)):
        C[A[i]] += 1
    for i in range(1,k+1):
        C[i] += C[i-1]       # C[i]此时为小于等于i的元素有多少个
    for j in range(len(A)-1,-1,-1):
        B[C[A[j]]-1] = A[j]  # C[i]-1表示i应该输出在哪个位置 (0-based)
        C[A[j]] -= 1

if __name__ == "__main__":
    A = [3,6,8,10,1,2,1]
    B = [0] * len(A)
    counting_sort(A,B,max(A))
    print(B)



