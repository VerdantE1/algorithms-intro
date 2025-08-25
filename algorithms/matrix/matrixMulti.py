## 矩阵乘法算法

## 暴力法 O(n^3)
def matrix_multiply_brute_force(A,B):
    n = len(A)
    C = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]
    return C

## 简单分治法
def get_sub_matrix(M, row_start, row_end, col_start, col_end):
    return [row[col_start:col_end] for row in M[row_start:row_end]]


def add_matrix(A, B):
    return [[a + b for a, b in zip(rowA, rowB)] for rowA, rowB in zip(A, B)]

def matrix_multiply_divide_and_conquer(A, B):
    n = len(A)
    if n == 0: return []
    if len(A) == 1 and len(A[0]) == 1:
        return [[A[0][0] * B[0][0]]]

    mid = n // 2

    A11 = get_sub_matrix(A, 0, mid, 0, mid)
    A12 = get_sub_matrix(A, 0, mid, mid, n)
    A21 = get_sub_matrix(A, mid, n, 0, mid)
    A22 = get_sub_matrix(A, mid, n, mid, n)

    B11 = get_sub_matrix(B, 0, mid, 0, mid)
    B12 = get_sub_matrix(B, 0, mid, mid, n)
    B21 = get_sub_matrix(B, mid, n, 0, mid)
    B22 = get_sub_matrix(B, mid, n, mid, n)

    C11 = add_matrix(matrix_multiply_divide_and_conquer(A11, B11),
                     matrix_multiply_divide_and_conquer(A12, B21))
    C12 = add_matrix(matrix_multiply_divide_and_conquer(A11, B12),
                     matrix_multiply_divide_and_conquer(A12, B22))
    C21 = add_matrix(matrix_multiply_divide_and_conquer(A21, B11),
                     matrix_multiply_divide_and_conquer(A22, B21))
    C22 = add_matrix(matrix_multiply_divide_and_conquer(A21, B12),
                     matrix_multiply_divide_and_conquer(A22, B22))

    top = [row1 + row2 for row1, row2 in zip(C11, C12)]
    bottom = [row1 + row2 for row1, row2 in zip(C21, C22)]
    return top + bottom

if __name__ == "__main__":
    A = [[1,2,3,4],[4,5,6,7],[7,8,9,10]]
    B = [[9,8,7,6],[6,5,4,3],[3,2,1,0]]
    print(f"Matrix A:{A}")
    print(f"Matrix B:{B}")
    print(f"Matrix C:{matrix_multiply_brute_force(A,B)}")
    print(f"Matrix C by divide and conquer:{matrix_multiply_divide_and_conquer(A,B)}")