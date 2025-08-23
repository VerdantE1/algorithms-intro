# c1 * n^2 = c2 * logn (c2>c1)
# c1 n = c2 *logn
# n/logn  = c2 / c1
# c1/c2(n/logn) = 1
# c1/c2看作k系数，意味着暴力的常数因子与递归的常数因子之比
# k(n/logn)  当比值为1/40,n大约70左右=1，之后整个函数单调递增,n永远大于logn