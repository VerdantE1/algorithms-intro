def linear_search(A,l,r,key):
    for i in range(l,r+1):
        if A[i] == key:
            return i 
    return -1


def linear_search_recursive(A,l,r,key):
    if l>r:
        return -1
    if A[l] == key:
        return l
    return linear_search_recursive(A,l+1,r,key)


if __name__ == "__main__":
    A = [5,2,9,1,5,6]
    key = 9
    index = linear_search(A,0,len(A)-1,key)
    print(f"元素{key}的索引为:{index}")  # 元素5的索引为:0

    index = linear_search_recursive(A,0,len(A)-1,key)
    print(f"元素{key}的索引为:{index}")  # 元素5的索引为:0