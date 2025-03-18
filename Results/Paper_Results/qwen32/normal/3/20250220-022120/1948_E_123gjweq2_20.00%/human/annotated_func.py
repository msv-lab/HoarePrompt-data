#State of the program right berfore the function call: n and k are integers such that 2 <= n <= 40 and 1 <= k <= 2n.
def func_1(n, k):
    cliques = ceil(n / k)
    arr = [0] * n
    cliquess = [0] * n
    for i in range(cliques):
        make_array(i * k, min((i + 1) * k - 1, n - 1), i + 1)
        
    #State: `arr` and `cliquess` are lists of length `n` where each segment of length `k` (or less for the last segment) is filled with consecutive integers starting from `1` up to `cliques`. All other elements remain `0` if they do not fall into any segment.
    print(*arr)
    #This is printed: arr (where arr is a list of length n, divided into segments of length k, each segment filled with integers from 1 to cliques, and the rest of the elements in each segment are 0 if they do not fall into any segment)
    print(cliques)
    #This is printed: cliques (where cliques is a list of length n with segments of length k filled with consecutive integers starting from 1 up to cliques, and the rest of the elements are 0)
    print(*cliquess)
    #This is printed: [elements of the cliquess list, where each segment of length k is filled with consecutive integers from 1 to cliques, and the remaining elements are 0]
#Overall this is what the function does:The function `func_1` takes two integer parameters `n` and `k`, where `n` is between 2 and 40 inclusive, and `k` is between 1 and 2n inclusive. It divides `n` into segments of length `k` (or less for the last segment) and fills each segment with consecutive integers starting from 1 up to the number of segments (`cliques`). The function prints three lists: the first list (`arr`) contains these filled segments with zeros in any remaining positions, the second list is the number of segments (`cliques`), and the third list (`cliquess`) is identical to the first list.

#State of the program right berfore the function call: left and right are integers such that 0 <= left < right < len(arr), and clique is an integer representing the clique number to which the vertices will be assigned.
def make_array(left, right, clique):
    small_element = left + 1
    big_element = right + 1
    mid = (big_element - small_element) // 2
    not_mid = right - left + 1 - mid
    for i in range(mid):
        arr[left + i] = small_element + i
        
        cliquess[left + i] = clique
        
    #State: `left` and `right` are integers such that 0 <= left < right < len(arr); `clique` is an integer; `small_element` is `left + 1`; `big_element` is `right + 1`; `mid` is `(big_element - small_element) // 2`; `not_mid` is `(right - left + 2) // 2`; `arr[left + i]` is `small_element + i` for i from 0 to `mid - 1`; `cliquess[left + i]` is `clique` for i from 0 to `mid - 1`.
    for i in range(not_mid):
        arr[left + mid + i] = big_element - i
        
        cliquess[left + mid + i] = clique
        
    #State: `left` and `right` are integers such that `0 <= left < right < len(arr)`, `clique` is an integer, `small_element` is `left + 1`, `big_element` is `right + 1`, `mid` is `(big_element - small_element) // 2`, `not_mid` is `(right - left + 2) // 2`, `arr[left + i]` is `small_element + i` for `i` from `0` to `mid - 1`, `arr[left + mid + i]` is `big_element - i` for `i` from `0` to `not_mid - 1`, `cliquess[left + i]` is `clique` for `i` from `0` to `mid + not_mid - 1`.
#Overall this is what the function does:The function `make_array` modifies a given array `arr` by assigning specific values to its elements between indices `left` and `right` (inclusive). The first half of this segment is filled with consecutive increasing integers starting from `left + 1`, and the second half is filled with consecutive decreasing integers starting from `right + 1`. Additionally, it assigns the `clique` number to all elements between indices `left` and `right` in another array `cliquess`.

