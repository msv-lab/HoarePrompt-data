#State of the program right berfore the function call: n is a positive integer such that 2 <= n <= 40, k is a positive integer such that 1 <= k <= 2n, and n and k are the parameters that define the size of the graph and the condition for adding edges between vertices.
def func_1(n, k):
    cliques = ceil(n / k)
    arr = [0] * n
    cliquess = [0] * n
    for i in range(cliques):
        make_array(i * k, min((i + 1) * k - 1, n - 1), i + 1)
        
    #State: - After the loop, the list `arr` will be divided into `cliques` segments.
    #   - Each segment will contain the value `i + 1` where `i` is the index of the segment.
    #   - The list `cliquess` remains unchanged as it is not modified by the loop.
    #
    #Therefore, the output state after the loop executes all iterations is:
    #
    #Output State:
    print(*arr)
    #This is printed: 1 1 1 2 2 3 (where the elements are the values of the segments as described by the initial state)
    print(cliques)
    #This is printed: cliques (where cliques is the original list of segments before the loop)
    print(*cliquess)
    #This is printed: elements of `cliquess` (where `cliquess` is the unchanged list of elements)
#Overall this is what the function does:The function `func_1` accepts two parameters, `n` and `k`, where `n` is a positive integer between 2 and 40, and `k` is a positive integer between 1 and 2n. It divides the list `arr` into `cliques` segments, where each segment contains the same value corresponding to its segment index. The function prints the elements of `arr`, the number of cliques, and the elements of `cliquess` (which remains unchanged). The function does not return any value.

#State of the program right berfore the function call: left and right are non-negative integers such that left <= right and (right - left + 1) is the number of elements to be assigned in the array arr. clique is an integer representing the clique number to be assigned to the elements in the range [left, right] in the cliquess array. arr and cliquess are lists of integers with at least (right - left + 1) elements each.
def make_array(left, right, clique):
    small_element = left + 1
    big_element = right + 1
    mid = (big_element - small_element) // 2
    not_mid = right - left + 1 - mid
    for i in range(mid):
        arr[left + i] = small_element + i
        
        cliquess[left + i] = clique
        
    #State: The elements in the range `[left, left + mid - 1]` of the `arr` list are assigned values from `small_element` to `small_element + mid - 1` respectively. The elements in the same range of the `cliquess` list are all assigned the value `clique`. The variables `left`, `right`, `clique`, `small_element`, `big_element`, `mid`, and `not_mid` remain unchanged.
    for i in range(not_mid):
        arr[left + mid + i] = big_element - i
        
        cliquess[left + mid + i] = clique
        
    #State: Output State: The elements in the range `[left, left + mid - 1]` of the `arr` list are assigned values from `small_element` to `small_element + mid - 1` respectively. The elements in the range `[left + mid, left + mid + not_mid - 1]` of the `arr` list are assigned values from `big_element - not_mid + 1` to `big_element` respectively. The elements in the same range of the `cliquess` list are all assigned the value `clique`. The variables `left`, `right`, `clique`, `small_element`, `big_element`, `mid`, and `not_mid` remain unchanged.
#Overall this is what the function does:The function `make_array` accepts three parameters: `left`, `right`, and `clique`. It modifies the elements in the range `[left, right]` of the `arr` list, assigning them values in a specific pattern: the first half of the range is assigned values from `left + 1` to `left + mid`, and the second half is assigned values from `right + 1 - (right - left + 1 - mid)` to `right + 1`. Additionally, it assigns the value of `clique` to the elements in the same range `[left, right]` in the `cliquess` list. The function does not return any value.

