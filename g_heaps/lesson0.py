# Challenge: Convert Max-Heap to Min-Heap
def minHeapify(heap, index):
    left = (index * 2) + 1
    right = (index * 2) + 2
    smallest = index
    if len(heap) > left and heap[smallest] > heap[left]:
        smallest = left
    if len(heap) > right and heap[smallest] > heap[right]:
        smallest = right
    if smallest != index:
        tmp = heap[smallest]
        heap[smallest] = heap[index]
        heap[index] = tmp
        minHeapify(heap, smallest)
    return heap


def convertMax(maxHeap):
    # iterate from middle to first element
    # middle to first indices contain all parent nodes
    for i in range((len(maxHeap))//2, -1, -1):
        # call minHeapify on all parent nodes
        maxHeap = minHeapify(maxHeap, i)
    return maxHeap


if __name__ == '__main__':
    maxHeap = [9, 4, 7, 1, -2, 6, 5]
    print(convertMax(maxHeap))
