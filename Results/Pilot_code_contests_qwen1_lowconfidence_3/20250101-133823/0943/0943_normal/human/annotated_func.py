#State of the program right berfore the function call: i is an integer such that 0 <= i < H, where H is the number of elements in the binary heap and represents the heap size.
def func_1(i):
    return 2 * i + 1
    #The program returns an integer that is 2 times i plus 1, where i is an integer such that 0 <= i < H
#Overall this is what the function does:The function `func_1` accepts an integer `i` such that \(0 \leq i < H\), where \(H\) is the number of elements in a binary heap. It returns an integer that is calculated as \(2 \times i + 1\). There are no edge cases to consider beyond the given constraint on `i`. The function performs a simple arithmetic operation without any additional actions or validations.

#State of the program right berfore the function call: i is an integer such that 0 <= i < H - 1, where H is the number of elements in the binary heap and is given as input. The function assumes that the input list represents a max-heap except possibly for the subtree rooted at index i.
def func_2(i):
    return 2 * i + 2
    #The program returns 2 * i + 2, where i is an integer such that 0 <= i < H - 1
#Overall this is what the function does:The function `func_2` accepts an integer `i` as a parameter, where `0 <= i < H - 1`, and returns the value `2 * i + 2`. There are no additional actions performed beyond this calculation. This function does not modify any external state and only relies on the input `i` to compute its output. The function correctly implements the provided logic without any missing functionality or edge cases.

#State of the program right berfore the function call: i is an integer such that 1 <= i <= H, where H is the number of elements in the binary heap and represents the heap size.
def func_3(i):
    return int((i - 1) / 2)
    #The program returns the integer value of (i - 1) / 2, where i is an integer such that 1 <= i <= H, and H is the number of elements in the binary heap
#Overall this is what the function does:This function accepts an integer `i` such that \(1 \leq i \leq H\), where \(H\) is the number of elements in the binary heap. It returns the integer value of \((i - 1) / 2\). This calculation corresponds to finding the parent index of the node at position `i` in a zero-indexed binary heap representation. The function handles all valid inputs within the specified range, ensuring that the returned value is always a non-negative integer. There are no missing functionalities or edge cases in the provided code; the function correctly implements the required operation without any redundancies.

#State of the program right berfore the function call: array is a list of integers representing the initial state of the binary heap, i is an integer such that 1 <= i < item_num // 2 + 1, and item_num is a positive integer representing the number of elements in the heap.
def func_4(array, i, item_num):
    left = func_1(i)
    right = func_2(i)
    largest = i
    if (left < item_num and array[left] > array[largest]) :
        largest = left
    #State of the program after the if block has been executed: *`array` is a list of integers representing the initial state of the binary heap, `i` is an integer such that \(1 \leq i < \text{item\_num} // 2 + 1\), `left` is the index of the left child of the node at index `i`, and `item_num` is a positive integer representing the number of elements in the heap. If the left child of the node at index `i` exists and its value is greater than the value of the node at index `i`, then `largest` is set to `left`. Otherwise, `largest` remains unchanged.
    if (right < item_num and array[right] > array[largest]) :
        largest = right
    #State of the program after the if block has been executed: *`array` is a list of integers representing the initial state of the binary heap, `i` is an integer such that \(1 \leq i < \text{item\_num} // 2 + 1\), `left` is the index of the left child of the node at index `i`, `right` is the index of the right child of the node at index `i`, `item_num` is a positive integer representing the number of elements in the heap, and `largest` is the index of the largest element among the node at index `i`, its left child, and its right child (if it exists). If the right child exists and its value is greater than the value of the node at index `i`, then `largest` is set to `right`. Otherwise, `largest` remains unchanged.
    if (largest != i) :
        tmp = array[i]
        array[i] = array[largest]
        array[largest] = tmp
        func_4(array, largest, item_num)
    #State of the program after the if block has been executed: *`array` is a list of integers maintaining the max-heap property. If `largest` is not equal to `i`, the value at index `i` is swapped with the value at index `largest`, and `largest` may be different. `i` is an integer such that \(1 \leq i < \text{item\_num} // 2 + 1\), `left` is the index of the left child of the node at index `i`, `right` is the index of the right child of the node at index `i`, `item_num` is a positive integer representing the number of elements in the heap, and `tmp` is equal to `array[i]`.
#Overall this is what the function does:The function `func_4` accepts a list of integers `array`, an integer `i`, and a positive integer `item_num`. It ensures that the sub-tree rooted at index `i` satisfies the max-heap property. Specifically, it finds the largest element among the node at index `i`, its left child, and its right child (if they exist). If the largest element is not the node at index `i`, it swaps the values and recursively calls itself on the affected child node. After the recursive call, the function ensures that the entire sub-tree rooted at index `i` maintains the max-heap property. If `i` is out of bounds or if no valid children exist, no action is taken.

#State of the program right berfore the function call: size is a positive integer representing the number of elements in the array, and array is an iterable of integers representing the initial state of the binary heap.
def func_5():
    size = int(sys.stdin.readline().strip())
    array = map(lambda x: int(x), sys.stdin.readline().strip().split(' '))
    for i in reversed(range(0, func_3(size))):
        func_4(array, i, size)
        
    #State of the program after the  for loop has been executed: `size` is 5, `i` is 0, `func_4(array, i, size)` has been called with parameters `array`, `i`, and `size` for each index from `size-1` to 0.
#Overall this is what the function does:The function reads the size of a binary heap and its initial state from standard input, then calls `func_4` for each index from `size-1` to `0`. After executing the for loop, the binary heap is transformed such that each node is greater than or equal to its children (satisfying the max-heap property). The function does not accept any parameters and returns nothing. Note that the function assumes valid input where `size` is a positive integer and the array represents a valid binary heap structure before calling `func_4`. If the input does not meet these assumptions, the behavior of `func_4` could be undefined.

