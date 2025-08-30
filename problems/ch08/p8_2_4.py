
def counting_num_intervals(A,k,a,b):
    C = [0] * (k+1)  # C[0...k]
    for i in range(len(A)):
        C[A[i]] += 1   # C[i]:i在A中的频数
    for i in range(1,k+1):
        C[i] += C[i-1]  # C[i]:A中有多少个数<=i
    return C[b] - C[a-1] if a > 0 else C[b]

if __name__ == "__main__":
    A = [1,4,1,2,7,5,2]
    print(counting_num_intervals(A,max(A),1,5))