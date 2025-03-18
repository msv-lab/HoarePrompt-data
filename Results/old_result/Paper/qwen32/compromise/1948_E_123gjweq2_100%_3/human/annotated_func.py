#State of the program right berfore the function call: n is an integer such that 2 <= n <= 40, and k is an integer such that 1 <= k <= 2n.
def func_1(n, k):
    cliques = ceil(n / k)
    arr = [0] * n
    cliquess = [0] * n
    for i in range(cliques):
        make_array(i * k, min((i + 1) * k - 1, n - 1), i + 1)
        
    #State: `n` is an integer such that 2 <= n <= 40, `k` is an integer such that 1 <= k <= 2n, `cliques` is the ceiling of `n / k`, `arr` is a list of `n` elements where each segment of length `k` (or less for the last segment) is filled with the value `i + 1` for the `i-th` iteration, `cliquess` is a list of `n` elements where each segment of length `k` (or less for the last segment) is filled with the value `i + 1` for the `i-th` iteration.
    print(*arr)
    #This is printed: [1, 1, 1, ..., i+1, i+1, ..., i+1, ..., last_segment] (where each segment of length k is filled with i+1 for the i-th iteration, and the last segment may be shorter than k)
    print(cliques)
    #This is printed: cliques (where cliques is the ceiling of n / k)
    print(*cliquess)
    #This is printed: [1, 1, ..., 1, 2, 2, ..., 2, 3, 3, ..., 3, ..., ceil(n / k), ceil(n / k), ..., ceil(n / k)] (where each number i appears k times except possibly the last number which appears n % k times if n % k != 0)
#Overall this is what the function does:The function `func_1` takes two integer parameters, `n` and `k`, where `n` is in the range [2, 40] and `k` is in the range [1, 2n]. It calculates the ceiling of `n / k` and creates two lists, `arr` and `cliquess`, each of length `n`. The list `arr` is filled with segments of length `k` (or less for the last segment) with values incrementing from 1 up to the calculated ceiling. The list `cliquess` is similarly filled, with each number from 1 to the ceiling appearing `k` times, except possibly the last number which may appear fewer times if `n % k` is not zero. The function prints the contents of `arr`, the calculated ceiling, and the contents of `cliquess`.

#State of the program right berfore the function call: left and right are integers such that 0 <= left < right < n, and clique is an integer representing the clique number for the vertices in the range from left to right.
def make_array(left, right, clique):
    small_element = left + 1
    big_element = right + 1
    mid = (big_element - small_element + 1) // 2
    not_mid = right - left + 1 - mid
    for i in range(mid):
        arr[left + mid - i - 1] = small_element + i
        
        cliquess[left + i] = clique
        
    #State: `left` and `right` are integers such that 0 <= left < right < n, `clique` is an integer representing the clique number for the vertices in the range from left to right, `small_element` is `left + 1`, `big_element` is `right + 1`, `mid` is `(right - left + 1) // 2`, `not_mid` is `right - left + 1 - mid`, `arr[left + mid - 1]` to `arr[left]` are set to `small_element` to `small_element + mid - 1` respectively, `cliquess[left]` to `cliquess[left + mid - 1]` are all set to `clique`.
    for i in range(not_mid):
        arr[left + mid + i] = big_element - i
        
        cliquess[left + mid + i] = clique
        
    #State: `left` and `right` are integers such that 0 <= left < right < n, `clique` is an integer representing the clique number for the vertices in the range from left to right, `small_element` is `left + 1`, `big_element` is `right + 1`, `mid` is `(right - left + 1) // 2`, `not_mid` is `right - left + 1 - mid`, `arr[left + mid - 1]` to `arr[left]` are set to `small_element` to `small_element + mid - 1` respectively, `cliquess[left]` to `cliquess[left + mid - 1]` are all set to `clique`, `arr[left + mid]` to `arr[right]` are set to `big_element - 1` to `big_element - not_mid` respectively, `cliquess[left + mid]` to `cliquess[right]` are all set to `clique`.
#Overall this is what the function does:The function `make_array` modifies two arrays, `arr` and `cliquess`, for a specified range of indices from `left` to `right`. It sets the first half of the range in `arr` to increasing values starting from `left + 1` and the second half to decreasing values starting from `right + 1`. It also assigns the `clique` value to all entries in the `cliquess` array for the same range.

