#State of the program right berfore the function call: n and k are integers such that 2 <= n <= 40 and 1 <= k <= 2n.
def func_1(n, k):
    cliques = ceil(n / k)
    arr = [0] * n
    cliquess = [0] * n
    for i in range(cliques):
        make_array(i * k, min((i + 1) * k - 1, n - 1), i + 1)
        
    #State: `n` and `k` are integers such that 2 <= n <= 40 and 1 <= k <= 2n, `cliques` is the ceiling of `n / k` and must be greater than or equal to the number of iterations, `arr` is a list of `n` integers where each segment of length `k` (or the remaining elements if the last segment is shorter) is filled with the corresponding `i + 1` value, `cliquess` is a list of `n` zeros, and the function `make_array` has been called `cliques` times with arguments `i * k`, `min((i + 1) * k - 1, n - 1)`, and `i + 1` for each `i` from 0 to `cliques - 1`.
    print(*arr)
    #This is printed: 1 1 1 ... (repeating `i + 1` for each segment of length `k` or the remaining elements, where `i` ranges from 0 to `cliques - 1`)
    print(cliques)
    #This is printed: cliques (where cliques is the ceiling of \(n / k\))
    print(*cliquess)
    #This is printed: 0 0 0 ... 0 (where there are n zeros in the sequence)
#Overall this is what the function does:The function `func_1` accepts two parameters `n` and `k`, where `n` is an integer between 2 and 40 (inclusive) and `k` is an integer between 1 and 2n (inclusive). It calculates the number of cliques as the ceiling of `n / k`. The function then populates an array `arr` of length `n` such that each segment of length `k` (or the remaining elements if the last segment is shorter) is filled with the corresponding `i + 1` value, where `i` ranges from 0 to `cliques - 1`. The function prints the contents of `arr`, the number of cliques, and a list of `n` zeros. The function does not return any value.

#State of the program right berfore the function call: left and right are non-negative integers such that left <= right, and clique is a positive integer.
def make_array(left, right, clique):
    small_element = left + 1
    big_element = right + 1
    mid = (big_element - small_element + 1) // 2
    not_mid = right - left + 1 - mid
    for i in range(mid):
        arr[left + mid - i - 1] = small_element + i
        
        cliquess[left + i] = clique
        
    #State: `left` and `right` are non-negative integers such that `left` < `right`, `clique` is a positive integer, `small_element` is `left + 1`, `big_element` is `right + 1`, `mid` is `(right - left) // 2` (which must be greater than or equal to `mid`), `not_mid` is `(right - left + 1) - (right - left) // 2`, `i` is `mid - 1`, `arr[left + mid - i - 1]` to `arr[left]` are filled with `small_element + i` to `small_element + 0` respectively, and `cliquess[left + i]` to `cliquess[left]` are all set to `clique`.
    for i in range(not_mid):
        arr[left + mid + i] = big_element - i
        
        cliquess[left + mid + i] = clique
        
    #State: After the loop executes all iterations, `i` is `not_mid - 1`, `not_mid` is greater than or equal to 0, `left` and `right` are non-negative integers such that `left` < `right`, `clique` is a positive integer, `small_element` is `left + 1`, `big_element` is `right + 1`, `mid` is `(right - left) // 2`, `arr[left + mid - i - 1]` to `arr[left]` are filled with `small_element + i` to `small_element + 0` respectively, `cliquess[left + i]` to `cliquess[left]` are all set to `clique`, `cliquess[left + mid + i]` to `cliquess[left + mid]` are all set to `clique`, and `arr[left + mid + i]` to `arr[left + mid]` are filled with `big_element - i` to `big_element - (not_mid - 1)` respectively.
#Overall this is what the function does:The function `make_array` accepts three parameters: `left`, `right`, and `clique`. `left` and `right` are non-negative integers with `left` ≤ `right`, and `clique` is a positive integer. The function modifies two arrays, `arr` and `cliquess`, such that: 
- The elements in `arr` from index `left` to `right` are filled with values in a specific pattern. The first half of this range (from `left + mid - 1` to `left`) is filled with values starting from `left + 1` and incrementing by 1, while the second half (from `left + mid` to `right`) is filled with values starting from `right + 1` and decrementing by 1.
- The elements in `cliquess` from index `left` to `right` are all set to the value of `clique`. 
The function does not return any value.

