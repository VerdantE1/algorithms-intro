# 给定n个整数的集合S和另外一个整数x,该算法能否确定S中是否存在两个其和刚好为x的元素

# 增量法
# 循环不变式：S[0...i]是没有与后续元素中形成和为x的序列

# 证明循环不变式
'''
循环初始时:S是空集,符合循环不变式
循环每次迭代时：S[0...i-1]是没有与后续元素中形成和为x的序列,
               对于A[i]，如果存在A[i]与S[0...i-1]中某个元素的和为x，
               则find(A, i+1, r, x - A[i])返回True，否则将A[i]加入S中
               S[0...i]仍然是没有与后续元素中形成和为x的序列
循环结束时：S[0...n-1]是没有与后续元素中形成和为x的序列
所以循环不变式成立
'''

# 算法伪代码
'''
 for i to n 
    key = A[i]
    if(find(A,i+1,r,x-A[i])):
        return true
    else 
        S.append(A[i])
        continue;
'''
import sys
sys.path.append(r'c:\dev\algorithms-intro')

from algorithms.search.binary_search import binary_search

def find(A,l,r,key):
    return binary_search(A, l, r, key)

def find_two_sum_x(A,l,r,x):
    S =[]
    for i in range(l,r+1):
        key = A[i]
        if (find(A, i+1, r, x - A[i]) != -1):
            return True
        else:
            S.append(A[i])
            continue
    return False


if __name__ == "__main__":
    A = [1, 2, 3, 4, 5]
    x = 9
    result = find_two_sum_x(A, 0, len(A) - 1, x)
    print(f"是否存在两个元素的和为{x}: {result}")