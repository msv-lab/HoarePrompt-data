#State of the program right berfore the function call: n is an integer such that 2 <= n <= 40, k is an integer such that 1 <= k <= 2 * n, and the function `make_array` is defined elsewhere to populate the array `arr` and `cliquess` according to the specified conditions.
def func_1(n, k):
    cliques = ceil(n / k)
    arr = [0] * n
    cliquess = [0] * n
    for i in range(cliques):
        make_array(i * k, min((i + 1) * k - 1, n - 1), i + 1)
        
    #State: Output State: `cliques` is equal to `ceil(n / k)`, `arr` is a list where each index from `i * k` to `min((i + 1) * k - 1, n - 1)` is set to `i + 1` for each iteration `i` from `0` to `cliques - 1`, and `cliquess` is a list of `n` zeros.
    print(*arr)
    #This is printed: 1 1 2 2 3 3 4
    print(cliques)
    #This is printed: ceil(n / k)
    print(*cliquess)
    #This is printed: - The `print(*cliquess)` statement will print the elements of `cliquess` separated by spaces. Since `cliquess` is a list of `n` zeros, the output will be `0 0 0 ... 0` (with `n` zeros).
    #
    #Output:
#Overall this is what the function does:The function `func_1` accepts two parameters, `n` and `k`, where `n` is an integer between 2 and 40, and `k` is an integer between 1 and 2 * `n`. It populates an array `arr` and a list `cliquess` based on the value of `cliques`, which is calculated as `ceil(n / k)`. After populating `arr`, the function prints the contents of `arr`, the value of `cliques`, and the list `cliquess` filled with zeros. The final state of the program includes the printed values of `arr`, `cliques`, and `cliquess`.

#State of the program right berfore the function call: left and right are integers such that left < right, and clique is an integer representing the clique identifier.
def make_array(left, right, clique):
    small_element = left + 1
    big_element = right + 1
    mid = (big_element - small_element) // 2
    not_mid = right - left + 1 - mid
    for i in range(mid):
        arr[left + i] = small_element + i
        
        cliquess[left + i] = clique
        
    #State: Output State: `left` is an integer such that `left` < `right`, `right` is an integer, `clique` is an integer representing the clique identifier, `small_element` is `left + 1`, `big_element` is `right + 1`, `mid` is `(right + 1 - (left + 1)) // 2`, `not_mid` is `right - left + 1 - mid`, `arr` is a list where for each index `i` in the range `[left, left + mid - 1]`, `arr[i] = small_element + i` and `cliquess[i] = clique`.
    for i in range(not_mid):
        arr[left + mid + i] = big_element - i
        
        cliquess[left + mid + i] = clique
        
    #State: Output State: `left` is an integer such that `left` < `right`, `right` is an integer, `clique` is an integer representing the clique identifier, `small_element` is `left + 1`, `big_element` is `right + 1`, `mid` is `(right + 1 - (left + 1)) // 2`, `not_mid` is `right - left + 1 - mid`, `arr` is a list where for each index `i` in the range `[left, left + mid - 1]`, `arr[i] = small_element + i` and `cliquess[i] = clique`, for each index `i` in the range `[left + mid, left + not_mid + mid - 1]`, `arr[i] = big_element - (i - (left + mid))` and `cliquess[i] = clique`.
#Overall this is what the function does:The function `make_array` accepts two integers `left` and `right` (where `left < right`), and an integer `clique`. It constructs an array `arr` and populates it with values ranging from `left + 1` to `right` in a specific pattern. For each index `i` in the first half of the range, it sets `arr[i]` to `left + 1 + i` and associates the `clique` identifier with that index. For the second half of the range, it sets `arr[i]` to `right` minus the corresponding offset and again associates the `clique` identifier. The function also updates another array `cliquess` to store the `clique` identifier for each index in the specified range. After executing the function, the arrays `arr` and `cliquess` contain the specified values based on the given `left`, `right`, and `clique` parameters.

