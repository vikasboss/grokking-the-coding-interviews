# Challenge: Find k Largest Elements in a List
from MaxHeaps import MaxHeap


def findKLargest(lst, k):
    # Write your code here
    max_heap = MaxHeap()
    for element in lst:
        max_heap.insert(element)
    answer = []
    while k:
        answer.append(max_heap.removeMax())
        k -= 1
    return answer


lst = [9, 4, 7, 1, -2, 6, 5]
k = 3
print(findKLargest(lst, k))
