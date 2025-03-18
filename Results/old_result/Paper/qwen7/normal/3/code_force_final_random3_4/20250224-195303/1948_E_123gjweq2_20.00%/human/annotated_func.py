#State of the program right berfore the function call: n is an integer such that 2 ≤ n ≤ 40, k is an integer such that 1 ≤ k ≤ 2n, and the function `make_array` is defined elsewhere to fill the array `arr` based on the given parameters.
def func_1(n, k):
    cliques = ceil(n / k)
    arr = [0] * n
    cliquess = [0] * n
    for i in range(cliques):
        make_array(i * k, min((i + 1) * k - 1, n - 1), i + 1)
        
    #State: Output State: `cliques` must be at least 1, `i` equals `cliques`, `n` is an integer such that \(2 \leq n \leq 40\), `k` is an integer such that \(1 \leq k \leq 2n\), `arr` is a list of `n` zeros, `cliquess` is a list of `n` zeros, `arr` is updated to contain values from `0 * k` to `min((cliques) * k - 1, n - 1)` inclusive, with a length of `cliques`.
    #
    #In simpler terms, after the loop has executed all its iterations, `cliques` will still be at least 1, `i` will now be equal to the final value of `cliques`, `n` will remain within the range of 2 to 40, `k` will stay within the range of 1 to 2n, `arr` will still be a list of `n` zeros, and `cliquess` will also remain a list of `n` zeros. The `arr` list will be updated to include values starting from `0 * k` up to the minimum of `(cliques * k - 1)` and `n - 1`, with the length of this segment being equal to `cliques`.
    print(*arr)
    #This is printed: [0, 10, ..., min((cliques * k - 1), n - 1)] (where the list starts from 0 * k and ends at the minimum of (cliques * k - 1) and n - 1, with a total of cliques elements)
    print(cliques)
    #This is printed: cliques (where cliques is at least 1)
    print(*cliquess)
    #This is printed: 0 0 0 ... 0 (n times)
#Overall this is what the function does:The function `func_1` accepts two parameters, `n` and `k`, where `n` is an integer between 2 and 40, and `k` is an integer between 1 and 2n. It calculates the number of cliques (`cliques`) based on these parameters and uses the `make_array` function to fill an array `arr` with specific values. After processing, it prints the updated array `arr`, the number of cliques, and an array of zeros (`cliquess`). The final state of the program includes an updated `arr` containing values from `0 * k` to `min((cliques * k - 1), n - 1)`, a `cliques` value indicating the number of cliques, and a `cliquess` array consisting entirely of zeros.

#State of the program right berfore the function call: left and right are integers such that left < right, and clique is an integer representing the clique identifier.
def make_array(left, right, clique):
    small_element = left + 1
    big_element = right + 1
    mid = (big_element - small_element) // 2
    not_mid = right - left + 1 - mid
    for i in range(mid):
        arr[left + i] = small_element + i
        
        cliquess[left + i] = clique
        
    #State: Output State: All elements in `arr` from index `left` to `left + mid - 1` are set to values starting from `small_element` and incrementing by 1 for each subsequent index. The corresponding elements in `cliquess` from index `left` to `left + mid - 1` are all set to `clique`. The variable `i` will be equal to `mid - 1` after the loop finishes, and both `left` and `right` will retain their original values.
    #
    #In more detail:
    #- `arr[left]` to `arr[left + mid - 1]` will contain the sequence of integers starting from `small_element` to `small_element + mid - 1`.
    #- `cliquess[left]` to `cliquess[left + mid - 1]` will all be set to `clique`.
    #- The loop variable `i` will be `mid - 1` after the loop completes.
    #- The variables `left`, `right`, `small_element`, `big_element`, `mid`, and `not_mid` will retain their initial or updated values from before the loop started, but no further changes will occur within the loop itself.
    for i in range(not_mid):
        arr[left + mid + i] = big_element - i
        
        cliquess[left + mid + i] = clique
        
    #State: Output State: The array `arr` from index `left + mid` to `left + mid + not_mid - 1` will contain the sequence of integers starting from `big_element - (not_mid - 1)` to `big_element - 1`. The corresponding elements in `cliquess` from index `left + mid` to `left + mid + not_mid - 1` will all be set to `clique`. The variable `i` will be equal to `not_mid` after the loop finishes, and both `left`, `right`, `small_element`, `big_element`, `mid`, and `not_mid` will retain their original values from before the loop started.
    #
    #In simpler terms, after the loop has executed all its iterations, the elements in `arr` from `left + mid` to `left + mid + not_mid - 1` will be filled with decreasing values starting from `big_element - 1` down to `big_element - (not_mid - 1)`, while the corresponding elements in `cliquess` will all be set to `clique`.
#Overall this is what the function does:The function `make_array` accepts two integers `left` and `right` (with `left` less than `right`) and an integer `clique` representing a clique identifier. It fills the array `arr` with a specific pattern of values between indices `left` and `right`, inclusive, and sets corresponding elements in the array `cliquess` to the given `clique` identifier. Specifically, it first populates the array segment from `left` to `left + mid - 1` with increasing values starting from `small_element`, and then populates the segment from `left + mid` to `left + mid + not_mid - 1` with decreasing values starting from `big_element`. After executing the function, the array `arr` and the array `cliquess` will reflect these changes, and the variables `left`, `right`, `small_element`, `big_element`, `mid`, and `not_mid` will retain their original values.

