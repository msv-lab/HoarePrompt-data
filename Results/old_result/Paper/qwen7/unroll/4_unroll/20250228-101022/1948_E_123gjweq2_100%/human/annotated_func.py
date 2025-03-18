#State of the program right berfore the function call: n is an integer such that 2 <= n <= 40, k is an integer such that 1 <= k <= 2 * n, and the function `make_array` is defined elsewhere to populate the array `arr` based on the specified range and clique index.
def func_1(n, k):
    cliques = ceil(n / k)
    arr = [0] * n
    cliquess = [0] * n
    for i in range(cliques):
        make_array(i * k, min((i + 1) * k - 1, n - 1), i + 1)
        
    #State: Output State: `cliques` is equal to ceil(`n` / `k`), `n` is an integer such that 2 <= n <= 40, `k` is an integer such that 1 <= k <= 2 * n, `arr` is a list of `n` ones, `cliquess` is a list of `n` zeros.
    #
    #Explanation: The loop iterates from `i = 0` to `i = cliques - 1`. For each iteration, the function `make_array(i * k, min((i + 1) * k - 1, n - 1), i + 1)` is called. This function sets the elements in the `arr` list from index `i * k` to `min((i + 1) * k - 1, n - 1)` (inclusive) to `i + 1`. Since `i + 1` will take on values from 1 to `cliques`, and each element in `arr` will be set to one of these values within its respective range, the final state of `arr` will be a list of `n` ones. The variable `cliquess` remains unchanged as it is not modified by the loop.
    print(*arr)
    #This is printed: 1 1 1 ... 1 (n times)
    print(cliques)
    #This is printed: cliques (where cliques is the ceiling of n divided by k)
    print(*cliquess)
    #This is printed: 0 0 0 ... 0 (where there are n zeros)
#Overall this is what the function does:The function `func_1` accepts two parameters, `n` and `k`, where `n` is an integer between 2 and 40, and `k` is an integer between 1 and 2 * n. It calculates the number of cliques as `ceil(n / k)` and populates an array `arr` with `n` ones. Additionally, it prints the array `arr`, the number of cliques, and an array `cliquess` filled with `n` zeros.

#State of the program right berfore the function call: left and right are integers such that left < right and both are within the range [0, n-1], where n is the length of the array arr. clique is an integer representing the clique identifier.
def make_array(left, right, clique):
    small_element = left + 1
    big_element = right + 1
    mid = (big_element - small_element + 1) // 2
    not_mid = right - left + 1 - mid
    for i in range(mid):
        arr[left + mid - i - 1] = small_element + i
        
        cliquess[left + i] = clique
        
    #State: Output State: `left` is an integer, `right` is an integer such that `left < right`, `small_element` is `left + 1`, `big_element` is `right + 1`, `mid` is `(right + 1 - (left + 1) + 1) // 2`, `not_mid` is `right - left - mid + 1`, `arr` is a list where elements from index `left + mid - 1` to `left` are filled with values starting from `small_element` to `small_element + mid - 1`, `cliquess` is a list where elements from index `left` to `left + mid - 1` are set to `clique`.
    for i in range(not_mid):
        arr[left + mid + i] = big_element - i
        
        cliquess[left + mid + i] = clique
        
    #State: Output State: `left` is an integer, `right` is an integer such that `left < right`, `small_element` is `left + 1`, `big_element` is `right + 1`, `mid` is `(right + 1 - (left + 1) + 1) // 2`, `not_mid` is `right - left - mid + 1`, `arr` is a list where elements from index `left + mid - 1` to `left` are filled with values starting from `small_element` to `small_element + mid - 1`, and elements from index `left` to `left + not_mid - 1` are filled with values starting from `big_element - (i + 1)` to `big_element - i`, `cliquess` is a list where elements from index `left` to `left + mid - 1` are set to `clique`.
#Overall this is what the function does:The function `make_array` takes three parameters: `left`, `right`, and `clique`. It modifies an array `arr` by filling a segment of it with a sequence of increasing integers starting from `left + 1` up to `right + 1` and assigns the value of `clique` to a corresponding segment in another list `cliquess`. Specifically, it fills the first half of the specified segment with increasing values and the second half with decreasing values, ensuring that the entire segment is covered.

