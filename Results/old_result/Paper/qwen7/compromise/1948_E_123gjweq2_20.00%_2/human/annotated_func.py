#State of the program right berfore the function call: n is an integer such that 2 ≤ n ≤ 40, k is an integer such that 1 ≤ k ≤ 2n, and the function `make_array` is defined elsewhere to fill the array `arr` with values according to the specified range and clique assignment.
def func_1(n, k):
    cliques = ceil(n / k)
    arr = [0] * n
    cliquess = [0] * n
    for i in range(cliques):
        make_array(i * k, min((i + 1) * k - 1, n - 1), i + 1)
        
    #State: Output State: `cliques` is equal to ceil(`n` / `k`), `n` is an integer such that 2 ≤ n ≤ 40, `k` is an integer such that 1 ≤ k ≤ 2n, `arr` is a list of length `n` with some elements set to non-zero values depending on the values of `cliques`, `i * k`, and min((i + 1) * k - 1, n - 1), `cliquess` is a list of `n` zeros.
    #
    #Explanation: The loop iterates `cliques` times. During each iteration `i`, it sets elements in `arr` from index `i * k` to min((i + 1) * k - 1, n - 1) to a value of `i + 1`. This means that for each `i`, a segment of `arr` starting at `i * k` and ending at the minimum of (i + 1) * k - 1 or n - 1 will be filled with the value `i + 1`. The rest of the array remains zero. The variable `cliquess` remains unchanged as it is not modified within the loop.
    print(*arr)
    #This is printed: 1 1 1 2 2 2 3 3 3 4 (or a similar pattern based on the specific values of `n` and `k`)
    print(cliques)
    #This is printed: cliques (where cliques is an integer between 1 and n inclusive)
    print(*cliquess)
    #This is printed: 0 0 0 ... 0 (n zeros)
#Overall this is what the function does:The function `func_1` accepts two integers `n` and `k`, where `2 ≤ n ≤ 40` and `1 ≤ k ≤ 2n`. It calculates the number of cliques (`cliques`) as `ceil(n / k)`. The function then fills an array `arr` of length `n` with values based on the calculated number of cliques and the range defined by `k`. Specifically, for each clique `i`, it sets elements in `arr` from index `i * k` to the minimum of `(i + 1) * k - 1` and `n - 1` to the value `i + 1`. After filling the array, the function prints the array, the number of cliques, and an array of `n` zeros.

#State of the program right berfore the function call: left and right are integers such that left < right, and clique is an integer representing the clique identifier.
def make_array(left, right, clique):
    small_element = left + 1
    big_element = right + 1
    mid = (big_element - small_element) // 2
    not_mid = right - left + 1 - mid
    for i in range(mid):
        arr[left + i] = small_element + i
        
        cliquess[left + i] = clique
        
    #State: Output State: `left` is an integer such that `left` < `right`, `right` is an integer, `clique` is an integer representing the clique identifier, `small_element` is `left + 1`, `big_element` is `right + 1`, `mid` is `(big_element - small_element) // 2`, `not_mid` is `right - left + 1 - mid`, `arr` is a list where elements from index `left` to `left + mid - 1` are set to `small_element + i` for `i` in the range `0` to `mid - 1` and corresponding `cliquess` is a list where elements from index `left` to `left + mid - 1` are set to `clique`.
    for i in range(not_mid):
        arr[left + mid + i] = big_element - i
        
        cliquess[left + mid + i] = clique
        
    #State: Output State: `left` is an integer such that `left` < `right`, `right` is an integer, `clique` is an integer representing the clique identifier, `small_element` is `left + 1`, `big_element` is `right + 1`, `mid` is `(big_element - small_element) // 2`, `not_mid` is `right - left + 1 - mid`, `arr` is a list where elements from index `left` to `left + mid - 1` are set to `small_element + i` for `i` in the range `0` to `mid - 1` and elements from index `left + mid` to `left + not_mid - 1` are set to `big_element - (i - mid)` and corresponding `cliquess` is a list where elements from index `left` to `left + mid - 1` are set to `clique` and elements from index `left + mid` to `left + not_mid - 1` are set to `clique`.
#Overall this is what the function does:The function `make_array` accepts two integers `left` and `right` (where `left < right`) and an integer `clique`. It constructs an array `arr` and another list `cliquess`. The function sets the elements of `arr` from index `left` to `left + mid - 1` to values starting from `small_element` (which is `left + 1`) and incrementing by 1, and sets the corresponding elements in `cliquess` to `clique`. It then sets the elements of `arr` from index `left + mid` to `left + not_mid - 1` to values starting from `big_element` (which is `right + 1`) and decrementing by 1, and sets the corresponding elements in `cliquess` to `clique`. After the function executes, the array `arr` and list `cliquess` are updated according to these rules.

