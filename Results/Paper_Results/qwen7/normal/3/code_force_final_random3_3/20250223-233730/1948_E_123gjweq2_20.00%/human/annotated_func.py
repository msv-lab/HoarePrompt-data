#State of the program right berfore the function call: n is an integer such that 2 ≤ n ≤ 40, k is an integer such that 1 ≤ k ≤ 2n, and the function `make_array` is defined elsewhere to fill the array `arr` based on the given parameters.
def func_1(n, k):
    cliques = ceil(n / k)
    arr = [0] * n
    cliquess = [0] * n
    for i in range(cliques):
        make_array(i * k, min((i + 1) * k - 1, n - 1), i + 1)
        
    #State: Output State: `cliques` must be greater than or equal to the number of iterations, `i` will be `cliques`, `k` is used in the calculations but its exact value is not provided, resulting in the final call to `make_array((cliques-1) * k, min(cliques * k - 1, n - 1), cliques)`. The variable `arr` will be updated multiple times during the loop, and `cliquess` will also be updated, but their final values depend on the specific sequence of updates performed by the `make_array` function calls.
    #
    #In simpler terms, after all iterations of the loop, `cliques` will be the total number of iterations, `i` will match `cliques`, `k` will be used in the last `make_array` call but its exact value is unknown, and both `arr` and `cliquess` will have been updated according to the calls made within the loop.
    print(*arr)
    #This is printed: [elements of arr] (where the elements depend on the sequence of operations performed within the loop)
    print(cliques)
    #This is printed: cliques (where cliques is the total number of iterations)
    print(*cliquess)
    #This is printed: the elements of the cliquess list after all iterations (where the exact values depend on the sequence of updates performed by the make_array function calls)
#Overall this is what the function does:The function `func_1` accepts two parameters, `n` and `k`, where `n` is an integer between 2 and 40 inclusive, and `k` is an integer between 1 and 2n inclusive. It calculates the number of cliques (`cliques`) based on `n` and `k`, and then fills an array `arr` using the `make_array` function. After filling the array, it prints the contents of `arr`, the number of cliques, and the updated `cliquess` list.

#State of the program right berfore the function call: left and right are integers such that 0 <= left < right < n, and clique is an integer representing the clique identifier.
def make_array(left, right, clique):
    small_element = left + 1
    big_element = right + 1
    mid = (big_element - small_element) // 2
    not_mid = right - left + 1 - mid
    for i in range(mid):
        arr[left + i] = small_element + i
        
        cliquess[left + i] = clique
        
    #State: Output State: All elements from index `left` to `left + mid - 1` in the array `arr` are set to values starting from `small_element` and incrementing by 1 for each subsequent element; `cliquess` at indices from `left` to `left + mid - 1` are all set to the value `clique`. The variable `mid` remains greater than 0 after the loop completes, indicating that there were enough elements to iterate over according to the initial conditions.
    #
    #In simpler terms, after the loop finishes executing all its iterations, the array `arr` will have its elements from index `left` to `left + mid - 1` filled with values starting from `small_element` up to `small_element + mid - 1`, and the corresponding indices in the `cliquess` array will all be set to the `clique` identifier.
    for i in range(not_mid):
        arr[left + mid + i] = big_element - i
        
        cliquess[left + mid + i] = clique
        
    #State: Output State: The array `arr` will have its elements from index `left + mid` to `left + mid + not_mid - 1` filled with values starting from `big_element - 1` down to `big_element - not_mid + 1`, and the corresponding indices in the `cliquess` array will all be set to the `clique` identifier.
    #
    #This means that after the loop has executed all its iterations, the elements in `arr` from `left + mid` to `left + mid + not_mid - 1` will contain values ranging from `big_element - 1` to `big_element - not_mid + 1` in descending order. The `cliquess` array will have the value `clique` assigned to these same indices.
#Overall this is what the function does:The function `make_array` takes three parameters: `left`, `right`, and `clique`. It fills an array `arr` and another array `cliquess` within the specified range `[left, right]` with specific values. Specifically, it sets the first half of the range to values starting from `small_element` (which is `left + 1`) and incrementing by 1, and assigns the `clique` identifier to the corresponding indices in `cliquess`. The second half of the range is filled with values starting from `big_element` (which is `right + 1`) and decrementing by 1, also assigning the `clique` identifier to the corresponding indices in `cliquess`. The function does not return anything explicitly, but modifies the `arr` and `cliquess` arrays in place.

