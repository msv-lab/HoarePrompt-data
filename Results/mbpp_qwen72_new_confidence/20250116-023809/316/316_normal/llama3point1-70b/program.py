def check_min_heap(heap):
    for i in range(len(heap)):
        left_child = 2 * i + 1
        right_child = 2 * i + 2
        if left_child < len(heap) and heap[i] > heap[left_child]:
            return False
        if right_child < len(heap) and heap[i] > heap[right_child]:
            return False
    return True