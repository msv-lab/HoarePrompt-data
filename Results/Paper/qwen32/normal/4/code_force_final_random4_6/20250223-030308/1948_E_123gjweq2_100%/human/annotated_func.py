#State of the program right berfore the function call: n is an integer such that 2 <= n <= 40, and k is an integer such that 1 <= k <= 2n.
def func_1(n, k):
    cliques = ceil(n / k)
    arr = [0] * n
    cliquess = [0] * n
    for i in range(cliques):
        make_array(i * k, min((i + 1) * k - 1, n - 1), i + 1)
        
    #State: `n` is an integer such that 2 <= n <= 40, `k` is an integer such that 1 <= k <= 2n, `cliques` is the ceiling of `n / k`, `arr` is a list of `n` elements where each segment of `k` elements (or less for the last segment) is filled with consecutive integers starting from 1 up to `cliques`, `cliquess` is a list of `n` elements where each segment of `k` elements (or less for the last segment) is filled with consecutive integers starting from 1 up to `cliques`.
    print(*arr)
    #This is printed: The elements of `arr` list, where each segment of `k` elements (or less for the last segment) is filled with consecutive integers starting from 1 up to `cliques` (where `cliques` is the ceiling of `n / k`)
    print(cliques)
    #This is printed: cliques (where cliques is the ceiling of n / k)
    print(*cliquess)
    #This is printed: The elements of `cliquess` list, where each segment of `k` elements (or less for the last segment) is filled with consecutive integers starting from 1 up to `cliques`.
#Overall this is what the function does:The function `func_1` takes two integer parameters, `n` and `k`, where `n` is between 2 and 40 inclusive, and `k` is between 1 and 2n inclusive. It calculates the ceiling of `n / k` and uses this value to fill two lists, `arr` and `cliquess`, with segments of `k` elements each, filled with consecutive integers starting from 1 up to the calculated ceiling value. The function prints the elements of `arr`, the calculated ceiling value, and the elements of `cliquess`.

#State of the program right berfore the function call: left and right are integers such that 0 <= left < right < n, and clique is an integer representing the clique number.
def make_array(left, right, clique):
    small_element = left + 1
    big_element = right + 1
    mid = (big_element - small_element + 1) // 2
    not_mid = right - left + 1 - mid
    for i in range(mid):
        arr[left + mid - i - 1] = small_element + i
        
        cliquess[left + i] = clique
        
    #State: `left` and `right` are integers such that 0 <= left < right < n, `clique` is an integer representing the clique number, `small_element` is `left + 1`, `big_element` is `right + 1`, `mid` is `(right - left + 1) // 2`, `not_mid` is `(right - left + 1) // 2`, `arr[left]` to `arr[left + mid - 1]` are `left + 1` to `left + mid`, `cliquess[left]` to `cliquess[left + mid - 1]` are all `clique`.
    for i in range(not_mid):
        arr[left + mid + i] = big_element - i
        
        cliquess[left + mid + i] = clique
        
    #State: `left` and `right` are integers such that `0 <= left < right < n`, `clique` is an integer representing the clique number, `small_element` is `left + 1`, `big_element` is `right + 1`, `mid` is `(right - left + 1) // 2`, `not_mid` is `(right - left + 1) // 2` and must be greater than 0, `arr[left]` to `arr[left + mid - 1]` are `left + 1` to `left + mid`, `cliquess[left]` to `cliquess[left + mid - 1]` are all `clique`, `arr[left + mid]` to `arr[left + mid + (not_mid - 1)]` are `big_element` to `big_element - (not_mid - 1)`, `cliquess[left + mid]` to `cliquess[left + mid + (not_mid - 1)]` are all `clique`.
#Overall this is what the function does:The function `make_array` populates a portion of the `arr` array with a sequence of numbers from `left + 1` to `right + 1`, splitting this sequence into two parts: the first half in ascending order and the second half in descending order. It also assigns the value of `clique` to the corresponding elements in the `cliquess` array.

