#State of the program right berfore the function call: n and k are integers such that 2 <= n <= 40 and 1 <= k <= 2n.
def func_1(n, k):
    cliques = ceil(n / k)
    arr = [0] * n
    cliquess = [0] * n
    for i in range(cliques):
        make_array(i * k, min((i + 1) * k - 1, n - 1), i + 1)
        
    #State: `i` is `cliques - 1`, `cliques` is the ceiling of `n / k`, `arr` is a list of `n` integers where each block of `k` elements (or the remaining elements if less than `k`) is set to the corresponding `i + 1` value, and `cliquess` is a list of `n` zeros.
    print(*arr)
    #This is printed: 1, 1, 1, 2, 2, 2, 3, 3, 3, 4 (where the number of elements and their values depend on the values of `n` and `k` as described above)
    print(cliques)
    #This is printed: - The print statement will output the value of `cliques`, which is the ceiling of `n / k`.
    #
    #Output:
    print(*cliquess)
    #This is printed: - The output will be a sequence of `n` zeros separated by spaces.
    #
    #Output:
#Overall this is what the function does:The function `func_1` accepts two integer parameters `n` and `k` where 2 <= n <= 40 and 1 <= k <= 2n. It calculates the number of cliques as the ceiling of `n / k`. The function then creates a list `arr` of `n` integers, where each block of `k` elements (or the remaining elements if less than `k`) is set to the corresponding `i + 1` value, where `i` is the index of the block. The function prints the list `arr`, the number of cliques, and a list `cliquess` of `n` zeros. The function does not return any value.

#State of the program right berfore the function call: left and right are non-negative integers such that left <= right, and clique is a positive integer.
def make_array(left, right, clique):
    small_element = left + 1
    big_element = right + 1
    mid = (big_element - small_element) // 2
    not_mid = right - left + 1 - mid
    for i in range(mid):
        arr[left + i] = small_element + i
        
        cliquess[left + i] = clique
        
    #State: After the loop executes all the iterations, `left` and `right` remain non-negative integers such that `left` < `right`, `clique` is still a positive integer, `small_element` is `left + 1`, `big_element` is `right + 1`, `mid` is `(right - left) // 2` (which must be greater than 0), `not_mid` is `right - left + 1 - mid`, `i` is `mid - 1`, `arr[left + i]` for all `i` in the range `[0, mid - 1]` is `left + 1 + i`, and `cliquess[left + i]` for all `i` in the range `[0, mid - 1]` is `clique`.
    for i in range(not_mid):
        arr[left + mid + i] = big_element - i
        
        cliquess[left + mid + i] = clique
        
    #State: `left` and `right` are non-negative integers such that `left` < `right`, `clique` is a positive integer, `small_element` is `left + 1`, `big_element` is `right + 1`, `mid` is `(right - left) // 2` (which must be greater than 0), `not_mid` is `right - left + 1 - mid` (which must be greater than or equal to 0), `i` is `not_mid - 1`, `arr[left + i]` for all `i` in the range `[0, mid - 1]` is `left + 1 + i`, `arr[left + mid + i]` for all `i` in the range `[0, not_mid - 1]` is `big_element - i`, `cliquess[left + i]` for all `i` in the range `[0, mid - 1]` is `clique`, and `cliquess[left + mid + i]` for all `i` in the range `[0, not_mid - 1]` is `clique`.
#Overall this is what the function does:The function `make_array` accepts three parameters: `left`, `right`, and `clique`. `left` and `right` are non-negative integers with `left` ≤ `right`, and `clique` is a positive integer. The function populates an array `arr` and another array `cliquess` with specific values. After the function concludes, `arr` contains a sequence of integers starting from `left + 1` to `right + 1` in a specific pattern: the first half of the range from `left` to `left + mid - 1` is filled with increasing values starting from `left + 1`, and the second half from `left + mid` to `right` is filled with decreasing values starting from `right + 1` and moving backwards. The `cliquess` array is filled with the value of `clique` for all indices from `left` to `right`. The function does not return any value, but it modifies the arrays `arr` and `cliquess` in place.

