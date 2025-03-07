#State of the program right berfore the function call: n and k are integers such that 2 <= n <= 40 and 1 <= k <= 2n.
def func_1(n, k):
    cliques = ceil(n / k)
    arr = [0] * n
    cliquess = [0] * n
    for i in range(cliques):
        make_array(i * k, min((i + 1) * k - 1, n - 1), i + 1)
        
    #State: `n` and `k` are integers such that 2 <= n <= 40 and 1 <= k <= 2n, `cliques` is the smallest integer greater than or equal to `n / k`, `arr` is a list where the first `k` elements are 1, the next `k` elements are 2, and so on, up to the last segment which will be filled with the value `cliques`, `cliquess` is a list of `n` zeros.
    print(*arr)
    #This is printed: - The output will be a sequence of integers where the first `k` elements are 1, the next `k` elements are 2, and so on, up to the last segment which will be filled with the value `cliques`.
    #
    #Output:
    print(cliques)
    #This is printed: cliques (where cliques is the smallest integer greater than or equal to n / k)
    print(*cliquess)
    #This is printed: 0 0 0 ... 0 (where the sequence contains `n` zeros)
#Overall this is what the function does:The function `func_1` accepts two integer parameters `n` and `k`, where `2 <= n <= 40` and `1 <= k <= 2n`. It calculates the number of cliques as the smallest integer greater than or equal to `n / k`. The function then creates a list `arr` of length `n` where the first `k` elements are 1, the next `k` elements are 2, and so on, up to the last segment which will be filled with the value `cliques`. It prints the list `arr`, the number of cliques, and a list `cliquess` of `n` zeros. The function does not return any value.

#State of the program right berfore the function call: left and right are non-negative integers such that left <= right, and clique is a positive integer.
def make_array(left, right, clique):
    small_element = left + 1
    big_element = right + 1
    mid = (big_element - small_element) // 2
    not_mid = right - left + 1 - mid
    for i in range(mid):
        arr[left + i] = small_element + i
        
        cliquess[left + i] = clique
        
    #State: `left` and `right` remain the same, `clique` remains the same, `small_element` remains the same, `big_element` remains the same, `mid` remains the same, `not_mid` remains the same, `arr[left:mid]` is updated to `[small_element, small_element + 1, ..., small_element + (mid - 1)]`, and `cliquess[left:mid]` is updated to `[clique, clique, ..., clique]`.
    for i in range(not_mid):
        arr[left + mid + i] = big_element - i
        
        cliquess[left + mid + i] = clique
        
    #State: Output State: `left` and `right` remain the same, `clique` remains the same, `small_element` remains the same, `big_element` remains the same, `mid` remains the same, `not_mid` remains the same, `arr[left:mid]` is updated to `[small_element, small_element + 1, ..., small_element + (mid - 1)]`, and `arr[left + mid:left + mid + not_mid]` is updated to `[big_element - 0, big_element - 1, ..., big_element - (not_mid - 1)]`, and `cliquess[left:mid]` is updated to `[clique, clique, ..., clique]`, and `cliquess[left + mid:left + mid + not_mid]` is updated to `[clique, clique, ..., clique]`.
#Overall this is what the function does:The function `make_array` accepts three parameters: `left`, `right`, and `clique`, where `left` and `right` are non-negative integers with `left` ≤ `right`, and `clique` is a positive integer. It updates two lists, `arr` and `cliquess`, such that `arr[left:right + 1]` is filled with a sequence of integers starting from `left + 1` to `right + 1` in a specific pattern: the first half of the range is filled with increasing values starting from `left + 1`, and the second half is filled with decreasing values starting from `right + 1`. The `cliquess` list is updated to contain the value `clique` for all indices from `left` to `right + 1`. The function does not return any value.

