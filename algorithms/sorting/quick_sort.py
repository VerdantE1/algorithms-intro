# 

# 划分三个子数组,以r为pivot
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


def quick_sort(A,l,r):
    if(l>=r):
        return 
    q = partition(A,l,r)  # 划分三个子数组.已经保证了A[q]在序列中
    quick_sort(A,l,q-1)
    quick_sort(A,q+1,r)


def quick_sort_random(A,l,r):
    if(l >= r):
        return 
    x = randint(l,r)
    A[x],A[r] = A[r],A[x]
    q = partition(A,l,r)
    quick_sort_random(A,l,q-1)
    quick_sort_random(A,q+1,r)


def fuzzy_interval_sorting(A,l,r):
    if (l>=r):
        return 
    x = randint(l,r)
    A[x],A[r] = A[r],A[x]
    pivot = A[r]

    i = l-1 
    for j in range(l,r):
        if (A[j][0] > pivot[1]):   # left
            continue
        if A[j][1] < pivot[0]:     # right
            i = i + 1
            A[i],A[j] = A[j],A[i]
        elif A[j][0] > A[r][1]:    # middle
            continue
    A[i+1],A[r] = A[r],A[i+1]

    fuzzy_interval_sorting(A,l,i)
    fuzzy_interval_sorting(A,i+2,r)



def fuzzy_interval_sorting_with_overlapping(A,l,r):
    if (l>=r):
        return 
    x = randint(l,r)
    A[x],A[r] = A[r],A[x]
    pivot = A[r]

    i = l-1 
    k = l-1 
    for j in range(l,r):
        if (A[j][0] > pivot[1]):   # right
            continue
        elif A[j][1] < pivot[0]:     # left
            i += 1 
            k += 1
            A[k],A[j] = A[j],A[k]
            A[i],A[k] = A[k],A[i]

        elif A[j][0] > A[r][1]:    # middle
            k +=1
            A[k],A[j] = A[j],A[k]

    A[k+1],A[r] = A[r],A[k+1]


    # 区间模糊比较关系是具有传递性的,所以可以不对middle排序
    fuzzy_interval_sorting(A,l,i)
    fuzzy_interval_sorting(A,k+2,r)


if __name__ == "__main__":
    A = [3,6,8,10,1,2,1]
    quick_sort(A,0,len(A)-1)
    print(A)

    B = [3,6,8,10,1,2,1]
    quick_sort_random(B,0,len(B)-1)
    print(B)

    C = [[1,4],[2,5],[6,8],[9,9],[3,6]]
    fuzzy_interval_sorting(C, 0, len(C) - 1)
    print(C)

    C = [[1,4],[2,5],[6,8],[9,9],[3,6]]
    fuzzy_interval_sorting_with_overlapping(C, 0, len(C) - 1)
    print(C)