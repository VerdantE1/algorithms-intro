"""
better than关系是自反,非对称,传递的,所以它是偏序
又我们在line4中意味着对任意前i个元素与j进行比较,所以定义了所有比较次序
所以better than是一个全序
所以可以得到全部次序

"""


"""
def RANDOM(a,b):
    range = b-a
    bits = ceil(log(2,range))
    
    result = 0
    for i in range(0,bits):
        r = RANDOM(0,1)
        result = result + r<<i
    if result < range:
        return RANDOM(a,b)  # 重来一次
    else :
        return a + result

"""