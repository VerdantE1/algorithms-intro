"""
输入:k个升序链表的头节点列表
输出:合并后的升序链表的头节点
"""

## 贪心法

from listNode import ListNode,build_list,print_list
import heapq

# lists=[链表1的头结点,链表2的头结点,...,链表k的头结点]
def mergeKLists(lists):
    min_heap = []
    for idx,node in enumerate(lists):
        if node:
            heapq.heappush(min_heap,(node.val,idx,node))   # 堆中存储(节点值,链表索引,节点)
    
    # 此时堆中已经维护了所有链表的头结点,开始归并
    dummy = ListNode(-1)
    current = dummy

    while min_heap:
        val, idx, node = heapq.heappop(min_heap)
        current.next = node
        current = current.next

        if node.next:
            heapq.heappush(min_heap,(node.next.val,idx,node.next))
    
    return dummy.next 




## 分治法
def mergeKLists_divide_and_conquer(lists):
    if not lists:
        return None
    if len(lists)==1:
        return lists[0]

    dummy = ListNode(-1)
    current = dummy

    mid = len(lists) // 2
    Llist = mergeKLists_divide_and_conquer(lists[0:mid])
    Rlist = mergeKLists_divide_and_conquer(lists[mid:len(lists)])    

    l,r = Llist,Rlist
    while(l and r):
        if(l.val <= r.val):
            current.next, l = l, l.next
        else:
            current.next, r = r, r.next
    current.next = l or r 
    return dummy.next


if __name__ == "__main__":
    # 测试合并K个升序链表
    lists = [
        build_list([1, 4, 5]),
        build_list([1, 3, 4]),
        build_list([2, 6])
    ]
    # merged_head = mergeKLists(lists)
    merged_head = mergeKLists_divide_and_conquer(lists)
    print("Merged linked list:")
    print_list(merged_head)
