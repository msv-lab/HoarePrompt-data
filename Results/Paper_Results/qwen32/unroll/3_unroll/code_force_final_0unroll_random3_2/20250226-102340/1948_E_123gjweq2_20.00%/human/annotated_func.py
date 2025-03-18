#State of the program right berfore the function call: n is an integer such that 2 <= n <= 40, and k is an integer such that 1 <= k <= 2n.
def func_1(n, k):
    cliques = ceil(n / k)
    arr = [0] * n
    cliquess = [0] * n
    for i in range(cliques):
        make_array(i * k, min((i + 1) * k - 1, n - 1), i + 1)
        
    #State: - `arr` will be divided into segments of size `k` (or smaller for the last segment), with each segment filled with a unique value starting from 1 up to `cliques`.
    #   - `cliquess` will also be modified in the same manner as `arr`.
    #
    #Let's describe the output state in a clear format:
    #
    #Output State:
    print(*arr)
    #This is printed: [values of arr after filling segments of size k with unique values from 1 to cliques]
    print(cliques)
    #This is printed: cliques (where cliques is the number of unique values used to fill the segments of arr and cliquess)
    print(*cliquess)
    #This is printed: cliquess (where cliquess is a list divided into segments of size k, each filled with a unique value from 1 to cliques)
#Overall this is what the function does:The function `func_1` takes two integer parameters, `n` and `k`, where `n` is between 2 and 40 inclusive, and `k` is between 1 and 2n inclusive. It divides a list of size `n` into segments of size `k` (or smaller for the last segment), fills each segment with a unique value starting from 1 up to the number of segments (`cliques`), and prints the modified list, the number of unique values used, and another list that mirrors the first list's segmentation.

#State of the program right berfore the function call: left and right are integers such that 0 <= left < right < len(arr), and clique is an integer representing the clique number.
def make_array(left, right, clique):
    small_element = left + 1
    big_element = right + 1
    mid = (big_element - small_element) // 2
    not_mid = right - left + 1 - mid
    for i in range(mid):
        arr[left + i] = small_element + i
        
        cliquess[left + i] = clique
        
    #State: `left` and `right` are integers such that 0 <= left < right < len(arr), `clique` is an integer representing the clique number, `small_element` is `left + 1`, `big_element` is `right + 1`, `mid` is `(right - left) // 2`, `not_mid` is `right - left + 1 - (right - left) // 2`, `arr[left]` to `arr[left + mid - 1]` are set to `small_element`, `small_element + 1`, ..., `small_element + mid - 1`, `cliquess[left]` to `cliquess[left + mid - 1]` are set to `clique`.
    for i in range(not_mid):
        arr[left + mid + i] = big_element - i
        
        cliquess[left + mid + i] = clique
        
    #State: `arr[left]` to `arr[left + mid - 1]` are `small_element`, `small_element + 1`, ..., `small_element + mid - 1`, `arr[left + mid]` to `arr[right]` are `big_element`, `big_element - 1`, ..., `big_element - (not_mid - 1)`, `cliquess[left]` to `cliquess[right]` are all `clique`.
#Overall this is what the function does:The function `make_array` modifies a portion of the array `arr` between the indices `left` and `right` by setting the first half to increasing values starting from `left + 1` and the second half to decreasing values starting from `right + 1`. It also sets the corresponding elements in the `cliquess` array to the given `clique` number.

