# Challenge: Find k Smallest Elements in a List
from MinHeap import MinHeap


def findKSmallest(lst, k):
    # Write your code here
    min_heap = MinHeap()
    for element in lst:
        min_heap.insert(element)
    answer = []
    while k:
        answer.append(min_heap.removeMin())
        k -= 1
    return answer


lst = [9, 4, 7, 1, -2, 6, 5]
k = 3
print(findKSmallest(lst, k))
