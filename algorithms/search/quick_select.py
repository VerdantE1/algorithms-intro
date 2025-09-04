from random import randint

def partition(A,l,r):
    x = A[r]    
    i = l -1 
    for j in range(l,r):
        if A[j] > x:
            continue
        if A[j] <= x:
            A[i+1],A[j] = A[j],A[i+1]
            i = i + 1
    # 此时A[l...r-1]符合循环不变式,再处理A[r]
    A[i+1],A[r] = A[r],A[i+1]
    i = i + 1
    return i


def quick_select(A,l,r,i):
    if l == r:
        return A[l]
    pivot =randint(l,r)
    A[pivot],A[r] = A[r],A[pivot]
    q = partition(A,l,r)

    k = q - l + 1  # A[l...q]包含k个元素
    if i == k:
        return A[q]
    elif i < k:
        return quick_select(A,l,q-1,i)
    else:
        return quick_select(A,q+1,r,i-k)

# 循环不变量：每次循环开始时,A[i...j]中的第target个元素必定是A[l...r]中的第k个元素
def quick_select_loop(A,l,r,i):
    i,j,target = l,r,i

    while i <= j:
        pivot = randint(i,j)
        A[pivot],A[j] = A[j],A[pivot]
        q = partition(A,i,j)

        k = q - i + 1
        if k == target:
            return A[q]
        elif k < target:
            i = q + 1
            target = target - k
        else:
            j = q - 1
    

if __name__ == "__main__":
    A = [3,2,1,5,6,4]
    print(quick_select(A,0,len(A)-1,2))  # 2
    A = [3,2,3,1,2,4,5,5,6]
    print(quick_select(A,0,len(A)-1,4))  # 3

    # 迭代版本
    A = [3,2,1,5,6,4]
    print(quick_select_loop(A,0,len(A)-1,2))  # 2
    A = [3,2,3,1,2,4,5,5,6]
    print(quick_select_loop(A,0,len(A)-1,4))  # 3
