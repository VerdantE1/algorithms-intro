# Definition for singly-linked list.
class ListNode:
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next


def build_list(arr):
    dummy = ListNode(0)
    current = dummy
    for x in arr:
        current.next = ListNode(x)
        current = current.next

    return dummy.next

def print_list(node):
    res = []
    current = node 
    while current:
        res.append(current.val)
        current = current.next
    print(res)

if __name__ == "__main__":
    # 测试构建链表
    arr = [1, 2, 3, 4, 5]
    head = build_list(arr)
    print("Built linked list:")
    print_list(head)