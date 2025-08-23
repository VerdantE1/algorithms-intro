# 二分查找递归定义:在数组A[l:r]中查找key
def binary_search_recursive(A,l,r,key):
    if l > r:
        return -1
    mid = (l+r) // 2
    if A[mid] == key:
        return mid
    elif A[mid] > key:
        return binary_search_recursive(A,l,mid-1,key)
    else:
        return binary_search_recursive(A,mid+1,r,key)
    

def binary_search(A,l,r,key):
    while l<=r:
        mid = (l+r) //2
        if A[mid] == key:
            return mid
        elif A[mid] > key:
            r = mid - 1
        else:
            l = mid + 1

if __name__ == "__main__":
    A = [1,2,3,4,5,6,7,8,9]
    key = 5
    index = binary_search_recursive(A,0,len(A)-1,key)
    print(f"元素{key}的索引为:{index}")  # 元素5的索引为:4

    index = binary_search(A,0,len(A)-1,key)
    print(f"元素{key}的索引为:{index}")  # 元素5的索引为:4