#State of the program right berfore the function call: n and k are integers such that 2 <= n <= 40 and 1 <= k <= 2n.
def func_1(n, k):
    cliques = ceil(n / k)
    arr = [0] * n
    cliquess = [0] * n
    for i in range(cliques):
        make_array(i * k, min((i + 1) * k - 1, n - 1), i + 1)
        
    #State: `arr` is a list where each segment of length `k` (or the remaining elements if the last segment is shorter) is filled with a unique integer starting from 1, and `cliquess` remains a list of `n` zeros.
    print(*arr)
    #This is printed: 1 1 1 2 2 2 3 3 3 4 (where `arr` is a list with each segment of length `k` filled with a unique integer starting from 1, and the last segment may be shorter)
    print(cliques)
    #This is printed: [0, 0, ..., 0] (where the list contains `n` zeros)
    print(*cliquess)
    #This is printed: 0 0 0 ... 0 (where the number of zeros is equal to `n`)
#Overall this is what the function does:The function `func_1` accepts two parameters, `n` and `k`, where `n` is an integer between 2 and 40, inclusive, and `k` is an integer between 1 and 2n, inclusive. It divides the integer `n` into `ceil(n / k)` segments, each of length `k` (or the remaining elements if the last segment is shorter), and fills each segment in the list `arr` with a unique integer starting from 1. The function prints the list `arr` where each segment is filled as described, the number of segments `cliques`, and a list `cliquess` of `n` zeros. The function does not return any value.

#State of the program right berfore the function call: left and right are non-negative integers such that left <= right, and clique is a positive integer.
def make_array(left, right, clique):
    small_element = left + 1
    big_element = right + 1
    mid = (big_element - small_element + 1) // 2
    not_mid = right - left + 1 - mid
    for i in range(mid):
        arr[left + mid - i - 1] = small_element + i
        
        cliquess[left + i] = clique
        
    #State: The values of `left`, `right`, `clique`, `small_element`, and `big_element` remain unchanged. The array `arr` has been updated such that the elements from index `left + mid - mid` (which is `left`) to `left + mid - 1` are set to the values from `small_element` to `small_element + mid - 1`. The array `cliquess` has been updated such that the elements from index `left` to `left + mid - 1` are all set to `clique`.
    for i in range(not_mid):
        arr[left + mid + i] = big_element - i
        
        cliquess[left + mid + i] = clique
        
    #State: Output State: The values of `left`, `right`, `clique`, `small_element`, and `big_element` remain unchanged. The array `arr` has been updated such that the elements from index `left` to `left + mid - 1` are set to the values from `small_element` to `small_element + mid - 1`, and the elements from index `left + mid` to `left + mid + not_mid - 1` are set to the values from `big_element - not_mid + 1` to `big_element`. The array `cliquess` has been updated such that the elements from index `left` to `left + mid - 1` are all set to `clique`, and the elements from index `left + mid` to `left + mid + not_mid - 1` are also all set to `clique`.
#Overall this is what the function does:The function `make_array` accepts three parameters: `left`, `right`, and `clique`. `left` and `right` are non-negative integers with `left` ≤ `right`, and `clique` is a positive integer. The function updates two arrays, `arr` and `cliquess`, in place. After the function concludes, the elements of `arr` from index `left` to `right` are set such that the first half of the range (from `left` to `left + mid - 1`) contains values from `left + 1` to `left + mid`, and the second half (from `left + mid` to `right`) contains values from `right + 1 - not_mid` to `right + 1`. The elements of `cliquess` from index `left` to `right` are all set to the value of `clique`. The function does not return any value.

