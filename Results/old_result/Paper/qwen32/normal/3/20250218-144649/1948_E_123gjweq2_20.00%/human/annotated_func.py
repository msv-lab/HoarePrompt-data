#State of the program right berfore the function call: n is an integer such that 2 <= n <= 40, and k is an integer such that 1 <= k <= 2n.
def func_1(n, k):
    cliques = ceil(n / k)
    arr = [0] * n
    cliquess = [0] * n
    for i in range(cliques):
        make_array(i * k, min((i + 1) * k - 1, n - 1), i + 1)
        
    #State: - `n` remains an integer such that 2 <= n <= 40.
    #- `k` remains an integer such that 1 <= k <= 2n.
    #- `cliques` remains the ceiling of `n` divided by `k`.
    #- `arr` is a list of `n` elements where each segment of `k` elements is filled with consecutive integers starting from 1 up to `cliques`.
    #- `cliquess` is a list of `n` elements with the same pattern as `arr`.
    #- `i` is `cliques - 1` at the end of the loop.
    #
    #In natural language, the final state is that `arr` and `cliquess` are lists of `n` elements where each segment of `k` elements is filled with consecutive integers starting from 1 up to the ceiling of `n` divided by `k`.
    #
    #Output State:
    print(*arr)
    #This is printed: The elements of `arr` list, where each segment of `k` elements is filled with consecutive integers starting from 1 up to `cliques` (where `cliques` is the ceiling of `n` divided by `k`)
    print(cliques)
    #This is printed: cliques (where cliques is the ceiling of n divided by k)
    print(*cliquess)
    #This is printed: the elements of `cliquess` list separated by spaces (where `cliquess` is constructed by filling segments of `k` elements with consecutive integers starting from 1 up to the ceiling of `n` divided by `k`)
#Overall this is what the function does:The function `func_1` takes two integer parameters, `n` and `k`, where `n` is between 2 and 40 inclusive, and `k` is between 1 and 2n inclusive. It calculates the ceiling of `n` divided by `k` and creates two lists, `arr` and `cliquess`, each of length `n`. These lists are filled with consecutive integers starting from 1 up to the calculated ceiling, with each segment of `k` elements containing the same integer. The function prints the elements of `arr`, the calculated ceiling value, and then the elements of `cliquess`.

#State of the program right berfore the function call: left and right are integers such that 0 <= left < right < n, and clique is an integer representing the clique number.
def make_array(left, right, clique):
    small_element = left + 1
    big_element = right + 1
    mid = (big_element - small_element) // 2
    not_mid = right - left + 1 - mid
    for i in range(mid):
        arr[left + i] = small_element + i
        
        cliquess[left + i] = clique
        
    #State: `left` and `right` are integers such that 0 <= left < right < n and right is at least left + 2, `clique` is an integer representing the clique number, `small_element` is left + 1, `big_element` is right + 1, `mid` is (right - left) // 2, `not_mid` is right - left + 1 - (right - left) // 2, `arr[left + i]` is left + 1 + i for each i from 0 to mid - 1, `cliquess[left + i]` is clique for each i from 0 to mid - 1.
    for i in range(not_mid):
        arr[left + mid + i] = big_element - i
        
        cliquess[left + mid + i] = clique
        
    #State: `left` and `right` are integers such that `0 <= left < right < n` and `right` is at least `left + 2`; `clique` is an integer representing the clique number; `small_element` is `left + 1`; `big_element` is `right + 1`; `mid` is `(right - left) // 2`; `not_mid` is `right - left + 1 - (right - left) // 2`; `arr[left + i]` is `left + 1 + i` for each `i` from `0` to `mid - 1`; `arr[left + mid + i]` is `big_element - i` for each `i` from `0` to `not_mid - 1`; `cliquess[left + i]` is `clique` for each `i` from `0` to `mid + not_mid - 1`.
#Overall this is what the function does:The function `make_array` modifies the array `arr` by filling a segment from index `left` to `right` with a specific sequence of numbers. The first half of this segment is filled with increasing numbers starting from `left + 1`, and the second half is filled with decreasing numbers starting from `right + 1`. Simultaneously, it updates another array `cliquess` to set all values in the same segment to the given `clique` number.

